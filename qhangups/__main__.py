#!/usr/bin/env python

import sys, os, logging, argparse, asyncio, signal

from PyQt5 import QtCore, QtGui, QtWidgets
import appdirs
import hangups
from hangups.ui.notify import Notifier

# Force use of PyQt5 for Quamash
os.environ['QUAMASH_QTIMPL'] = "PyQt5"

# Fake os.name to be always "posix" when loading QEventLoop.
# We need SelectorEventLoop on Windows because
# ProactorEventLoop doesn't support SSL in Python < 3.5
# (and Quamash uses ProactorEventLoop on Windows by default)
_os_name_orig = os.name
os.name = "posix"
from quamash import QEventLoop
os.name = _os_name_orig

from qhangups.version import __version__
from qhangups.settings import QHangupsSettings
from qhangups.conversations import QHangupsConversations
from qhangups.conversationslist import QHangupsConversationsList
from qhangups.browser import QHangupsBrowser


# Logging settings
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logger = logging.getLogger(__name__)

# Prepare Qt translators
translator = QtCore.QTranslator()
qt_translator = QtCore.QTranslator()


class CredentialsPrompt(QtCore.QObject):
    """Callbacks for prompting user for their Google account credentials."""
    def __init__(self, parent):
        super().__init__(parent) 

    def get_email(self):
        """Return Google account email address."""
        email, ok = QtWidgets.QInputDialog.getText(
            self.parent(), self.tr("QHangups - Email"), self.tr("Email:"),
            QtWidgets.QLineEdit.Normal
        )
        return email if ok else ''

    def get_password(self):
        """Return Google account password."""
        password, ok = QtWidgets.QInputDialog.getText(
            self.parent(), self.tr("QHangups - Password"), self.tr("Password:"),
            QtWidgets.QLineEdit.Password
        )
        return password if ok else ''

    def get_verification_code(self):
        """Return Google account verification code."""
        verification_code, ok = QtWidgets.QInputDialog.getText(
            self.parent(), self.tr("QHangups - Verification code"), self.tr("Verification code:"),
            QtWidgets.QLineEdit.Normal
        )
        return verification_code if ok else ''


