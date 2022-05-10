from PyQt5.QtWidgets import QWidget
from PyQt5 import  uic
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtGui import QPixmap



from menus.my_popup import my_popup


class word_popup(my_popup):
    def __init__(self, parent=None):
        super(word_popup, self).__init__(parent)
        uic.loadUi('menus/words_menu/word_popup.ui', self)
        
        self.toolButton.clicked.connect(
            self.select_file_diag
        )
    
    def select_file_diag(self):
        self.block_close = True
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', 'c:\\', "Image files (*.jpg *.gif)")
        self.label.setPixmap(QPixmap(fname[0]))

        self.block_close = False

    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter("Text files (*.txt)")
        filenames = []

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                self.contents.setText(data)

