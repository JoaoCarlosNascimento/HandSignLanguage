# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\SRI\HandSignLanguage\menus\text_menu\text_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(732, 590)
        self.bt_next = QtWidgets.QPushButton(Form)
        self.bt_next.setGeometry(QtCore.QRect(610, 460, 101, 41))
        self.bt_next.setObjectName("bt_next")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 701, 261))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.upload = QtWidgets.QPushButton(Form)
        self.upload.setGeometry(QtCore.QRect(270, 290, 181, 41))
        self.upload.setObjectName("upload")
        self.preview = QtWidgets.QLabel(Form)
        self.preview.setGeometry(QtCore.QRect(40, 300, 181, 141))
        self.preview.setScaledContents(True)
        self.preview.setObjectName("preview")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bt_next.setText(_translate("Form", "Next"))
        self.upload.setText(_translate("Form", "Upload illustration"))
        self.preview.setText(_translate("Form", "TextLabel"))

