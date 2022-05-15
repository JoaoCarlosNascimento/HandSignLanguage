from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5 import uic

from menus.my_menus import my_menus

class main_menu(my_menus):
    def __init__(self, parent=None, close_handler = None):
        super(main_menu, self).__init__(parent)
        uic.loadUi('menus/main_menu/main_menu.ui', self)
        self.objectName = "menu_main"

        self.pushButton_2.clicked.connect(lambda : close_handler())

