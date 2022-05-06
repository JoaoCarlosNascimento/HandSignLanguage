from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(Ui, self).__init__()
        uic.loadUi('untitled.ui', self)  # Load the .ui file

        self.button = self.findChild(QtWidgets.QPushButton, 'banana')  # Find the button
        # Remember to pass the definition/method, not the return value!
        self.button.clicked.connect(self.printButtonPressed)

        self.list = self.findChild(QtWidgets.QListWidget, 'listWidget')

        # QtWidgets.QListWidgetItem(self.list, "bla")
        # QtWidgets.QListWidget.addItem("asdas")

        # QtWidgets.QLabel.mouseMoveEvent = 
        self.lab = self.findChild(QtWidgets.QLabel, 'label')  # Find the button

        self.lab.mouseMoveEvent = self.lab_fun

        # lab_fun



        self.show()  # Show the GUI

    def printButtonPressed(self):
        # This is executed when the button is pressed
        self.list.addItem("banana")
        print('banana')

    def lab_fun(self,pos):
        print(pos)
        pass



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
