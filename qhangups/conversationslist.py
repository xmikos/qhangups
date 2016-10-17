import logging

from PyQt5 import QtCore, QtWidgets

import hangups
from hangups.ui.utils import get_conv_name

from qhangups.ui_qhangupsconversationslist import Ui_QHangupsConversationsList

logger = logging.getLogger(__name__)


class QHangupsConversationsList(QtWidgets.QMainWindow, Ui_QHangupsConversationsList):
    """Window with list of conversations"""
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.controller = controller
        self.client = None
        self.conv_list = None

        self.controller.startHangups.connect(self.on_start)
        self.controller.stopHangups.connect(self.on_stop)

        self.set_status(self.tr("Disconnected"))

    def init_conversations(self, client, conv_list):
        """Initialize list of conversations and connect signals"""
        self.client = client
        self.conv_list = conv_list

        self.conv_list.on_event.add_observer(self.on_event)
        self.client.on_disconnect.add_observer(self.on_disconnect)
        self.client.on_reconnect.add_observer(self.on_reconnect)
        self.conversationsListWidget.itemActivated.connect(self.on_item_activated)

        self.update_conversations()

    def set_status(self, status_text):
        """Display static status text instead of list of conversations"""
        self.conversationsListWidget.clear()
        item = QtWidgets.QListWidgetItem(status_text)
        item.setTextAlignment(QtCore.Qt.AlignHCenter)
        self.conversationsListWidget.addItem(item)

    def update_conversations(self):
        """Update list of conversations"""
        self.conversationsListWidget.clear()
        for conv in sorted(self.conv_list.get_all(), reverse=True, key=lambda c: c.last_modified):
            item = QtWidgets.QListWidgetItem(get_conv_name(conv, truncate=True))
            item.setToolTip(get_conv_name(conv))
            item.setData(QtCore.Qt.UserRole, conv.id_)
            self.conversationsListWidget.addItem(item)

    def on_item_activated(self, item):
        """List item activated (callback)"""
        item_data = item.data(QtCore.Qt.UserRole)
        if item_data:
            self.controller.open_messages_dialog(item_data)

    def on_event(self, conv_event):
        """Hangups event received (callback)"""
        if isinstance(conv_event, hangups.RenameEvent):
            self.update_conversations()

    def on_disconnect(self):
        """Show that Hangups has disconnected from server (callback)"""
        self.set_status(self.tr("Reconnecting..."))

    def on_reconnect(self):
        """Show that Hangups has reconnected to server (callback)"""
        self.update_conversations()

    def on_start(self):
        """Show that Hangups is starting (callback)"""
        self.set_status(self.tr("Connecting..."))

    def on_stop(self):
        """Show that Hangups has been stopped (callback)"""
        self.client = None
        self.conv_list = None
        self.set_status(self.tr("Disconnected"))

    def save_geometry(self):
        """Save window position and size"""
        settings = QtCore.QSettings()
        settings.setValue("conversationslist_geometry", self.saveGeometry())

    def restore_geometry(self):
        """Restore window position and size from saved values"""
        settings = QtCore.QSettings()
        if settings.value("conversationslist_geometry"):
            self.restoreGeometry(settings.value("conversationslist_geometry"))

    def showEvent(self, event):
        """Restore window geometry when window is displayed"""
        # If we don't use single-shot timer, position is not restored
        # correctly from minimized state on Windows
        QtCore.QTimer.singleShot(0, self.restore_geometry)
        super().showEvent(event)

    def hideEvent(self, event):
        """Save window geometry when window is hidden"""
        self.save_geometry()
        super().hideEvent(event)
