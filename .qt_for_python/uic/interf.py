# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\SRI\HandSignLanguage\pyqt examples\interf.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.prev_btn = QtWidgets.QPushButton(self.centralwidget)
        self.prev_btn.setGeometry(QtCore.QRect(0, 260, 75, 23))
        self.prev_btn.setObjectName("prev_btn")
        self.next_btn = QtWidgets.QPushButton(self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(710, 260, 75, 23))
        self.next_btn.setObjectName("next_btn")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 30, 601, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lb_1.setMouseTracking(True)
        self.lb_1.setFrameShape(QtWidgets.QFrame.Box)
        self.lb_1.setObjectName("lb_1")
        self.horizontalLayout.addWidget(self.lb_1)
        self.lb_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lb_2.setMouseTracking(True)
        self.lb_2.setFrameShape(QtWidgets.QFrame.Box)
        self.lb_2.setObjectName("lb_2")
        self.horizontalLayout.addWidget(self.lb_2)
        self.lb_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lb_3.setMouseTracking(True)
        self.lb_3.setFrameShape(QtWidgets.QFrame.Box)
        self.lb_3.setObjectName("lb_3")
        self.horizontalLayout.addWidget(self.lb_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.prev_btn.setText(_translate("MainWindow", "Previous"))
        self.next_btn.setText(_translate("MainWindow", "Next"))
        self.lb_1.setText(_translate("MainWindow", "TextLabel"))
        self.lb_2.setText(_translate("MainWindow", "TextLabel"))
        self.lb_3.setText(_translate("MainWindow", "TextLabel"))

