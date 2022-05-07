from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication

from menus.books_menu.books_menu import books_menu
from menus.words_menu.words_menu import words_menu
from menus.text_menu.text_menu import text_menu

from menus.main_menu.main_menu import main_menu

from menus.create_menu.create_menu import create_menu

menus = []

from lib.database import database
def add_menu(stck,name,ptr):
    menus.append({"name": name, "idx": stck.indexOf(ptr), "ptr": ptr})
    # print(name+" idx "+str(stck.indexOf(ptr)))

def find_menu(name):
    return [item for item in menus if item['name'] == name][0]



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('base.ui', self)

        self.books_page_config()
        self.main_page_config()

        self.create_page_config()
        self.text_page_config()
        self.words_page_config()

        self.change_page("menu_create")

        self.show()  # Show the GUI

        self.db = database()

    def change_page(self, name, func = None):
        find_menu(name)['ptr'].init_page()
        if func != None:
            func()
        self.stackedWidget.setCurrentIndex(find_menu(name)['idx'])

    def text_page_config(self):
        widget = text_menu(self.stackedWidget)
        self.stackedWidget.addWidget(widget)
        add_menu(self.stackedWidget, "menu_text",widget)
        
        # bt_next
        widget.bt_next.clicked.connect(lambda: self.change_page(
            "menu_words",
            lambda: find_menu("menu_words")['ptr'].initialize_list(
                widget.plainTextEdit.toPlainText()
                )
            )
        )

    def words_page_config(self):
        widget = words_menu(self.stackedWidget)
        self.stackedWidget.addWidget(widget)
        add_menu(self.stackedWidget, "menu_words",widget)

        # bt_prev
        widget.bt_prev.clicked.connect(lambda: self.change_page("menu_text"))

        widget.bt_next.clicked.connect(lambda:
            widget.new_page_popup(
                self.change_page, find_menu("menu_text")['ptr'].clear_text
            )
        )

    def books_page_config(self):
        widget = books_menu(self.stackedWidget, lambda: self.change_page(
            "menu_create", find_menu("menu_text")['ptr'].clear_text))
        self.stackedWidget.addWidget(widget)
        add_menu(self.stackedWidget, "menu_books", widget)

        widget.pb_back.clicked.connect(lambda: self.change_page("menu_main"))

    def main_page_config(self):
        widget = main_menu(self.stackedWidget)
        self.stackedWidget.addWidget(widget)
        add_menu(self.stackedWidget, "menu_main", widget)

        widget.pb_read.clicked.connect(lambda: self.change_page("menu_books"))

    def create_page_config(self):
        widget = create_menu(self.stackedWidget,)
        self.stackedWidget.addWidget(widget)
        add_menu(self.stackedWidget, "menu_create", widget)



        widget.pb_back.clicked.connect(lambda: self.change_page("menu_books"))
        
        widget.pb_np.clicked.connect(lambda: 
            find_menu("menu_create")['ptr'].submit(
                self.change_page("menu_text")
            )
        )




app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
window.db.connection.close()