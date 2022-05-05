from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class Words_Item_Widget(QWidget):
    def __init__(self, parent=None):
        super(Words_Item_Widget, self).__init__(parent)
        uic.loadUi('menus/words_menu/custom_widget.ui', self)

