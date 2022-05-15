from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from menus.words_menu.word_popup import word_popup

from PyQt5.QtWidgets import QFileDialog

class words_item_widget(QWidget):
    def __init__(self, text, parent=None, func=None):
        super(words_item_widget, self).__init__(parent)
        uic.loadUi('menus/words_menu/words_item_widget.ui', self)
        self.func = func
        self.le_word.setText(text)
        self.pb_config.clicked.connect(self.press_word_popup)
        self.bt_delete.clicked.connect(self.auto_delete)
        self.word_file_name = None

    def press_word_popup(self, e):
        self.block_close = True
        self.fname = QFileDialog.getOpenFileName(
            self, 'Open file', 'c:\\', "Video files (*.avi *.mp4)")

        self.word_file_name = self.fname[0]

    def auto_delete(self):
        if self.func != None:
            self.func(self,self.le_word.text())





