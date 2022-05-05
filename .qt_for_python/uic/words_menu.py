# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\SRI\HandSignLanguage\menus\words_menu\words_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 486)
        self.bt_prev = QtWidgets.QPushButton(Form)
        self.bt_prev.setGeometry(QtCore.QRect(30, 450, 75, 23))
        self.bt_prev.setObjectName("bt_prev")
        self.bt_next = QtWidgets.QPushButton(Form)
        self.bt_next.setGeometry(QtCore.QRect(570, 450, 75, 23))
        self.bt_next.setObjectName("bt_next")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 650, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(650, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(650, 16777215))
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bt_prev.setText(_translate("Form", "prev"))
        self.bt_next.setText(_translate("Form", "next"))
        self.listWidget.setSortingEnabled(False)

