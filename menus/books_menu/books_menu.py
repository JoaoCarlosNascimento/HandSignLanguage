from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5 import uic

from menus.my_menus import my_menus
from menus.books_menu.books_item_widget import books_item_widget

class books_menu(my_menus):
    def __init__(self, parent=None, func=None):
        super(books_menu, self).__init__(parent)
        uic.loadUi('menus/books_menu/books_menu.ui', self)
        self.objectName = "menu_books"

        if func != None:
            self.changePage = func

        self.listWidget.setSpacing(15)

        self.listWidget.itemClicked.connect(self.item_clicked)

        # self.init_page()


    def item_clicked(self,obj):
        if self.listWidget.itemWidget(self.listWidget.item(
                self.listWidget.indexFromItem(obj).row())).objectName == "CreateBook":

            self.changePage()

            print("New Book")
        else:
            print("Open Book")
            book_name = self.listWidget.itemWidget(self.listWidget.item(
                self.listWidget.indexFromItem(obj).row())).book_name.text()

            print(book_name)

    def init_page(self):
        # Load da base de dados
        self.listWidget.clear()

        # Inicializar os livros
        for i in range(1):
            item = QListWidgetItem(self.listWidget)
            item_widget = books_item_widget()
            item.setSizeHint(item_widget.size())

            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item_widget)

        # Livro de criacao
        item = QListWidgetItem(self.listWidget)
        item_widget = books_item_widget()
        item_widget.objectName = "CreateBook"
        item.setSizeHint(item_widget.size())

        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, item_widget)


        


