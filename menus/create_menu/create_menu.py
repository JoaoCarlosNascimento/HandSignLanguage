from PyQt5.QtWidgets import QWidget, QListWidgetItem, QMessageBox
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
        name = self.book_title.text()
        if name == '' or name == ' ':
            msgBox = QMessageBox(self) 
            msgBox.setWindowTitle('Unvalid title')
            msgBox.setText("You have to add a title to continue.")
            msgBox.exec()
            msgBox.setModal(True)
            # reply = QMessageBox.question(self, 'Unvalid title', "You have to add a title to continue.")
            # # reply
            # href = "<a href = 'http://www.codecguide.com/download_k-lite_codec_pack_standard.htm' > Codec < /a >"

            # if reply == QMessageBox.Yes:
            #     webbrowser.open(
            #         'http://www.codecguide.com/download_k-lite_codec_pack_standard.htm')
            # elif reply == QMessageBox.No:
            #     self.close()
        else:
            db.new_book(name, img_path= self.image_path)
            
            if func != None:
                func("menu_text")
        
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


        


