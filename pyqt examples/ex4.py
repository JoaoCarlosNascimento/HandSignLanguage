import sys
from turtle import pos
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys

class MainClass(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainClass, self).__init__(parent)
        self.setParent(parent)
        self.setModal(True)
        #widgets added below
