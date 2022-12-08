from PyQt5.QtCore import QObject, pyqtSignal
from threading import Thread

import datetime
import codecs

import enum

import cv2  # это временно!!!

# типы клиентов
class typeClient(enum.Enum):
    Guard = 1
    Barrier = 2

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

        self.__waitData()

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
    dataPackageSize = 2048 * 1000 * 1000

    def __init__(self, socket_, loginCamera_):
        QObject.__init__(self)
        Thread.__init__(self)

        # сокет взаимодействия с камерой
        self.__socket = socket_

        self.__login = loginCamera_

        # создать новый объект камеру
        self.cap = cv2.VideoCapture(0) # временно!

    def read(self):
        return self.__currentImage

    def acceptImage(self):
        _, image = self.cap.read()

        return image

    def run(self):
        # получение данных
        try:
            self.__currentImage = acceptImage()
        except:
            print("данные с камеры не получены!")
