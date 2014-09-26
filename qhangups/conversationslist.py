from PyQt4 import QtCore, QtGui

import hangups
from hangups.ui.utils import get_conv_name

from qhangups.ui_qhangupsconversationslist import Ui_QHangupsConversationsList


class QHangupsConversationsList(QtGui.QDialog, Ui_QHangupsConversationsList):
    """Window with list of conversations"""
    def __init__(self, client, conv_list, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.client = client
        self.conv_list = conv_list

        self.conv_list.on_event.add_observer(self.on_event)
        self.conversationsListWidget.itemActivated.connect(self.on_item_activated)

        self.update_conversations()

    def update_conversations(self):
        """Update list of conversations"""
        self.conversationsListWidget.clear()
        for conv in sorted(self.conv_list.get_all(), reverse=True, key=lambda c: c.last_modified):
            item = QtGui.QListWidgetItem(get_conv_name(conv, truncate=True))
            item.setToolTip(get_conv_name(conv))
            item.setData(QtCore.Qt.UserRole, conv.id_)
            self.conversationsListWidget.addItem(item)

    def on_item_activated(self, item):
        """List item activated (callback)"""
        self.parent().open_messages_dialog(item.data(QtCore.Qt.UserRole))

    def on_event(self, conv_event):
        """Hangups event received (callback)"""
        if isinstance(conv_event, hangups.RenameEvent):
            self.update_conversations()
