# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\SRI\HandSignLanguage\menus\books_menu\books_item_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(175, 270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.book_cover = QtWidgets.QLabel(Form)
        self.book_cover.setGeometry(QtCore.QRect(0, 0, 175, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.book_cover.sizePolicy().hasHeightForWidth())
        self.book_cover.setSizePolicy(sizePolicy)
        self.book_cover.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.book_cover.setText("")
        self.book_cover.setPixmap(QtGui.QPixmap("../imagens_menus/plus_sign.png"))
        self.book_cover.setScaledContents(True)
        self.book_cover.setObjectName("book_cover")
        self.book_name = QtWidgets.QLabel(Form)
        self.book_name.setGeometry(QtCore.QRect(0, 200, 175, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.book_name.sizePolicy().hasHeightForWidth())
        self.book_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.book_name.setFont(font)
        self.book_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.book_name.setAutoFillBackground(False)
        self.book_name.setAlignment(QtCore.Qt.AlignCenter)
        self.book_name.setWordWrap(True)
        self.book_name.setObjectName("book_name")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.book_name.setText(_translate("Form", "Add New Book"))