class QHangupsMainWidget(QtWidgets.QWidget):
    """QHangups main widget (icon in system tray)"""
    startHangups = QtCore.pyqtSignal()
    stopHangups = QtCore.pyqtSignal()

    def __init__(self, refresh_token_path, parent=None):
        super().__init__(parent)
        self.set_language()

        self.refresh_token_path = refresh_token_path
        self.hangups_running = False
        self.client = None

        self.create_actions()
        self.create_menu()
        self.create_icon()
        self.update_status()

        # These are populated by on_connect when it's called.
        self.conv_list = None  # hangups.ConversationList
        self.user_list = None  # hangups.UserList
        self.notifier = None   # hangups.notify.Notifier

        # Widgets
        self.conversations_dialog = QHangupsConversationsList(controller=self)
        self.messages_dialog = QHangupsConversations(controller=self)

        # Setup system tray icon doubleclick timer
        self.icon_doubleclick_timer = QtCore.QTimer(self)
        self.icon_doubleclick_timer.setSingleShot(True)
        self.icon_doubleclick_timer.timeout.connect(self.icon_doubleclick_timeout)

        # Handle signals on Unix
        # (add_signal_handler is not implemented on Windows)
        try:
            loop = asyncio.get_event_loop()
            for signum in (signal.SIGINT, signal.SIGTERM):
                loop.add_signal_handler(signum, lambda: self.quit(force=True))
        except NotImplementedError:
            pass

        settings = QtCore.QSettings()

        if settings.value("autoconnect", False, type=bool):
            self.hangups_start()

    def create_actions(self):
        """Create actions and connect relevant signals"""
        self.startAction = QtWidgets.QAction(self)
        self.startAction.triggered.connect(self.hangups_start)
        self.stopAction = QtWidgets.QAction(self)
        self.stopAction.triggered.connect(self.hangups_stop)
        self.settingsAction = QtWidgets.QAction(self)
        self.settingsAction.triggered.connect(self.settings)
        self.aboutAction = QtWidgets.QAction(self)
        self.aboutAction.triggered.connect(self.about)
        self.quitAction = QtWidgets.QAction(self)
        self.quitAction.triggered.connect(self.quit)

    def create_menu(self):
        """Create menu and add items to it"""
        self.trayIconMenu = QtWidgets.QMenu(self)
        self.trayIconMenu.addAction(self.startAction)
        self.trayIconMenu.addAction(self.stopAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.settingsAction)
        self.trayIconMenu.addAction(self.aboutAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)

    def create_icon(self):
        """Create system tray icon"""
        self.trayIcon = QtWidgets.QSystemTrayIcon(self)
        self.iconActive = QtGui.QIcon("{}/qhangups.svg".format(os.path.dirname(os.path.abspath(__file__))))
        self.iconDisabled = QtGui.QIcon("{}/qhangups_disabled.svg".format(os.path.dirname(os.path.abspath(__file__))))
        # Workaround for Plasma 5 not showing SVG icons
        self.iconActive = QtGui.QIcon(self.iconActive.pixmap(128, 128))
        self.iconDisabled = QtGui.QIcon(self.iconDisabled.pixmap(128, 128))

        self.trayIcon.activated.connect(self.icon_activated)
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.setIcon(self.iconDisabled)
        self.trayIcon.setToolTip("QHangups")
        self.trayIcon.show()

    def retranslateUi(self):
        """Retranslate GUI"""
        self.startAction.setText(self.tr("&Connect"))
        self.stopAction.setText(self.tr("&Disconnect"))
        self.settingsAction.setText(self.tr("S&ettings ..."))
        self.aboutAction.setText(self.tr("A&bout ..."))
        self.quitAction.setText(self.tr("&Quit"))

    def login(self, refresh_token_path):
        """Login to Google account"""
        try:
            refresh_token_cache = hangups.auth.RefreshTokenCache(refresh_token_path)
            cookies = hangups.auth.get_auth(CredentialsPrompt(self), refresh_token_cache)
            return cookies
        except hangups.GoogleAuthError:
            QtWidgets.QMessageBox.warning(self, self.tr("QHangups - Warning"),
                                          self.tr("Google login failed!"))
            return False

    def get_credentials(self):
        """Ask user for OAuth 2 authorization code"""
        browser = QHangupsBrowser(hangups.auth.OAUTH2_LOGIN_URL, self).exec_()
        code, ok = QtWidgets.QInputDialog.getText(self, self.tr("QHangups - Authorization"),
                                                  self.tr("Authorization code:"),
                                                  QtWidgets.QLineEdit.Normal)
        if ok and code:
            return code
        else:
            return None

    def update_status(self):
        """Update GUI according to Hangups status"""
        if self.hangups_running:
            self.trayIcon.setIcon(self.iconActive)
            self.startAction.setEnabled(False)
            self.stopAction.setEnabled(True)
        else:
            self.trayIcon.setIcon(self.iconDisabled)
            self.startAction.setEnabled(True)
            self.stopAction.setEnabled(False)

    def hangups_start(self):
        """Connect to Hangouts"""
        cookies = self.login(self.refresh_token_path)
        if cookies:
            self.startHangups.emit()

            self.client = hangups.Client(cookies)
            self.client.on_connect.add_observer(self.on_connect)

            # Run Hangups event loop
            asyncio.async(
                self.client.connect()
            ).add_done_callback(lambda future: future.result())
            self.hangups_running = True
            self.update_status()

    def hangups_stop(self):
        """Disconnect from Hangouts"""
        self.stopHangups.emit()

        asyncio.async(
            self.client.disconnect()
        ).add_done_callback(lambda future: future.result())

        self.conv_list = None
        self.user_list = None
        self.notifier = None

        self.hangups_running = False
        self.client = None
        self.update_status()

    def about(self):
        """Show About dialog"""
        QtWidgets.QMessageBox.information(self, self.tr("About"), self.tr("QHangups {}".format(__version__)))

    def settings(self):
        """Show Settings dialog"""
        dialog = QHangupsSettings(self)
        if dialog.exec_():
            self.set_language()
            if self.hangups_running:
                self.hangups_stop()
                self.hangups_start()

    def set_language(self):
        """Change language"""
        settings = QtCore.QSettings()

        language = settings.value("language")
        if not language:
            language = QtCore.QLocale.system().name().split("_")[0]

        lang_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "languages")
        lang_file = "qhangups_{}.qm".format(language)

        qt_lang_path = QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
        qt_lang_file = "qt_{}.qm".format(language)

        if os.path.isfile(os.path.join(lang_path, lang_file)):
            translator.load(lang_file, lang_path)
            qt_translator.load(qt_lang_file, qt_lang_path)
        else:
            translator.load("")
            qt_translator.load("")

    def icon_activated(self, reason):
        """Connect or disconnect from Hangouts by double-click on tray icon"""
        if reason == QtWidgets.QSystemTrayIcon.Trigger or reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            if self.icon_doubleclick_timer.isActive():
                self.icon_doubleclick_timer.stop()
                if self.hangups_running:
                    self.hangups_stop()
                else:
                    self.hangups_start()
            else:
                self.icon_doubleclick_timer.start(QtWidgets.qApp.doubleClickInterval())

    def icon_doubleclick_timeout(self):
        """Open or close list of conversations after single-click on tray icon"""
        if self.conversations_dialog:
            if self.conversations_dialog.isVisible() and not self.conversations_dialog.isMinimized():
                self.conversations_dialog.hide()
            else:
                self.conversations_dialog.showNormal()
                self.conversations_dialog.raise_()
                self.conversations_dialog.activateWindow()

    def quit(self, force=False):
        """Quit QHangups"""
        if self.hangups_running:
            if not force:
                reply = QtWidgets.QMessageBox.question(self, self.tr("QHangups - Quit"),
                                                       self.tr("You are still connected to Google Hangouts. "
                                                               "Do you really want to quit QHangups?"),
                                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                       QtWidgets.QMessageBox.No)
                if reply != QtWidgets.QMessageBox.Yes:
                    return
            self.hangups_stop()

        loop = asyncio.get_event_loop()
        loop.stop()
        # QtWidgets.qApp.quit()

    def changeEvent(self, event):
        """Handle LanguageChange event"""
        if (event.type() == QtCore.QEvent.LanguageChange):
            logger.debug("Language changed")
            self.retranslateUi()

        super().changeEvent(event)

    def open_messages_dialog(self, conv_id, switch=True):
        """Open conversation in new tab"""
        self.messages_dialog.set_conv_tab(conv_id, switch=switch)
        self.messages_dialog.showNormal()
        if switch:
            self.messages_dialog.raise_()
            self.messages_dialog.activateWindow()

    @asyncio.coroutine
    def on_connect(self):
        """Handle connecting for the first time (callback)"""
        logger.debug('Connected')

        self.user_list, self.conv_list = (
            yield from hangups.build_user_conversation_list(self.client)
        )
        self.conv_list.on_event.add_observer(self.on_event)

        # Setup notifications
        self.notifier = Notifier(self.conv_list)

        # Setup conversations window
        self.messages_dialog.init_conversations(self.client, self.conv_list)

        # Setup conversations list window and show it
        self.conversations_dialog.init_conversations(self.client, self.conv_list)
        self.conversations_dialog.show()

    @asyncio.coroutine
    def on_event(self, conv_event):
        """Open conversation tab for new messages when they arrive (callback)"""
        if isinstance(conv_event, hangups.ChatMessageEvent):
            self.open_messages_dialog(conv_event.conversation_id, switch=False)


