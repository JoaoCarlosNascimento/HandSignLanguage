from PyQt5.QtWidgets import QWidget, QListWidgetItem, QFileDialog, QTabWidget
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from menus.my_menus import my_menus
from menus.read_menu.read_menu_contents import read_menu_contents
class read_menu(my_menus):
    def __init__(self, parent=None, book_id=0):
        super(read_menu, self).__init__(parent)
        uic.loadUi('menus/read_menu/read_menu.ui', self)
        self.objectName = "menu_read"
        self.book_id = 0
        self.image = None
        self.text = None
    def load(self, book_id):
        self.clear()
        db = self.parent().parent().parent().db
        book_info = db.get_books(book_id)
        self.text = book_info[0][1]
        self.image = book_info[0][2]
        self.page = 0

        self.book_id = book_id

        self.display(db)
    def display(self, db):
        pages = db.get_pages(self.book_id)
        for n, p in enumerate(pages):
            self.body.addTab(read_menu_contents(self.parent(), p[0]), "Page" + str(n + 1))
    def clear(self):
        # self.text.clear()
        self.body.clear()

    def select_file_diag(self):
        self.block_close = True
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', 'c:\\', "Image files (*.jpg *.gif)")

        self.image_path = fname[0]
        img = QPixmap(self.image_path)
        self.preview.setPixmap(img)
        
        self.block_close = False