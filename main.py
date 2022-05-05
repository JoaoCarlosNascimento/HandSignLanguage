from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication

from menus.words_menu.words_menu import words_menu
from menus.text_menu.text_menu import text_menu

menus = []

def add_menu(stck,name,ptr):
    menus.append({"name": name, "idx": stck.indexOf(ptr), "ptr": ptr})
    print(name+" idx "+str(stck.indexOf(ptr)))

def find_menu(name):
    return [item for item in menus if item['name'] == name][0]



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('menus/main.ui', self)

        self.text_page_config()
        self.words_page_config()

        self.stackedWidget.setCurrentIndex(find_menu("menu_text")['idx'])
        self.show()  # Show the GUI

    def change_page(self, name, func = None):
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
            find_menu("menu_words")['ptr'].init_words_page(
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



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
