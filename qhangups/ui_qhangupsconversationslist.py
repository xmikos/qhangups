# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupsconversationslist.ui'
#
# Created: Thu Mar 12 14:06:14 2015
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

class Ui_QHangupsConversationsList(object):
    def setupUi(self, QHangupsConversationsList):
        QHangupsConversationsList.setObjectName(_fromUtf8("QHangupsConversationsList"))
        QHangupsConversationsList.resize(250, 500)
        self.centralwidget = QtGui.QWidget(QHangupsConversationsList)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.conversationsListWidget = QtGui.QListWidget(self.centralwidget)
        self.conversationsListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.conversationsListWidget.setObjectName(_fromUtf8("conversationsListWidget"))
        self.verticalLayout.addWidget(self.conversationsListWidget)
        QHangupsConversationsList.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(QHangupsConversationsList)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        QHangupsConversationsList.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(QHangupsConversationsList)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        QHangupsConversationsList.setStatusBar(self.statusbar)

        self.retranslateUi(QHangupsConversationsList)
        QtCore.QMetaObject.connectSlotsByName(QHangupsConversationsList)

    def retranslateUi(self, QHangupsConversationsList):
        QHangupsConversationsList.setWindowTitle(_translate("QHangupsConversationsList", "QHangups", None))

