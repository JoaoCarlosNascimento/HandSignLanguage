from PyQt5.QtWidgets import QWidget
from PyQt5 import  uic
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtGui import QPixmap



from menus.my_popup import my_popup


class create_popup(my_popup):
    def __init__(self, parent=None):
        super(create_popup, self).__init__(parent)
        uic.loadUi('menus/create_menu/create_popup.ui', self)
        self.block_close = True
