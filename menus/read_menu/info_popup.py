
from menus.my_popup import my_popup
from PyQt5 import uic

class info_popup(my_popup):
    def __init__(self, word, parent = None):
        super().__init__(parent)
        uic.loadUi('menus/read_menu/info_popup.ui', self)
        self.word.setText(word)
    def set(self):
        # db = self.parent().parent().parent().db
        # info = db.get_word(self.word)
        # self.word = 
        pass