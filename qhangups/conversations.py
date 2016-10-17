import logging

from PyQt5 import QtCore, QtWidgets

from qhangups.conversationwidget import QHangupsConversationWidget
from qhangups.ui_qhangupsconversations import Ui_QHangupsConversations

logger = logging.getLogger(__name__)


class QHangupsConversations(QtWidgets.QMainWindow, Ui_QHangupsConversations):
    """Tabbed window with opened conversations"""
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.controller = controller
        self.client = None
        self.conv_list = None
        self.conv_widgets = {}

        self.controller.stopHangups.connect(self.on_stop)
        self.conversationsTabWidget.currentChanged.connect(self.on_tab_current_changed)
        self.conversationsTabWidget.tabCloseRequested.connect(self.on_tab_close_requested)

        # Install ourselves as event filter so we can catch middle mouse button (see eventFilter method)
        self.conversationsTabWidget.tabBar().installEventFilter(self)

    def init_conversations(self, client, conv_list):
        """Initialize list of conversations"""
        self.client = client
        self.conv_list = conv_list

    def eventFilter(self, obj, event):
        """Event filter for catching middle mouse button on tab and closing it"""
        if obj is self.conversationsTabWidget.tabBar():
            if event.type() == QtCore.QEvent.MouseButtonRelease and event.button() == QtCore.Qt.MidButton:
                tab_index = obj.tabAt(event.pos())
                if tab_index != -1:
                    obj.tabCloseRequested.emit(tab_index)
                    return True
        return super().eventFilter(obj, event)

    def get_conv_widget(self, conv_id):
        """Return an existing or new QHangupsConversationWidget"""
        if conv_id not in self.conv_widgets:
            conv = self.conv_list.get(conv_id)
            conv_widget = QHangupsConversationWidget(self, self.client, conv)
            self.conv_widgets[conv_id] = conv_widget
            self.conversationsTabWidget.addTab(conv_widget, "")
            conv_widget.set_title()
        return self.conv_widgets[conv_id]

    def set_conv_tab(self, conv_id, switch=False):
        """Add conversation tab (if not present) and optionally switch to it"""
        conv_widget = self.get_conv_widget(conv_id)
        conv_widget_id = self.conversationsTabWidget.indexOf(conv_widget)

        if switch:
            self.conversationsTabWidget.setCurrentWidget(conv_widget)

    def on_stop(self):
        """Remove all QHangupsConversationWidgets after stopping Hangups (callback)"""
        self.conversationsTabWidget.clear()
        self.conv_widgets = {}
        self.client = None
        self.conv_list = None
        self.close()

    def on_tab_current_changed(self, conv_widget_id):
        """Current tab changed (callback)"""
        conv_widget = self.conversationsTabWidget.widget(conv_widget_id)
        if conv_widget:
            conv_widget.set_active()

    def on_tab_close_requested(self, conv_widget_id):
        """Tab close button clicked (callback)"""
        conv_widget = self.conversationsTabWidget.widget(conv_widget_id)
        self.conversationsTabWidget.removeTab(conv_widget_id)
        del self.conv_widgets[conv_widget.conv.id_]
        if not self.conv_widgets:
            self.close()

    def save_geometry(self):
        """Save window position and size"""
        settings = QtCore.QSettings()
        settings.setValue("conversations_geometry", self.saveGeometry())

    def restore_geometry(self):
        """Restore window position and size from saved values"""
        settings = QtCore.QSettings()
        if settings.value("conversations_geometry"):
            self.restoreGeometry(settings.value("conversations_geometry"))

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
