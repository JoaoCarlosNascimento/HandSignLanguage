from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

# from menus.create_menu.create_item_widget import books_item_widget
from menus.my_menus import my_menus
from PyQt5.QtWidgets import QFileDialog

class create_menu(my_menus):
    def __init__(self, parent=None, func = None):
        super(create_menu, self).__init__(parent)
        uic.loadUi('menus/create_menu/create_menu.ui', self)
        self.objectName = "menu_create"

        self.changePage = func
        self.image_path = None
        self.pb_upload.clicked.connect(
            self.select_file_diag
        )
    def init_page(self):
        self.book_title.clear()
        self.preview.clear()

    def submit(self,func = None):
        print("Submit Title")
        db = self.parent().parent().parent().db
        # if self.image_path 
        db.new_book(name = self.book_title.text(), img_path= self.image_path)
        
        if func != None:
            func()
        
    def select_file_diag(self):
        self.block_close = True
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', 'c:\\', "Image files (*.jpg *.gif)")

        self.image_path = fname[0]
        img = QPixmap(self.image_path)
        self.preview.setPixmap(img)
        
        self.block_close = False

    # def getfiles(self):
    #     dlg = QFileDialog()
    #     dlg.setFileMode(QFileDialog.AnyFile)
    #     dlg.setFilter("Text files (*.txt)")
    #     filenames = []

    #     if dlg.exec_():
    #         filenames = dlg.selectedFiles()
    #         f = open(filenames[0], 'r')

    #         with f:
    #             data = f.read()
    #             self.contents.setText(data)


        


