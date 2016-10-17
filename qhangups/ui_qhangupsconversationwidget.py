# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupsconversationwidget.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QHangupsConversationWidget(object):
    def setupUi(self, QHangupsConversationWidget):
        QHangupsConversationWidget.setObjectName("QHangupsConversationWidget")
        QHangupsConversationWidget.resize(600, 400)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(QHangupsConversationWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(QHangupsConversationWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.messagesFrame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(250)
        sizePolicy.setHeightForWidth(self.messagesFrame.sizePolicy().hasHeightForWidth())
        self.messagesFrame.setSizePolicy(sizePolicy)
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
        self.frame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 60))
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, -1, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.messageTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.messageTextEdit.setObjectName("messageTextEdit")
        self.horizontalLayout.addWidget(self.messageTextEdit)
        self.sendButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout_2.addWidget(self.splitter)

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
