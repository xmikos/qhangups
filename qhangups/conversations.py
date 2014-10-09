import asyncio

from PyQt4 import QtCore, QtGui

from qhangups.conversationwidget import QHangupsConversationWidget
from qhangups.ui_qhangupsconversations import Ui_QHangupsConversations


class QHangupsConversations(QtGui.QDialog, Ui_QHangupsConversations):
    """Tabbed window with opened conversations"""
    def __init__(self, client, conv_list, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.client = client
        self.conv_list = conv_list
        self.conv_widgets = {}

        self.conversationsTabWidget.currentChanged.connect(self.on_tab_current_changed)
        self.conversationsTabWidget.tabCloseRequested.connect(self.on_tab_close_requested)

        # Install ourselves as event filter so we can catch middle mouse button (see eventFilter method)
        self.conversationsTabWidget.tabBar().installEventFilter(self)

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
