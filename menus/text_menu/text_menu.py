from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5 import uic

# from menus import my_menus


class text_menu(QWidget):
    def __init__(self, parent=None):
        super(text_menu, self).__init__(parent)
        uic.loadUi('menus/text_menu/text_menu.ui', self)
        self.objectName = "menu_text"