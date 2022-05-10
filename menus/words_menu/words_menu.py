from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5 import uic

from menus.my_menus import my_menus
from menus.words_menu.words_item_widget import words_item_widget
from menus.create_menu.create_popup import create_popup


class words_menu(my_menus):
    def __init__(self, parent=None):
        super(words_menu, self).__init__(parent)
        uic.loadUi('menus/words_menu/words_menu.ui', self)
        self.objectName = "menu_words"

        self.words_list = []
        self.full_text = ""
        self.bt_next.clicked.connect(
            lambda: self.submit_page())
        self.popup = None

    def init_page(self):
        self.listWidget.clear()
    
    def initialize_list(self,text, img_path):
        self.image_path = img_path
        self.full_text = text

        clean_text = text.replace('\n', ' ')
        words_list = clean_text.split(' ')
        self.words_list = words_menu.remove_duplicates(words_list)
        # print(self.words_list)
        for i in range(len(self.words_list)):
            item = QListWidgetItem(self.listWidget)
            item_widget = words_item_widget(
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

    def new_page_popup(self, func=None,init_text = None):
        db = self.parent().parent().parent().db

        book_id = db.get_id("BOOK")
        page = db.new_page(book_id, self.image_path)
        db.new_page_text(self.full_text, self.full_text, page)
        
        self.popup = create_popup()

        self.popup.bt_np.clicked.connect(
            lambda: self.new_page(func, init_text))

        self.popup.bt_sc.clicked.connect(lambda: self.save_close(func))

        self.popup.show()
    def new_page(self, func, init_text):
        init_text()
        func("menu_text")
        self.popup.close()

    def submit_page(self):
        print("Submit page")
        # db = self.parent().parent().parent().db
        # for item in self.listWidget:
            

    def save_close(self, func):
        print("Finish transaction")
        db = self.parent().parent().parent().db
        db.commit()
        self.popup.close()
        func("menu_books")
