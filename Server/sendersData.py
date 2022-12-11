from threading import Thread
import socket as socketNetwork
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap, QColor

import sys

import cv2

import pickle

from Client import typeClient

from processingImages import processingImage

from packerData import Packer

class senderVideo(QObject):

    def __init__(self, clientCamera, clientGuard):
        QObject.__init__(self)

        self.__clientCamera = clientCamera
        self.__clientGuard = clientGuard

        # связываем камеру и клиента
        self.__clientCamera.updateImage.connect(self.sendImageGuard)
        self.__clientGuard.getNewImageSignal.connect(self.acceptNewImage)

    def run(self):
        # запросить изображение с камеры
        self.acceptNewImage()

    def sendImageGuard(self):
        # берем изображение с клиента-камеры и обрабатываем нейро-ми сетями
        outImage = processingImage(self.__clientCamera.getCurrentImage())

        outBits = pickle.dumps(Packer("acceptShot", outImage))

        self.__clientGuard.send(outBits)
        print("send")

    # принять новое изображение от камеры
    def acceptNewImage(self):
        self.__clientCamera.requestImage()

