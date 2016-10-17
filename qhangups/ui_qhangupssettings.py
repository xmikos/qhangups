# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qhangups/qhangupssettings.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_QHangupsSettings(object):
    def setupUi(self, QHangupsSettings):
        QHangupsSettings.setObjectName("QHangupsSettings")
        QHangupsSettings.resize(375, 159)
        self.gridLayout = QtWidgets.QGridLayout(QHangupsSettings)
        self.gridLayout.setObjectName("gridLayout")
        self.sendReadStateCheckBox = QtWidgets.QCheckBox(QHangupsSettings)
        self.sendReadStateCheckBox.setObjectName("sendReadStateCheckBox")
        self.gridLayout.addWidget(self.sendReadStateCheckBox, 1, 0, 1, 2)
        self.connectionEventsCheckBox = QtWidgets.QCheckBox(QHangupsSettings)
        self.connectionEventsCheckBox.setObjectName("connectionEventsCheckBox")
        self.gridLayout.addWidget(self.connectionEventsCheckBox, 3, 0, 1, 3)
        self.buttonBox = QtWidgets.QDialogButtonBox(QHangupsSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 6, 1, 1, 2)
        self.label = QtWidgets.QLabel(QHangupsSettings)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.sendClientActiveCheckBox = QtWidgets.QCheckBox(QHangupsSettings)
        self.sendClientActiveCheckBox.setObjectName("sendClientActiveCheckBox")
        self.gridLayout.addWidget(self.sendClientActiveCheckBox, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(47, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 2, 1, 1)
        self.enterSendMessageCheckBox = QtWidgets.QCheckBox(QHangupsSettings)
        self.enterSendMessageCheckBox.setObjectName("enterSendMessageCheckBox")
        self.gridLayout.addWidget(self.enterSendMessageCheckBox, 2, 0, 1, 3)
        self.languageComboBox = QtWidgets.QComboBox(QHangupsSettings)
        self.languageComboBox.setObjectName("languageComboBox")
        self.gridLayout.addWidget(self.languageComboBox, 5, 1, 1, 1)
        self.autoConnectCheckBox = QtWidgets.QCheckBox(QHangupsSettings)
        self.autoConnectCheckBox.setObjectName("autoConnectCheckBox")
        self.gridLayout.addWidget(self.autoConnectCheckBox, 4, 0, 1, 1)

        self.retranslateUi(QHangupsSettings)
        self.buttonBox.accepted.connect(QHangupsSettings.accept)
        self.buttonBox.rejected.connect(QHangupsSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(QHangupsSettings)
        QHangupsSettings.setTabOrder(self.sendClientActiveCheckBox, self.sendReadStateCheckBox)
        QHangupsSettings.setTabOrder(self.sendReadStateCheckBox, self.enterSendMessageCheckBox)
        QHangupsSettings.setTabOrder(self.enterSendMessageCheckBox, self.languageComboBox)
        QHangupsSettings.setTabOrder(self.languageComboBox, self.buttonBox)

    def retranslateUi(self, QHangupsSettings):
        _translate = QtCore.QCoreApplication.translate
        QHangupsSettings.setWindowTitle(_translate("QHangupsSettings", "QHangups - Settings"))
        self.sendReadStateCheckBox.setText(_translate("QHangupsSettings", "Send read state notifications"))
        self.connectionEventsCheckBox.setText(_translate("QHangupsSettings", "Connection events in feed"))
        self.label.setText(_translate("QHangupsSettings", "Language:"))
        self.sendClientActiveCheckBox.setText(_translate("QHangupsSettings", "Send client active notifications"))
        self.enterSendMessageCheckBox.setText(_translate("QHangupsSettings", "Press Enter to send message (default is Ctrl+Enter)"))
        self.autoConnectCheckBox.setText(_translate("QHangupsSettings", "Auto-connect"))

