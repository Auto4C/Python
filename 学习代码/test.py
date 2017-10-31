# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testui_1.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(431, 215)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 20, 60, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 60, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.inputbox = QtWidgets.QTextEdit(Form)
        self.inputbox.setGeometry(QtCore.QRect(220, 10, 141, 31))
        self.inputbox.setObjectName("inputbox")
        self.spinRate = QtWidgets.QSpinBox(Form)
        self.spinRate.setGeometry(QtCore.QRect(220, 50, 48, 24))
        self.spinRate.setProperty("value", 5)
        self.spinRate.setObjectName("spinRate")
        self.ResultBox = QtWidgets.QTextEdit(Form)
        self.ResultBox.setGeometry(QtCore.QRect(220, 110, 104, 79))
        self.ResultBox.setObjectName("ResultBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.pushButton.setToolTip(_translate("Form", "CCC"))
        self.pushButton.setStatusTip(_translate("Form", "wwww"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.inputbox.setStatusTip(_translate("Form", "we "))
        self.inputbox.setPlaceholderText(_translate("Form", "2"))

