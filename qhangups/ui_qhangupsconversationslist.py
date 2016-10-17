# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupsconversationslist.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QHangupsConversationsList(object):
    def setupUi(self, QHangupsConversationsList):
        QHangupsConversationsList.setObjectName("QHangupsConversationsList")
        QHangupsConversationsList.resize(250, 500)
        self.centralwidget = QtWidgets.QWidget(QHangupsConversationsList)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.conversationsListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.conversationsListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.conversationsListWidget.setObjectName("conversationsListWidget")
        self.verticalLayout.addWidget(self.conversationsListWidget)
        QHangupsConversationsList.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QHangupsConversationsList)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 27))
        self.menubar.setObjectName("menubar")
        QHangupsConversationsList.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QHangupsConversationsList)
        self.statusbar.setObjectName("statusbar")
        QHangupsConversationsList.setStatusBar(self.statusbar)

        self.retranslateUi(QHangupsConversationsList)
        QtCore.QMetaObject.connectSlotsByName(QHangupsConversationsList)

    def retranslateUi(self, QHangupsConversationsList):
        _translate = QtCore.QCoreApplication.translate
        QHangupsConversationsList.setWindowTitle(_translate("QHangupsConversationsList", "QHangups"))

