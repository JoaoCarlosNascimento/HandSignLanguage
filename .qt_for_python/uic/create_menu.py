# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\SRI\HandSignLanguage\menus\create_menu\create_menu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(581, 411)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(581, 411))
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 330, 561, 71))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pb_upload = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pb_upload.setObjectName("pb_upload")
        self.horizontalLayout_8.addWidget(self.pb_upload)
        self.pb_back = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pb_back.setObjectName("pb_back")
        self.horizontalLayout_8.addWidget(self.pb_back)
        self.preview = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.preview.setFrameShadow(QtWidgets.QFrame.Plain)
        self.preview.setScaledContents(True)
        self.preview.setObjectName("preview")
        self.horizontalLayout_8.addWidget(self.preview)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.pb_np = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pb_np.setObjectName("pb_np")
        self.horizontalLayout_8.addWidget(self.pb_np)
        self.book_title = QtWidgets.QLineEdit(Form)
        self.book_title.setGeometry(QtCore.QRect(170, 170, 223, 20))
        self.book_title.setObjectName("book_title")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb_upload.setText(_translate("Form", "Upload cover image"))
        self.pb_back.setText(_translate("Form", "Cancel"))
        self.preview.setText(_translate("Form", "TextLabel"))
        self.pb_np.setText(_translate("Form", "Next"))
        self.book_title.setPlaceholderText(_translate("Form", "Book Title"))

