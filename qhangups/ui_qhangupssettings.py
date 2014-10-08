# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupssettings.ui'
#
# Created: Wed Oct  8 17:32:26 2014
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

class Ui_QHangupsSettings(object):
    def setupUi(self, QHangupsSettings):
        QHangupsSettings.setObjectName(_fromUtf8("QHangupsSettings"))
        QHangupsSettings.resize(300, 130)
        self.gridLayout = QtGui.QGridLayout(QHangupsSettings)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.sendClientActiveCheckBox = QtGui.QCheckBox(QHangupsSettings)
        self.sendClientActiveCheckBox.setObjectName(_fromUtf8("sendClientActiveCheckBox"))
        self.gridLayout.addWidget(self.sendClientActiveCheckBox, 0, 0, 1, 2)
        self.sendReadStateCheckBox = QtGui.QCheckBox(QHangupsSettings)
        self.sendReadStateCheckBox.setObjectName(_fromUtf8("sendReadStateCheckBox"))
        self.gridLayout.addWidget(self.sendReadStateCheckBox, 1, 0, 1, 2)
        self.label = QtGui.QLabel(QHangupsSettings)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.languageComboBox = QtGui.QComboBox(QHangupsSettings)
        self.languageComboBox.setObjectName(_fromUtf8("languageComboBox"))
        self.gridLayout.addWidget(self.languageComboBox, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(QHangupsSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 1)

        self.retranslateUi(QHangupsSettings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QHangupsSettings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QHangupsSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(QHangupsSettings)

    def retranslateUi(self, QHangupsSettings):
        QHangupsSettings.setWindowTitle(_translate("QHangupsSettings", "QHangups - Settings", None))
        self.sendClientActiveCheckBox.setText(_translate("QHangupsSettings", "Send client active notifications", None))
        self.sendReadStateCheckBox.setText(_translate("QHangupsSettings", "Send read state notifications", None))
        self.label.setText(_translate("QHangupsSettings", "Language:", None))

