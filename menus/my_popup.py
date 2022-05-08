from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent


class my_popup(QWidget):
    def __init__(self, parent=None):
        super(my_popup, self).__init__(parent)
        self.block_close = False

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.installEventFilter(self)

    def setup_popup(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.installEventFilter(self)

    def eventFilter(self, object, event):
        if not self.block_close:
            if event.type() == QEvent.WindowDeactivate:  
                self.close()
        # else:
        #     print("blocked!")
        # if event.type() == QEvent.MouseButtonPress:
        #     print("asdas")
        return False
    


