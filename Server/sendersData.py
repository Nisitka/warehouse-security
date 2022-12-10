from threading import Thread
import socket as socketNetwork
from PyQt5.QtCore import QObject, pyqtSignal

import sys

import cv2

from Client import typeClient

from processingImages import processingImage

class senderVideo(QObject):

    def __init__(self, clientCamera, clientGuard):
        QObject.__init__(self)

        self.__clientCamera = clientCamera
        self.__clientGuard = clientGuard

        self.__clientCamera.updateImage.connect(self.sendImageGuard)
        self.__clientGuard.getNewImageSignal.connect(self.acceptNewImage)

    def run(self):
        # запросить изображение с камеры
        self.acceptNewImage()

    def sendImageGuard(self):
        # берем изображение с клиента-камеры и обрабатываем нейро-ми сетями
        outImage = processingImage(self.__clientCamera.getCurrentImage())

        # перевод в список numpy
        outImage = outImage.reshape((-1,))

        # отправка данных
        self.__clientGuard.send(outImage)

    # принять новое изображение от камеры
    def acceptNewImage(self):
        self.__clientCamera.requestImage()

