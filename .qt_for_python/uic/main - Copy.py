# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\SRI\HandSignLanguage\menus\main - Copy.ui'
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
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 20, 721, 521))
        self.stackedWidget.setObjectName("stackedWidget")
        self.x1 = QtWidgets.QWidget()
        self.x1.setObjectName("x1")
        self.stackedWidget.addWidget(self.x1)
        self.x2 = QtWidgets.QWidget()
        self.x2.setObjectName("x2")
        self.wp_prev = QtWidgets.QPushButton(self.x2)
        self.wp_prev.setGeometry(QtCore.QRect(50, 460, 75, 23))
        self.wp_prev.setObjectName("wp_prev")
        self.wp_next = QtWidgets.QPushButton(self.x2)
        self.wp_next.setGeometry(QtCore.QRect(590, 460, 75, 23))
        self.wp_next.setObjectName("wp_next")
        self.listWidget = QtWidgets.QListWidget(self.x2)
        self.listWidget.setGeometry(QtCore.QRect(30, 30, 650, 401))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(650, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(650, 16777215))
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setObjectName("listWidget")
        self.stackedWidget.addWidget(self.x2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.wp_prev.setText(_translate("MainWindow", "prev"))
        self.wp_next.setText(_translate("MainWindow", "next"))
        self.listWidget.setSortingEnabled(False)

