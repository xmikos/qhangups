# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupsconversationslist.ui'
#
# Created: Fri Sep 26 12:58:44 2014
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

class Ui_QHangupsConversationsList(object):
    def setupUi(self, QHangupsConversationsList):
        QHangupsConversationsList.setObjectName(_fromUtf8("QHangupsConversationsList"))
        QHangupsConversationsList.resize(250, 500)
        self.gridLayout = QtGui.QGridLayout(QHangupsConversationsList)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.conversationsListWidget = QtGui.QListWidget(QHangupsConversationsList)
        self.conversationsListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.conversationsListWidget.setObjectName(_fromUtf8("conversationsListWidget"))
        self.gridLayout.addWidget(self.conversationsListWidget, 0, 0, 1, 1)

        self.retranslateUi(QHangupsConversationsList)
        QtCore.QMetaObject.connectSlotsByName(QHangupsConversationsList)

    def retranslateUi(self, QHangupsConversationsList):
        QHangupsConversationsList.setWindowTitle(_translate("QHangupsConversationsList", "QHangups", None))

