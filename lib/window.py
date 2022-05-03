from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reading is fun!")