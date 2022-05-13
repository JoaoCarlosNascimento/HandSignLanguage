from PyQt5.QtWidgets import QWidget
from PyQt5 import  uic
from PyQt5.QtCore import QEvent, pyqtSignal
from PyQt5.QtWidgets import QFileDialog

from PyQt5.QtGui import QPixmap



from menus.my_popup import my_popup


class word_popup(my_popup):
    # closeEvent = pyqtSignal()
    def __init__(self, parent=None):
        super(word_popup, self).__init__()
        uic.loadUi('menus/words_menu/word_popup.ui', self)
        self.parent = parent
        self.toolButton.clicked.connect(
            self.select_file_diag
        )
        self.fname = None
    def select_file_diag(self):
        self.block_close = True
        self.fname = QFileDialog.getOpenFileName(
            self, 'Open file', 'c:\\', "Image files (*.jpg *.gif)")
        self.label.setPixmap(QPixmap(self.fname[0]))

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
                self.data_ = f.read()
                self.contents.setText(data_)    
    
    def send_data(self):
        self.parent.word_file_name = self.fname[0]
        print(self.parent.word_file_name)
    def eventFilter(self, object, event):
        if not self.block_close:
            if event.type() == QEvent.WindowDeactivate:
                self.send_data() 
                self.close()
        return False