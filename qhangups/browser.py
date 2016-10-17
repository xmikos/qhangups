import logging

from PyQt5 import QtCore, QtWidgets

from qhangups.ui_qhangupsbrowser import Ui_QHangupsBrowser

logger = logging.getLogger(__name__)


class QHangupsBrowser(QtWidgets.QDialog, Ui_QHangupsBrowser):
    """Extremely simple web browser"""
    def __init__(self, url="", parent=None):
        super().__init__(parent)
        self.setupUi(self)

        if url:
            self.load(url)

    def load(self, url):
        """Load URL"""
        self.browserWebView.load(QtCore.QUrl.fromUserInput(url))