def main():
    # Build default paths for files.
    dirs = appdirs.AppDirs('QHangups', 'QHangups')
    default_log_path = os.path.join(dirs.user_data_dir, 'hangups.log')
    default_token_path = os.path.join(dirs.user_data_dir, 'refresh_token.txt')

    # Setup command line argument parser
    parser = argparse.ArgumentParser(prog='qhangups',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-d', '--debug', action='store_true',
                        help='log detailed debugging messages')
    parser.add_argument('--log', default=default_log_path,
                        help='log file path')
    parser.add_argument('--token', default=default_token_path,
                        help='OAuth refresh token storage path')
    args = parser.parse_args()

    # Create all necessary directories.
    for path in [args.log, args.token]:
        directory = os.path.dirname(path)
        if directory and not os.path.isdir(directory):
            try:
                os.makedirs(directory)
            except OSError as e:
                sys.exit('Failed to create directory: {}'.format(e))

    # Setup logging
    log_level = logging.DEBUG if args.debug else logging.WARNING
    logging.basicConfig(filename=args.log, level=log_level, format=LOG_FORMAT)
    # asyncio's debugging logs are VERY noisy, so adjust the log level
    logging.getLogger('asyncio').setLevel(logging.WARNING)
    # ...and if we don't need Hangups debug logs, then uncomment this:
    # logging.getLogger('hangups').setLevel(logging.WARNING)

    # Setup QApplication
    app = QtWidgets.QApplication(sys.argv)
    app.setOrganizationName("QHangups")
    app.setOrganizationDomain("qhangups.eutopia.cz")
    app.setApplicationName("QHangups")
    app.setQuitOnLastWindowClosed(False)
    app.installTranslator(translator)
    app.installTranslator(qt_translator)

    # Start Quamash event loop
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    with loop:
        widget = QHangupsMainWidget(args.token)
        loop.run_forever()


if __name__ == "__main__":
    main()
