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

    def get_conv_widget(self, conv_id):
        """Return an existing or new QHangupsConversationWidget"""
        if conv_id not in self.conv_widgets:
            conv = self.conv_list.get(conv_id)
            conv_widget = QHangupsConversationWidget(self, self.client, conv)
            self.conv_widgets[conv_id] = conv_widget
            self.conversationsTabWidget.addTab(conv_widget, "")
            conv_widget.set_title()
        return self.conv_widgets[conv_id]

    def set_conv_tab(self, conv_id, switch=False, title=None):
        """Add conversation tab (if not present) and optionally switch to it"""
        conv_widget = self.get_conv_widget(conv_id)
        conv_widget_id = self.conversationsTabWidget.indexOf(conv_widget)

        if switch:
            self.conversationsTabWidget.setCurrentWidget(conv_widget)

        if title:
            self.conversationsTabWidget.setTabText(conv_widget_id, title)
            self.conversationsTabWidget.setTabToolTip(conv_widget_id, title)

    def on_tab_current_changed(self, conv_widget_id):
        """Current tab changed (callback)"""
        conv_widget = self.conversationsTabWidget.widget(conv_widget_id)
        if conv_widget:
            conv_widget.num_unread = 0
            conv_widget.set_title()

    def on_tab_close_requested(self, conv_widget_id):
        """Tab close button clicked (callback)"""
        conv_widget = self.conversationsTabWidget.widget(conv_widget_id)
        self.conversationsTabWidget.removeTab(conv_widget_id)
        del self.conv_widgets[conv_widget.conv.id_]
        if not self.conv_widgets:
            self.close()
