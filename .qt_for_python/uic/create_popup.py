# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\SRI\HandSignLanguage\menus\create_menu\create_popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(400, 300)
        Form.setStyleSheet("")
        self.bt_sc = QtWidgets.QPushButton(Form)
        self.bt_sc.setGeometry(QtCore.QRect(30, 180, 111, 31))
        self.bt_sc.setObjectName("bt_sc")
        self.bt_np = QtWidgets.QPushButton(Form)
        self.bt_np.setGeometry(QtCore.QRect(270, 190, 75, 23))
        self.bt_np.setObjectName("bt_np")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 100, 221, 61))
        self.label.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.number_of_pages = QtWidgets.QLabel(Form)
        self.number_of_pages.setGeometry(QtCore.QRect(200, 110, 51, 41))
        self.number_of_pages.setObjectName("number_of_pages")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bt_sc.setText(_translate("Form", "Save and Close"))
        self.bt_np.setText(_translate("Form", "New Page"))
        self.label.setText(_translate("Form", "Number of pages:"))
        self.number_of_pages.setText(_translate("Form", "0"))

