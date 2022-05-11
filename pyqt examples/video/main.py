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
class VideoWindow(QMainWindow):
    def __init__(self):
         super(VideoWindow, self).__init__()
         self.setWindowTitle('QMediaPlayer TEST')
         self.resize(640, 480)

         # QMediaPlayer
         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
         self.mediaPlayer.error.connect(self.er)
         self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('demo.mp4')))

         self.mediaPlayer.mediaStatusChanged.connect(self.status_changed)

         # Set widget
         self.videoWidget = QVideoWidget()
         self.videoWidget.setGeometry(self.pos().x(), self.pos().y(), self.width(), self.height())
         self.setCentralWidget(self.videoWidget)
         self.mediaPlayer.setVideoOutput(self.videoWidget)


         # Play
         self.mediaPlayer.play()

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

if __name__ == '__main__':
     app = QApplication([])
     window = VideoWindow()
     window.show()
     sys.exit(app.exec_())
