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
        self.verticalLayout = QtWidgets.QVBoxLayout(QHangupsConversationWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(QHangupsConversationWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.messagesWebView = QtWebKitWidgets.QWebView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(99)
        sizePolicy.setHeightForWidth(self.messagesWebView.sizePolicy().hasHeightForWidth())
        self.messagesWebView.setSizePolicy(sizePolicy)
        self.messagesWebView.setUrl(QtCore.QUrl("about:blank"))
        self.messagesWebView.setObjectName("messagesWebView")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.messageTextEdit = QtWidgets.QPlainTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageTextEdit.sizePolicy().hasHeightForWidth())
        self.messageTextEdit.setSizePolicy(sizePolicy)
        self.messageTextEdit.setObjectName("messageTextEdit")
        self.horizontalLayout.addWidget(self.messageTextEdit)
        self.sendButton = QtWidgets.QPushButton(self.layoutWidget)
        self.sendButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(QHangupsConversationWidget)
        QtCore.QMetaObject.connectSlotsByName(QHangupsConversationWidget)
        QHangupsConversationWidget.setTabOrder(self.messageTextEdit, self.sendButton)

    def retranslateUi(self, QHangupsConversationWidget):
        _translate = QtCore.QCoreApplication.translate
        QHangupsConversationWidget.setWindowTitle(_translate("QHangupsConversationWidget", "QHangups - Conversation"))
        self.sendButton.setText(_translate("QHangupsConversationWidget", "Send"))
        self.sendButton.setShortcut(_translate("QHangupsConversationWidget", "Ctrl+Return"))

from PyQt5 import QtWebKitWidgets
