from PyQt5.QtWidgets import QWidget, QListWidgetItem, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from menus.my_menus import my_menus
class text_menu(my_menus):
    def __init__(self, parent=None):
        super(text_menu, self).__init__(parent)
        uic.loadUi('menus/text_menu/text_menu.ui', self)
        self.objectName = "menu_text"
        self.image_path = None
        self.upload.clicked.connect(
            self.select_file_diag
        )
    def clear_text(self):
        self.plainTextEdit.clear()
        self.preview.clear()

    def select_file_diag(self):
        self.block_close = True
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', 'c:\\', "Image files (*.jpg *.gif)")

        self.image_path = fname[0]
        img = QPixmap(self.image_path)
        self.preview.setPixmap(img)
        
        self.block_close = False