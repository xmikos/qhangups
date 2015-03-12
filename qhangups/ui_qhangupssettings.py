# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupssettings.ui'
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

class Ui_QHangupsSettings(object):
    def setupUi(self, QHangupsSettings):
        QHangupsSettings.setObjectName(_fromUtf8("QHangupsSettings"))
        QHangupsSettings.resize(370, 140)
        self.gridLayout = QtGui.QGridLayout(QHangupsSettings)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.sendClientActiveCheckBox = QtGui.QCheckBox(QHangupsSettings)
        self.sendClientActiveCheckBox.setObjectName(_fromUtf8("sendClientActiveCheckBox"))
        self.gridLayout.addWidget(self.sendClientActiveCheckBox, 0, 0, 1, 2)
        self.sendReadStateCheckBox = QtGui.QCheckBox(QHangupsSettings)
        self.sendReadStateCheckBox.setObjectName(_fromUtf8("sendReadStateCheckBox"))
        self.gridLayout.addWidget(self.sendReadStateCheckBox, 1, 0, 1, 2)
        self.enterSendMessageCheckBox = QtGui.QCheckBox(QHangupsSettings)
        self.enterSendMessageCheckBox.setObjectName(_fromUtf8("enterSendMessageCheckBox"))
        self.gridLayout.addWidget(self.enterSendMessageCheckBox, 2, 0, 1, 2)
        self.label = QtGui.QLabel(QHangupsSettings)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.languageComboBox = QtGui.QComboBox(QHangupsSettings)
        self.languageComboBox.setObjectName(_fromUtf8("languageComboBox"))
        self.gridLayout.addWidget(self.languageComboBox, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(47, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(QHangupsSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 2)

        self.retranslateUi(QHangupsSettings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QHangupsSettings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QHangupsSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(QHangupsSettings)
        QHangupsSettings.setTabOrder(self.sendClientActiveCheckBox, self.sendReadStateCheckBox)
        QHangupsSettings.setTabOrder(self.sendReadStateCheckBox, self.enterSendMessageCheckBox)
        QHangupsSettings.setTabOrder(self.enterSendMessageCheckBox, self.languageComboBox)
        QHangupsSettings.setTabOrder(self.languageComboBox, self.buttonBox)

    def retranslateUi(self, QHangupsSettings):
        QHangupsSettings.setWindowTitle(_translate("QHangupsSettings", "QHangups - Settings", None))
        self.sendClientActiveCheckBox.setText(_translate("QHangupsSettings", "Send client active notifications", None))
        self.sendReadStateCheckBox.setText(_translate("QHangupsSettings", "Send read state notifications", None))
        self.enterSendMessageCheckBox.setText(_translate("QHangupsSettings", "Press Enter to send message (default is Ctrl+Enter)", None))
        self.label.setText(_translate("QHangupsSettings", "Language:", None))

