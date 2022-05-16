# -*- coding: utf-8 -*-
import webbrowser
import sys
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from PyQt5 import QtCore

from PyQt5.QtCore import Qt

from PyQt5.QtMultimedia import *

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

from PyQt5 import QtWidgets, QtCore

class dummy(QWidget):
    def __init__(self, parent):
        super(dummy, self).__init__(parent)
        self.butt = QPushButton(text="Bla")
        self.vid = QVideoWidget(self)
        # self.vid.setVisible(True)

        #  self.butt.show()
        layout = QHBoxLayout()
        layout.addWidget(self.butt)
        self.setLayout(layout)
        

class VideoPlayer(QWidget):
    def __init__(self, video_path="Dog.mp4", parent=None):
        super(VideoPlayer, self).__init__(parent=parent)

        # QMediaPlayer
        self.mediaPlayer = QMediaPlayer(parent, QMediaPlayer.VideoSurface)
        self.mediaPlayer.error.connect(self.er)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(video_path)))

        self.mediaPlayer.mediaStatusChanged.connect(self.status_changed)

        # Set widget
        self.videoWidget = QVideoWidget(parent)
        self.videoWidget.setGeometry(self.pos().x(), self.pos().y(), self.width(), self.height())

        layout = QHBoxLayout()
        layout.addWidget(self.videoWidget)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.setLayout(layout)
        # Play
        self.mediaPlayer.play()
        print(self.videoWidget.isVisible())


    def status_changed(self,st):
        if st == self.mediaPlayer.EndOfMedia: # Loop video
            self.mediaPlayer.play()

    def er(self,error):
        if error == QMediaPlayer.ResourceError or error == QMediaPlayer.FormatError:
            reply = QtWidgets.QMessageBox.question(self, 'Unsuported file format', "The available codec is only able to play '.avi' video format. You can install a new codec in order to play '.mp4' videos.\n\n Do you want to install a new codec?")
            # reply
            href = "<a href = 'http://www.codecguide.com/download_k-lite_codec_pack_standard.htm' > Codec < /a >"

            if reply == QMessageBox.Yes:
                webbrowser.open(
                    'http://www.codecguide.com/download_k-lite_codec_pack_standard.htm')
            elif reply == QMessageBox.No:
                self.close()

