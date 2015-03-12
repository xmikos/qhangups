# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupsconversationwidget.ui'
#
# Created: Thu Mar 12 14:06:13 2015
#      by: PyQt4 UI code generator 4.11.3
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
        self.verticalLayout_2 = QtGui.QVBoxLayout(QHangupsConversationWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.messagesFrame = QtGui.QFrame(QHangupsConversationWidget)
        self.messagesFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.messagesFrame.setFrameShadow(QtGui.QFrame.Sunken)
        self.messagesFrame.setObjectName(_fromUtf8("messagesFrame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.messagesFrame)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.messagesWebView = QtWebKit.QWebView(self.messagesFrame)
        self.messagesWebView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.messagesWebView.setObjectName(_fromUtf8("messagesWebView"))
        self.verticalLayout.addWidget(self.messagesWebView)
        self.verticalLayout_2.addWidget(self.messagesFrame)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(QHangupsConversationWidget)
        QtCore.QMetaObject.connectSlotsByName(QHangupsConversationWidget)
        QHangupsConversationWidget.setTabOrder(self.messageTextEdit, self.sendButton)
        QHangupsConversationWidget.setTabOrder(self.sendButton, self.messagesWebView)

    def retranslateUi(self, QHangupsConversationWidget):
        QHangupsConversationWidget.setWindowTitle(_translate("QHangupsConversationWidget", "QHangups - Conversation", None))
        self.sendButton.setText(_translate("QHangupsConversationWidget", "Send", None))
        self.sendButton.setShortcut(_translate("QHangupsConversationWidget", "Ctrl+Return", None))

from PyQt4 import QtWebKit
