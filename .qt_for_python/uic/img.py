# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\SRI\HandSignLanguage\qt_tests\img.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(400, 300)
        self.graphicsView = QtWidgets.QGraphicsView(Frame)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))

