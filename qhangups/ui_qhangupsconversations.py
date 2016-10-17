# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupsconversations.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QHangupsConversations(object):
    def setupUi(self, QHangupsConversations):
        QHangupsConversations.setObjectName("QHangupsConversations")
        QHangupsConversations.resize(500, 350)
        self.centralwidget = QtWidgets.QWidget(QHangupsConversations)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.conversationsTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.conversationsTabWidget.setElideMode(QtCore.Qt.ElideRight)
        self.conversationsTabWidget.setTabsClosable(True)
        self.conversationsTabWidget.setMovable(True)
        self.conversationsTabWidget.setObjectName("conversationsTabWidget")
        self.gridLayout.addWidget(self.conversationsTabWidget, 0, 0, 1, 1)
        QHangupsConversations.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QHangupsConversations)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 27))
        self.menubar.setObjectName("menubar")
        QHangupsConversations.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QHangupsConversations)
        self.statusbar.setObjectName("statusbar")
        QHangupsConversations.setStatusBar(self.statusbar)

        self.retranslateUi(QHangupsConversations)
        self.conversationsTabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(QHangupsConversations)

    def retranslateUi(self, QHangupsConversations):
        _translate = QtCore.QCoreApplication.translate
        QHangupsConversations.setWindowTitle(_translate("QHangupsConversations", "QHangups - Conversations"))

