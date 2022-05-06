from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, uic, QtGui, QtCore
import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication


class Words_Item_Widget(QWidget):
    def __init__(self, parent=None):
        super(Words_Item_Widget, self).__init__(parent)
        uic.loadUi('custom_widget.ui', self)



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)  # Load the .ui file

        self.text_page_config()
        self.words_page_config()

        # self.custom_widget
        # self.it_ex
        # QtWidgets.QListWidgetItem.
        # QtWidgets.QListWidget.addItem()
    

        self.show()  # Show the GUI

    def text_page_config(self):
        self.tp_next.clicked.connect(
            lambda: self.st_nav_button(self.tp_next))

    def words_page_config(self):
        self.wp_next.clicked.connect(
            lambda: self.st_nav_button(self.wp_next))
        self.wp_prev.clicked.connect(
            lambda: self.st_nav_button(self.wp_prev))
        
    def st_nav_button(self,btn):
        print("Current Stack: "+str(self.stackedWidget.currentIndex.__call__()))
        if(self.stackedWidget.currentIndex.__call__() == 0):  # text_page
            if(btn.objectName.__call__() == 'tp_next'):
                self.init_words_page("sadas")
                self.stackedWidget.setCurrentIndex(1)
        elif(self.stackedWidget.currentIndex.__call__() == 1): #words_page
            if(btn.objectName.__call__() == 'wp_next'):
                pass
            elif(btn.objectName.__call__() == 'wp_prev'): 
                self.stackedWidget.setCurrentIndex(0)

    def init_words_page(self,text):
        self.listWidget.clear()
        for i in range(3):
            print(self.listWidget)
            item = QListWidgetItem(self.listWidget)
            item_widget = Words_Item_Widget()
            print(item_widget.frame_2.size())
            item.setSizeHint(item_widget.frame_2.size())

            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item,item_widget)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
