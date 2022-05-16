from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

# from menus.words_menu.word_popup import word_popup

class books_item_widget(QWidget):
    def __init__(self, parent=None, func=None):
        super(books_item_widget, self).__init__(parent)
        uic.loadUi('menus/books_menu/books_item_widget.ui', self)

        self.objectName = "book_icon"
        # self.func = func
        # self.le_word.setText(text)
        # self.pb_config.clicked.connect(self.press_word_popup)
        # self.bt_delete.clicked.connect(self.auto_delete)



