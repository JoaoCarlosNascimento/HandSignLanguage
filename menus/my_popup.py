from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent

from PyQt5 import uic


class my_popup(QWidget):
    def __init__(self, parent=None):
        super(my_popup, self).__init__(parent)
        # wid = uic.loadUi('menus/words_menu/word_popup.ui', self)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.installEventFilter(self)

    def setup_popup(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.installEventFilter(self)

    def eventFilter(self, object, event):
        # print(object)
        # print(event)
        # print("asdasd")
        # QEvent.WindowDeactivate
        if event.type() == QEvent.WindowDeactivate:  # QEvent.FocusOut:
            # QtGui.
            print("out")
            self.close()
        if event.type() == QEvent.MouseButtonPress:
            print("asdas")
            # pass
        return False
    


