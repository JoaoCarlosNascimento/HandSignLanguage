from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5 import uic

# from menus.create_menu.create_item_widget import books_item_widget
from menus.my_menus import my_menus


class create_menu(my_menus):
    def __init__(self, parent=None, func = None):
        super(create_menu, self).__init__(parent)
        uic.loadUi('menus/create_menu/create_menu.ui', self)
        self.objectName = "menu_create"

        self.changePage = func

    def init_page(self):
        self.lineEdit.clear()


    def submit(self,func = None):
        print("Submit Title")


        if func != None:
            func()



        


