
from menus.my_popup import my_popup
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

class info_popup(my_popup):
    def __init__(self, word, parent = None):
        super().__init__()
        uic.loadUi('menus/read_menu/info_popup.ui', self)
        self.word.setText(word)
        self.parent = parent
        self.set()
        
    def set(self):
        db = self.parent.parent().parent().parent().parent().parent().parent().db
        info = db.get_word(self.word.text())
        if len(info)>0:
            fig = info[2]
            img = QPixmap()
            img.loadFromData(fig)
            self.img.setPixmap (img)