from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5 import uic

from menus.words_menu import Words_Item_Widget

class words_menu(QWidget):
    def __init__(self, parent=None):
        super(words_menu, self).__init__(parent)
        uic.loadUi('menus/words_menu/words_menu.ui', self)
        self.objectName = "menu_words"

    def init_words_page(self, text):
        self.listWidget.clear()
        for i in range(3):
            print(self.listWidget)
            item = QListWidgetItem(self.listWidget)
            item_widget = Words_Item_Widget.Words_Item_Widget()
            print(item_widget.frame_2.size())
            item.setSizeHint(item_widget.frame_2.size())

            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item_widget)
