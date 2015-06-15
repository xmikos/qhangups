# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupsbrowser.ui'
#
# Created: Mon Jun 15 11:28:36 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QHangupsBrowser(object):
    def setupUi(self, QHangupsBrowser):
        QHangupsBrowser.setObjectName("QHangupsBrowser")
        QHangupsBrowser.resize(600, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(QHangupsBrowser)
        self.verticalLayout.setObjectName("verticalLayout")
        self.browserWebView = QtWebKitWidgets.QWebView(QHangupsBrowser)
        self.browserWebView.setUrl(QtCore.QUrl("about:blank"))
        self.browserWebView.setObjectName("browserWebView")
        self.verticalLayout.addWidget(self.browserWebView)

        self.retranslateUi(QHangupsBrowser)
        QtCore.QMetaObject.connectSlotsByName(QHangupsBrowser)

    def retranslateUi(self, QHangupsBrowser):
        _translate = QtCore.QCoreApplication.translate
        QHangupsBrowser.setWindowTitle(_translate("QHangupsBrowser", "QHangups - Browser"))

from PyQt5 import QtWebKitWidgets
