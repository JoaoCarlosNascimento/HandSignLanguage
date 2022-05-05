from PyQt5.QtWidgets import QWidget
from PyQt5 import  uic
from PyQt5.QtCore import QEvent

from menus.my_popup import my_popup


class word_popup(my_popup):
    def __init__(self, parent=None):
        super(word_popup, self).__init__(parent)
        uic.loadUi('menus/words_menu/word_popup.ui', self)
