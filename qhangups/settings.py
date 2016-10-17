import os, glob, logging

from PyQt5 import QtCore, QtWidgets

from qhangups.ui_qhangupssettings import Ui_QHangupsSettings

logger = logging.getLogger(__name__)


class QHangupsSettings(QtWidgets.QDialog, Ui_QHangupsSettings):
    """Settings dialog"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.populate_ui()

    def populate_ui(self):
        """Load settings and populate dialog"""
        settings = QtCore.QSettings()

        self.sendClientActiveCheckBox.setChecked(settings.value("send_client_active", True, type=bool))
        self.sendReadStateCheckBox.setChecked(settings.value("send_read_state", True, type=bool))
        self.enterSendMessageCheckBox.setChecked(settings.value("enter_send_message", False, type=bool))
        self.connectionEventsCheckBox.setChecked(settings.value("connection_events", True, type=bool))
        self.autoConnectCheckBox.setChecked(settings.value("autoconnect", False, type=bool))

        lang_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "languages")

        self.languageComboBox.clear()
        self.languageComboBox.addItem(QtCore.QLocale.languageToString(QtCore.QLocale("en").language()), "en")

        for f in glob.glob(os.path.join(lang_path, "*.qm")):
            file_locale = os.path.splitext(os.path.basename(f))[0].split("_")[-1]
            file_lang = QtCore.QLocale.languageToString(QtCore.QLocale(file_locale).language())
            self.languageComboBox.addItem(file_lang, file_locale)

        language = settings.value("language")
        if not language:
            language = QtCore.QLocale.system().name().split("_")[0]

        i = self.languageComboBox.findData(language)
        if i == -1:
            self.languageComboBox.setCurrentIndex(0)
        else:
            self.languageComboBox.setCurrentIndex(i)

    def accept(self):
        """Save settings after clicking on OK button"""
        settings = QtCore.QSettings()
        settings.setValue("send_client_active", self.sendClientActiveCheckBox.isChecked())
        settings.setValue("send_read_state", self.sendReadStateCheckBox.isChecked())
        settings.setValue("enter_send_message", self.enterSendMessageCheckBox.isChecked())
        settings.setValue("language", self.languageComboBox.itemData(self.languageComboBox.currentIndex()))
        settings.setValue("connection_events", self.connectionEventsCheckBox.isChecked())
        settings.setValue("autoconnect", self.autoConnectCheckBox.isChecked())
        QtWidgets.QDialog.accept(self)
