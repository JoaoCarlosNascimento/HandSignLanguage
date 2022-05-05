from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5 import uic

from menus.words_menu import words_item_widget

class words_menu(QWidget):
    def __init__(self, parent=None):
        super(words_menu, self).__init__(parent)
        uic.loadUi('menus/words_menu/words_menu.ui', self)
        self.objectName = "menu_words"

        self.words_list = []

    def init_words_page(self, text):
        self.listWidget.clear()
        clean_text = text.replace('\n', ' ')
        words_list = clean_text.split(' ')
        self.words_list = words_menu.remove_duplicates(words_list)
        for i in range(len(self.words_list)):
            item = QListWidgetItem(self.listWidget)
            item_widget = words_item_widget.words_item_widget(
                self.words_list[i], func=self.remove_word)
            item.setSizeHint(item_widget.frame_2.size())

            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item_widget)

    def remove_word(self,obj,text):
        
        for idx in range(self.listWidget.__len__()):
            if self.listWidget.itemWidget(self.listWidget.item(idx)).le_word.text() == text:
                self.listWidget.takeItem(idx)
                self.words_list = [item for item in self.words_list if item != text]
                break
        # self.words_list = [item for item in self.words_list if item != text]


        print(self.words_list)

    def remove_duplicates(text):
        return list(dict.fromkeys(text))
