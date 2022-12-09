from PyQt5.QtCore import QObject, pyqtSignal
from threading import Thread

import datetime
import codecs

import enum

import cv2  # это временно!!!

import os
import sys

import numpy

# типы клиентов
class typeClient(enum.Enum):
    Guard = 1
    Camera = 2

class guardClient(QObject, Thread):
    dataPackageSize = 2048 * 1000 * 1000

    def __init__(self, socket_, address_, loginGuard_):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__loginGuard = loginGuard_

        self.__socket = socket_
        self.__address = address_

        self.__working = False
        self.__init = False

        # как только создаем клиента сразу же запускаем поток на принятие данных
        self.start()

    def run(self):
        self.__working = True

    def getSocket(self):
        return self.__socket

    def __stopGetData(self):
        self.__working = False

    def __waitData(self):
        while(self.__working):
            try:
                data = self.__socket.recv(self.dataPackageSize)
            except:
                print("не удалось получить данные")

            if not data:
                print("данные не переданы!")

    def remove(self):
        self.__stopGetData()
        self.__socket.close()

        # self.destroyed.emit(str(self.__loginGuard), typeClient.Guard.value)
        print("Клиент удален!")

    def getLoginGuard(self):
        return self.__loginGuard

class cameraClient(QObject, Thread):

    def __init__(self, socket_, loginCamera_):
        QObject.__init__(self)
        Thread.__init__(self)

        self.hVideo = 480
        self.wVideo = 640
        self.imageSize = self.hVideo * self.wVideo * 3

        # сокет взаимодействия с камерой
        self.__Socket = socket_

        self.__login = loginCamera_

        self.__work = True

    def getSocket(self):
        return self.__Socket

    def remove(self):
        self.__work = False

    def read(self):
        return self.__currentImage

    def acceptImage(self):
        try:
            data = self.__Socket.recv(self.imageSize)
            data = list(data)

            # print(len(data))
            if (len(data) != self.imageSize):
                print("потеря данных!")

                # запрос следующего изображения
                self.sendTextData("Get")
            else:
                # print("accept!")
                self.__currentImage = numpy.array(data).reshape(self.hVideo, self.wVideo, 3)

                # сообщаем о том, что готовы к след. изображению
                self.sendTextData("Get")
        except:
            print("соединение с камерой потеряно!")
            # сообщаем ядру об потери соединения

            # прекращаем получение данных
            self.__work = False

    def sendTextData(self, textMessage):
        self.__Socket.sendall(textMessage.encode("utf-8"))

    def run(self):
        # получение данных
        while self.__work:
            try:
                self.acceptImage()

            except:
                print("данные с камеры не получены!")

        print("получение данных с камеры прекращено")
        sys.exit()