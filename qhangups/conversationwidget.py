import datetime, asyncio

from PyQt4 import QtCore, QtGui

import hangups
from hangups.utils import get_conv_name

from qhangups.utils import text_to_segments, message_to_html
from qhangups.ui_qhangupsconversationwidget import Ui_QHangupsConversationWidget


class HTMLDelegate(QtGui.QStyledItemDelegate):
    """QStyledItemDelegate implementation - draws HTML instead of plain text
    http://stackoverflow.com/questions/1956542/how-to-make-item-view-render-rich-html-text-in-qt/1956781#1956781
    """
    def paint(self, painter, option, index):
        """QStyledItemDelegate.paint implementation"""
        option.state &= ~QtGui.QStyle.State_HasFocus  # never draw focus rect

        options = QtGui.QStyleOptionViewItemV4(option)
        self.initStyleOption(options, index)

        style = QtGui.QApplication.style() if options.widget is None else options.widget.style()

        doc = QtGui.QTextDocument()
        doc.setDocumentMargin(1)
        doc.setHtml(options.text)
        if options.widget is not None:
            doc.setDefaultFont(options.widget.font())
        # bad long (multiline) strings processing
        doc.setTextWidth(options.rect.width())

        options.text = ""
        style.drawControl(QtGui.QStyle.CE_ItemViewItem, options, painter)

        ctx = QtGui.QAbstractTextDocumentLayout.PaintContext()

        # Highlighting text if item is selected
        if option.state & QtGui.QStyle.State_Selected:
            ctx.palette.setColor(QtGui.QPalette.Text, option.palette.color(QtGui.QPalette.Active,
                                                                           QtGui.QPalette.HighlightedText))

        textRect = style.subElementRect(QtGui.QStyle.SE_ItemViewItemText, options)
        painter.save()
        painter.translate(textRect.topLeft())
        # Original example contained line
        # painter.setClipRect(textRect.translated(-textRect.topLeft()))
        # but text is drawn clipped with it on kubuntu 12.04
        doc.documentLayout().draw(painter, ctx)

        painter.restore()

    def sizeHint(self, option, index):
        """QStyledItemDelegate.sizeHint implementation"""
        options = QtGui.QStyleOptionViewItemV4(option)
        self.initStyleOption(options, index)

        doc = QtGui.QTextDocument()
        doc.setDocumentMargin(1)
        #  bad long (multiline) strings processing
        doc.setTextWidth(options.rect.width())
        doc.setHtml(options.text)
        return QtCore.QSize(doc.idealWidth(),
                            QtGui.QStyledItemDelegate.sizeHint(self, option, index).height())


