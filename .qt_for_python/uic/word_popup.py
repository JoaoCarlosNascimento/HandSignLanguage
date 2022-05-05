# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\SRI\HandSignLanguage\menus\words_menu\word_popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setStyleSheet("")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(90, 140, 25, 19))
        self.toolButton.setObjectName("toolButton")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(70, 110, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Form)
        self.commandLinkButton.setGeometry(QtCore.QRect(160, 130, 185, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", "..."))
        self.commandLinkButton.setText(_translate("Form", "CommandLinkButton"))

