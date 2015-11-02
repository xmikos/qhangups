# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupsconversationwidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QHangupsConversationWidget(object):
    def setupUi(self, QHangupsConversationWidget):
        QHangupsConversationWidget.setObjectName("QHangupsConversationWidget")
        QHangupsConversationWidget.resize(500, 350)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(QHangupsConversationWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.messagesFrame = QtWidgets.QFrame(QHangupsConversationWidget)
        self.messagesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.messagesFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.messagesFrame.setObjectName("messagesFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.messagesFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.messagesWebView = QtWebKitWidgets.QWebView(self.messagesFrame)
        self.messagesWebView.setUrl(QtCore.QUrl("about:blank"))
        self.messagesWebView.setObjectName("messagesWebView")
        self.verticalLayout.addWidget(self.messagesWebView)
        self.verticalLayout_2.addWidget(self.messagesFrame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.messageTextEdit = QtWidgets.QPlainTextEdit(QHangupsConversationWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageTextEdit.sizePolicy().hasHeightForWidth())
        self.messageTextEdit.setSizePolicy(sizePolicy)
        self.messageTextEdit.setMaximumSize(QtCore.QSize(16777215, 60))
        self.messageTextEdit.setObjectName("messageTextEdit")
        self.horizontalLayout.addWidget(self.messageTextEdit)
        self.sendButton = QtWidgets.QPushButton(QHangupsConversationWidget)
        self.sendButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(QHangupsConversationWidget)
        QtCore.QMetaObject.connectSlotsByName(QHangupsConversationWidget)
        QHangupsConversationWidget.setTabOrder(self.messageTextEdit, self.sendButton)
        QHangupsConversationWidget.setTabOrder(self.sendButton, self.messagesWebView)

    def retranslateUi(self, QHangupsConversationWidget):
        _translate = QtCore.QCoreApplication.translate
        QHangupsConversationWidget.setWindowTitle(_translate("QHangupsConversationWidget", "QHangups - Conversation"))
        self.sendButton.setText(_translate("QHangupsConversationWidget", "Send"))
        self.sendButton.setShortcut(_translate("QHangupsConversationWidget", "Ctrl+Return"))

from PyQt5 import QtWebKitWidgets
