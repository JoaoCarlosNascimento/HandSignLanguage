from menus.my_popup import my_popup
from PyQt5 import uic
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtGui import QPixmap

from menus.my_popup import my_popup


class help_menu(my_popup):
    def __init__(self, parent=None):
        super(help_menu, self).__init__(parent)
        uic.loadUi('menus/help_menu/help_menu.ui', self)
        self.objectName = "menu_help"
        self.block_close = True