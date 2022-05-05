#!/usr/bin/python

import sys
from turtle import pos
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5
import sys

# class Example(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):



#         QToolTip.setFont(QFont('SansSerif', 10))

#         self.setToolTip('This is a <b>QWidget</b> widget')

#         btn = QPushButton('Button', self)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.resize(btn.sizeHint())
#         btn.move(50, 50)

#         self.setGeometry(300, 300, 300, 200)
#         self.setWindowTitle('Tooltips')
#         self.show()


# def main():

#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     main()


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        # Call the inherited classes __init__ method
        super(Ui, self).__init__()
        uic.loadUi('interf.ui', self)  # Load the .ui file

        QToolTip.setFont(QFont('SansSerif', 10))
        # self.setToolTip('This is a <b>QWidget</b> widget')
        # self.lb_1
        lb_1 = self.findChild(QtWidgets.QLabel, 'lb_1')  # Find the button

        # lb_1.mouseMoveEvent = self.mouseMoveEvent
        QtWidgets.QLabel.mousePressEvent = self.moPe




        self.show()  # Show the GUI
    # def mouseMoveEvent(self, event):
    #     print(event)
    #     # print("sadas")
    #     self.squareSize = 20
    #     self.columns = 3
    #     widgetPosition = self.mapFromGlobal(event.globalPos())
    #     key = (widgetPosition.y() // self.squareSize) * self.columns + widgetPosition.x() // self.squareSize

        
    #     text = "bla"
    #     #  QtCore.QString.fromLatin1("<p>Character: <span style=\"font-size: 24pt; font-family: %1\">").arg(self.displayFont.family()) + \
    #     #         QtCore.QChar(key) + \
    #     #         QtCore.QString.fromLatin1("</span><p>Value: 0x") + \
    #     #         QtCore.QString.number(key, 16)
    #     QToolTip.showText(event.globalPos(), text, self)
    def moPe(self,e):
        self.diag = uic.loadUi('dWi.ui')
        # self.diag.setModal(True)
        self.diag.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.diag.installEventFilter(self)
        self.diag.show()

    def eventFilter(self, object, event):
        # print("asdasd")
        # QEvent.WindowDeactivate
        if event.type() == QEvent.WindowDeactivate:#QEvent.FocusOut:
            # QtGui.
            print("out")
            self.diag.close()
        if event.type() == QEvent.MouseButtonPress:
            print("asdas")
            pass
        # if event.type() == QEvent.Enter:
        #     print("Mouse is over the label")
        #     self.stop = True
        #     print('program stop is', self.stop)
        #     return True
        # elif event.type() == QEvent.Leave:
        #     print("Mouse is not over the label")
        #     self.stop = False
        #     print('program stop is', self.stop)
        return False


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
