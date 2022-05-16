from menus.my_popup import my_popup
from PyQt5 import uic
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QFileDialog

from PyQt5 import QtCore

from PyQt5.QtGui import QPixmap

from menus.my_popup import my_popup


class help_menu(my_popup):
    def __init__(self, parent=None):
        super(help_menu, self).__init__()
        uic.loadUi('menus/help_menu/help_menu.ui', self)
        self.parent = parent

        self.installEventFilter(self)

        # self.setWindowFlags(QtCore.Qt.Popup)

        self.in_pop = True
        # self.block_close
        # self.objectName = "menu_help"
        # self.block_close = False



    def eventFilter(self, object, event):
        if event.type() == QEvent.Enter:
            print("Mouse is over the label")
            self.stop = True
            print('program stop is', self.stop)
            return True
        elif event.type() == QEvent.Leave:
            print("Mouse is not over the label")
            self.stop = False
            print('program stop is', self.stop)
        return False

    def eventFilter(self, object, event):
        # if event.type() == QEvent.Enter:
        #     self.in_pop = True
        #     print("IN")
        # elif event.type() == QEvent.Leave:
        #     self.in_pop = False
        #     print("OUT")
        # if event.type() == QEvent.FocusOut:
        #     print("FOC")
        if event.type() == 3:
            self.close()
        # print(event.type())
        #     # self.close()
        return False