from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5 import uic

from menus.words_menu import Words_Item_Widget

from menus.words_menu.word_popup import word_popup

class words_menu(QWidget):
    def __init__(self, parent=None):
        super(words_menu, self).__init__(parent)
        uic.loadUi('menus/words_menu/words_menu.ui', self)
        self.objectName = "menu_words"

    def init_words_page(self, text):
        self.listWidget.clear()
        clean_text = text.replace('\n', ' ')
        words_list = clean_text.split(' ')
        no_dup = words_menu.remove_duplicates(words_list)
        # print(text.split(' '))
        for i in range(len(no_dup)):
            item = QListWidgetItem(self.listWidget)
            item_widget = Words_Item_Widget.Words_Item_Widget()
            item_widget.le_word.setText(no_dup[i])
            item_widget.mousePressEvent = self.press_word_popup
            # print(item_widget.frame_2.size())
            item.setSizeHint(item_widget.frame_2.size())

            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item_widget)

    def press_word_popup(self,e):
        self.popup = word_popup()
        self.popup.setup_popup()

        print("press")
        self.popup.show()

    def remove_duplicates(text):
        return list(dict.fromkeys(text))