class QHangupsConversationWidget(QtGui.QWidget, Ui_QHangupsConversationWidget):
    """Conversation tab"""
    def __init__(self, tab_parent, client, conv, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.messagesListWidget.setItemDelegate(HTMLDelegate(self.messagesListWidget))

        self.tab_parent = tab_parent
        self.client = client
        self.conv = conv

        self.client.on_disconnect.add_observer(self.on_disconnect)
        self.client.on_reconnect.add_observer(self.on_reconnect)
        self.conv.on_event.add_observer(self.on_event)

        self.sendButton.clicked.connect(self.on_send_clicked)

        self.num_unread = 0
        for event in self.conv.events:
            self.on_event(event, set_title=False, set_unread=False)

    def set_title(self):
        """Update this conversation's tab title."""
        title = get_conv_name(self.conv, truncate=True)
        conv_widget_id = self.tab_parent.conversationsTabWidget.indexOf(self)
        if self.num_unread > 0:
            title += ' ({})'.format(self.num_unread)
            self.tab_parent.conversationsTabWidget.tabBar().setTabTextColor(conv_widget_id, QtCore.Qt.darkBlue)
        else:
            self.tab_parent.conversationsTabWidget.tabBar().setTabTextColor(conv_widget_id, QtGui.QColor())
        self.tab_parent.conversationsTabWidget.setTabText(conv_widget_id, title)
        self.tab_parent.conversationsTabWidget.setTabToolTip(conv_widget_id, title)

    def add_message(self, timestamp, text, username=None):
        """Add new message to list of messages"""
        datestr = "%d.%m. %H:%M" if timestamp.astimezone(tz=None).date() < datetime.date.today() else "%H:%M"
        message = "<b>{}{}:</b><br>\n{}<br>\n".format(timestamp.astimezone(tz=None).strftime(datestr),
                                                      " | {}".format(username) if username is not None else "",
                                                      text)
        item = QtGui.QListWidgetItem(message)
        self.messagesListWidget.addItem(item)
        self.messagesListWidget.scrollToBottom()

    def is_current(self):
        """Is this conversation in current tab?"""
        return self.tab_parent.conversationsTabWidget.currentWidget() is self

    def on_send_clicked(self):
        """Send button pressed (callback)"""
        text = self.messageTextEdit.toPlainText()
        if not text.strip():
            return

        self.messageTextEdit.setEnabled(False)
        self.sendButton.setEnabled(False)

        segments = text_to_segments(text)
        asyncio.async(
            self.conv.send_message(segments)
        ).add_done_callback(self.on_message_sent)

    def on_message_sent(self, future):
        """Handle showing an error if a message fails to send (callback)"""
        try:
            future.result()
        except hangups.NetworkError:
            QtGui.QMessageBox.warning(self, self.tr("QHangups - Warning"),
                                      self.tr("Failed to send message!"))
        else:
            self.messageTextEdit.clear()
        finally:
            self.messageTextEdit.setEnabled(True)
            self.sendButton.setEnabled(True)

    def on_disconnect(self):
        """Show that Hangups has disconnected from server (callback)"""
        self.add_message(datetime.datetime.now(tz=datetime.timezone.utc), "<i>*** disconnected ***</i>")

    def on_reconnect(self):
        """Show that Hangups has reconnected to server (callback)"""
        self.add_message(datetime.datetime.now(tz=datetime.timezone.utc), "<i>*** connected ***</i>")

    def on_event(self, conv_event, set_title=True, set_unread=True):
        """Hangups event received (callback)"""
        user = self.conv.get_user(conv_event.user_id)

        if isinstance(conv_event, hangups.ChatMessageEvent):
            self.handle_message(conv_event, user, set_unread=set_unread)
        elif isinstance(conv_event, hangups.RenameEvent):
            self.handle_rename(conv_event, user)
        elif isinstance(conv_event, hangups.MembershipChangeEvent):
            self.handle_membership_change(conv_event, user)

        # Update the title in case unread count or conversation name changed.
        if set_title:
            self.set_title()

    def handle_message(self, conv_event, user, set_unread=True):
        """Handle received chat message"""
        self.add_message(conv_event.timestamp, message_to_html(conv_event), user.full_name)
        # Update the count of unread messages.
        if not user.is_self and set_unread and not self.is_current():
            self.num_unread += 1

    def handle_rename(self, conv_event, user):
        """Handle received rename event"""
        if conv_event.new_name == '':
            text = '<i>*** cleared the conversation name ***</i>'
        else:
            text = '<i>*** renamed the conversation to {} ***</i>'.format(conv_event.new_name)
        self.add_message(conv_event.timestamp, text, user.full_name)

    def handle_membership_change(self, conv_event, user):
        """Handle received membership change event"""
        event_users = [self.conv.get_user(user_id) for user_id in conv_event.participant_ids]
        names = ', '.join(user.full_name for user in event_users)
        if conv_event.type_ == hangups.MembershipChangeType.JOIN:
            self.add_message(conv_event.timestamp,
                             '<i>*** added {} to the conversation ***</i>'.format(names),
                             user.full_name)
        else:
            for name in names:
                self.add_message(conv_event.timestamp,
                                 '<i>*** left the conversation ***</i>',
                                 user.full_name)
