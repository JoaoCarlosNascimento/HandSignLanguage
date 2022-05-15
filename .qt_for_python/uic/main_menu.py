# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\SRI\HandSignLanguage\menus\main_menu\main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(785, 590)
        self.pb_read = QtWidgets.QPushButton(Form)
        self.pb_read.setGeometry(QtCore.QRect(310, 320, 161, 81))
        self.pb_read.setObjectName("pb_read")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 420, 161, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 420, 161, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 70, 431, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../imagens_menus/imagem_junta_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 381, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../imagens_menus/titulo_png.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb_read.setText(_translate("Form", "Read"))
        self.pushButton_2.setText(_translate("Form", "Exit"))
        self.pushButton_3.setText(_translate("Form", "Help"))

