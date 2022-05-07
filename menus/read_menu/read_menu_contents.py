from PyQt5.QtWidgets import QWidget, QTabWidget, QListWidgetItem, QListWidget, QLabel
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

from menus.my_menus import my_menus
from menus.read_menu.text_widget import text_widget
from menus.read_menu.info_popup import info_popup
class read_menu_contents(my_menus):
    def __init__(self, parent=None, page_id = 1):
        super(read_menu_contents, self).__init__(parent)
        uic.loadUi('menus/read_menu/read_menu_contents.ui', self)
        self.page_id = page_id
        self.load()

        self.text.itemClicked.connect(
            self.item_clicked
        )
    def load(self):
        self.clear()
        db = self.parent().parent().parent().db
        contents = db.get_page_text(self.page_id)
        page = db.get_page(self.page_id)
        
        if len(page) > 0:
            img = QPixmap()
            img.loadFromData(page[0][2])
            self.image.setPixmap(img)
        
        phrase = contents[1].split(' ')
        for word in phrase:
            item = QListWidgetItem(self.text)
            self.text.addItem(item)

            item_widget = text_widget(word)
            item.setSizeHint(item_widget.size())

            self.text.setItemWidget(item, item_widget)
    def clear(self):
        self.text.clear()
        
    def item_clicked(self):
        sel = self.text.itemWidget(self.text.currentItem()).text()

        self.pp = info_popup(sel)
        self.pp.show()
