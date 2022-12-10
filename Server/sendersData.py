from threading import Thread
import socket as socketNetwork
from PyQt5.QtCore import QObject, pyqtSignal

import sys

import cv2

from Client import typeClient

from processingImages import processingImage

class senderVideo(QObject, Thread):

    def __init__(self, clientCamera, clientGuard):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__clientCamera = clientCamera
        self.__clientGuard = clientGuard

        self.__clientCamera.updateImage.connect(self.sendImageGuard)
        self.__clientGuard.getNewImageSignal.connect(self.acceptNewImage)

        # запросить изображение с камеры
        self.acceptNewImage()

    def sendImageGuard(self):
        outImage = self.__clientCamera.getCurrentImage()

        outImage = outImage.reshape((-1,))

        self.__clientGuard.send(outImage)

    def acceptNewImage(self):
        self.__clientCamera.requestImage()

