from PyQt5.QtWidgets import QLabel
# from PyQt5 import QtGui, QtCore
# from PyQt5 import uic
from menus.read_menu.info_popup import info_popup

class text_widget(QLabel):
    def __init__(self, text):
        super().__init__(text)

        self.setStyleSheet("font: 14pt; \
                            color: black;\
                            padding-right: 2px")
        self.adjustSize()