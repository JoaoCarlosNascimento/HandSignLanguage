
from menus.my_popup import my_popup
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from menus.read_menu.video_preview import VideoPlayer
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QPushButton
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl

from menus.read_menu.video_preview import VideoPlayer, dummy
class info_popup(my_popup):
    def __init__(self, word, parent = None):
        super().__init__()
        uic.loadUi('menus/read_menu/info_popup.ui', self)
        # self.word = QLabel()
        self.word.setText(word)
        self.parent = parent

        db = self.parent.parent().parent().parent().parent().parent().parent().db
        info = db.get_word(self.word.text().upper())
        # print(self.word.text())
        # print("Video: ")
        # print(info)
        if info != []:
            self.setMinimumSize(680, 420)
            if len(info) > 0:
                self.video = VideoPlayer(info[2], self)
                self.verticalLayout.addWidget(self.video)
        else:
            self.close()