# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\SRI\HandSignLanguage\pyqt examples\custom_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 158)
        Form.setMinimumSize(QtCore.QSize(650, 0))
        Form.setMaximumSize(QtCore.QSize(650, 16777215))
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 530, 90))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(340, 30, 10, 30))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.le_word = QtWidgets.QLineEdit(self.frame_2)
        self.le_word.setGeometry(QtCore.QRect(40, 30, 300, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_word.sizePolicy().hasHeightForWidth())
        self.le_word.setSizePolicy(sizePolicy)
        self.le_word.setStyleSheet("")
        self.le_word.setObjectName("le_word")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(30, 30, 10, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(10, 16777215))
        self.frame.setStyleSheet("background-color: rgb(255, 0, 4);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pb_config = QtWidgets.QPushButton(self.frame_2)
        self.pb_config.setGeometry(QtCore.QRect(350, 30, 75, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_config.sizePolicy().hasHeightForWidth())
        self.pb_config.setSizePolicy(sizePolicy)
        self.pb_config.setObjectName("pb_config")
        self.pb_connect = QtWidgets.QPushButton(self.frame_2)
        self.pb_connect.setGeometry(QtCore.QRect(425, 30, 75, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_connect.sizePolicy().hasHeightForWidth())
        self.pb_connect.setSizePolicy(sizePolicy)
        self.pb_connect.setObjectName("pb_connect")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb_config.setText(_translate("Form", "..."))
        self.pb_connect.setText(_translate("Form", "Connect"))

