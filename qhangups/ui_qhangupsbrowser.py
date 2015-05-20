# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupsbrowser.ui'
#
# Created: Wed May 20 12:38:46 2015
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

class Ui_QHangupsBrowser(object):
    def setupUi(self, QHangupsBrowser):
        QHangupsBrowser.setObjectName(_fromUtf8("QHangupsBrowser"))
        QHangupsBrowser.resize(600, 450)
        self.verticalLayout = QtGui.QVBoxLayout(QHangupsBrowser)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.browserWebView = QtWebKit.QWebView(QHangupsBrowser)
        self.browserWebView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.browserWebView.setObjectName(_fromUtf8("browserWebView"))
        self.verticalLayout.addWidget(self.browserWebView)

        self.retranslateUi(QHangupsBrowser)
        QtCore.QMetaObject.connectSlotsByName(QHangupsBrowser)

    def retranslateUi(self, QHangupsBrowser):
        QHangupsBrowser.setWindowTitle(_translate("QHangupsBrowser", "QHangups - Browser", None))

from PyQt4 import QtWebKit
