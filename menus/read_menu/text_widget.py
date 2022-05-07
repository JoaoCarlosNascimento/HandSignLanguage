from PyQt5.QtWidgets import QWidget, QSizePolicy, QLabel
from PyQt5 import QtGui, QtCore
from PyQt5 import uic

class text_widget(QLabel):
    def __init__(self, text):
        super().__init__(text)

        self.setStyleSheet("font: 14pt; \
                            color: black;\
                            padding-right: 2px")
        self.adjustSize()
    # def popup(self):
