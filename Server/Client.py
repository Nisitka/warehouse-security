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

# потом реализовать насследование от скласса Client!!!!

class guardClient(QObject, Thread):
    getNewImageSignal = pyqtSignal()

    def __init__(self, socket_, loginGuard_):
        QObject.__init__(self)
        Thread.__init__(self)

        self.hVideo = 480
        self.wVideo = 640
        self.imageSize = self.hVideo * self.wVideo * 3

        self.__login = loginGuard_

        # сокет взаимодействия с охранником
        self.__Socket = socket_

        self.__work = True

    def getLogin(self):
        return self.__login

    def send(self, data):
        self.__Socket.send(data)

    def getSocket(self):
        return self.__Socket

    def waitCommand(self):
        command = self.__Socket.recv(200)
        return command.decode("utf-8")

    # всегда ждет команды от охранника
    def run(self):
        while self.__work:
            try:
                command = self.waitCommand()
                if command == "Get":
                    # сообщаем об готовности принять новое изображение
                    self.getNewImageSignal.emit()
            except:
                print("соединение с охранником потеряно")

        sys.exit()

    def remove(self):
        self.__work = False
        self.__closeSocket()

    def __closeSocket(self):
        try:
            self.__Socket.shutdown(socketNetwork.SHUT_RDWR)
            print("Это Linux")
        except:
            print("Это windows")

        self.__Socket.close()  # отключаем сокет


class cameraClient(QObject, Thread):
    updateImage = pyqtSignal()

    def __init__(self, socket_, loginCamera_):
        QObject.__init__(self)
        Thread.__init__(self)

        self.hVideo = 480
        self.wVideo = 640
        self.imageSize = self.hVideo * self.wVideo * 3

        self.login = loginCamera_

        # сокет взаимодействия с камерой
        self.__Socket = socket_

        self.__work = True

    def send(self, data):
        self.__Socket.send(data)

    # запросить изображение у камеры
    def requestImage(self):
        self.__Socket.sendall("get".encode("utf-8"))

    def getCurrentImage(self):
        return self.currentImage

    def acceptImage(self):
        image = self.__Socket.recv(self.imageSize)
        image = list(image)

        # print(len(image))  # кол-во эдементов в массиве
        if (len(image) != self.imageSize):
            print("потеря данных!")

        else:
            self.currentImage = numpy.array(image).reshape(self.hVideo, self.wVideo, 3)

            # костыль чтобы картинка выглядела не как в 80-х
            #   (потом будет реализовано сохранение картинрк -> перевод их в видео)
            cv2.imwrite("img.jpg", self.currentImage)
            self.currentImage = cv2.imread("img.jpg")

            self.updateImage.emit()

    def remove(self):
        self.__work = False
        self.__closeSocket()

    def __closeSocket(self):
        try:
            self.__Socket.shutdown(socketNetwork.SHUT_RDWR)
            print("Это Linux")
        except:
            print("Это windows")

        self.__Socket.close()  # отключаем сокет

    # всегда ждет принятие нового изображения
    def run(self):
        while self.__work:
            try:
                self.acceptImage()

            except:
                print("Соединение с камерой потеряно")

        sys.exit()
