# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupsconversationwidget.ui'
#
# Created: Thu Oct  9 00:54:07 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_QHangupsConversationWidget(object):
    def setupUi(self, QHangupsConversationWidget):
        QHangupsConversationWidget.setObjectName(_fromUtf8("QHangupsConversationWidget"))
        QHangupsConversationWidget.resize(500, 350)
        self.verticalLayout = QtGui.QVBoxLayout(QHangupsConversationWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.messagesListWidget = QtGui.QListWidget(QHangupsConversationWidget)
        self.messagesListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messagesListWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.messagesListWidget.setWordWrap(True)
        self.messagesListWidget.setObjectName(_fromUtf8("messagesListWidget"))
        self.verticalLayout.addWidget(self.messagesListWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.messageTextEdit = QtGui.QPlainTextEdit(QHangupsConversationWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageTextEdit.sizePolicy().hasHeightForWidth())
        self.messageTextEdit.setSizePolicy(sizePolicy)
        self.messageTextEdit.setMaximumSize(QtCore.QSize(16777215, 60))
        self.messageTextEdit.setObjectName(_fromUtf8("messageTextEdit"))
        self.horizontalLayout.addWidget(self.messageTextEdit)
        self.sendButton = QtGui.QPushButton(QHangupsConversationWidget)
        self.sendButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(QHangupsConversationWidget)
        QtCore.QMetaObject.connectSlotsByName(QHangupsConversationWidget)

    def retranslateUi(self, QHangupsConversationWidget):
        QHangupsConversationWidget.setWindowTitle(_translate("QHangupsConversationWidget", "QHangups - Conversation", None))
        self.sendButton.setText(_translate("QHangupsConversationWidget", "Send", None))
        self.sendButton.setShortcut(_translate("QHangupsConversationWidget", "Ctrl+Return", None))

