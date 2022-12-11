from PyQt5.QtCore import QObject, pyqtSignal

from threading import Thread

import cv2
from PyQt5.QtGui import QImage, QPixmap, QColor

import time

import numpy

import socket
import codecs

import pickle

import sys

from packerData import Packer

class threadAcceptCommand(QObject, Thread):
    # сообщаем ядру о потери соединения
    disconnectServer = pyqtSignal()
    importVideo = pyqtSignal(QPixmap)

    def __init__(self, socket):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__Socket = socket

        self.hVideo = 480
        self.wVideo = 640
        self.dataPackageSize = self.hVideo * self.wVideo * 3

        self.__working = True

    def run(self):
        # сообщаем об готовности принимать видео
        self.sendTextData("readyGetVideo")
        print("readyGetVideo")

        while self.__working:
            self.getDataServer()

        print("Принятие изображений прекращено!")
        sys.exit()

    def getDataServer(self):
        try:
            dataBits = self.__Socket.recv(self.dataPackageSize * 2)

            # преобразуем биты в объект класса Packer
            data = pickle.loads(dataBits)

            #   Дейсвия в зависимости от команды
            # принять изображение для видео
            if (data.getCommand() == "acceptShot"):
                npImage = numpy.array(data.getData()).reshape(self.hVideo, self.wVideo, 3)
                cv2.imwrite("img1.jpg", npImage)
                # cv2.imwrite("img2.jpg", npImage)

                pix = QPixmap("img1.jpg")

                self.importVideo.emit(pix)

                # запрос на следующие изображение
                self.sendPacker(None, "getShot")

                # запрос информации об пользователе
                self.sendPacker(None, "getInfoVisits")

            # установка информации об пользователе (охраннике)
            if (data.getCommand() == "setInfoVisits"):
                print("Принятие информации об аккаунте")

        except:
            print("соединение с сервером потеряно!")
            # сообщаем ядру об потери соединения
            self.disconnectServer.emit()

            # прекращаем получение данных
            self.__working = False

    # отправить данные с командой
    def sendPacker(self, data, command):
        outBits = pickle.dumps(Packer(command, data))
        self.__Socket.send(outBits)

    def sendTextData(self, textMessage):
        self.__Socket.sendall(textMessage.encode("utf-8"))
