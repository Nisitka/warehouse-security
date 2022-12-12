from PyQt5.QtCore import QObject, pyqtSignal
from threading import Thread

import datetime
import codecs

import enum

import cv2

import os
import sys

from PyQt5.QtGui import QImage, QPixmap, QColor

import numpy
import pickle

from packerData import Packer
from processingImages import processingImage

import socket as socketNetwork

from PIL import Image

# типы клиентов
class typeClient(enum.Enum):
    Guard = 1
    Camera = 2

class typeObjCamera(enum.Enum):
    Gate = 0
    Barrier = 1

# потом реализовать насследование от скласса Client!!!!

class guardClient(QObject, Thread):
    # запросить новый кадр для видео
    getNewImageSignal = pyqtSignal()

    # запросить информацию об клиенте
    getUserInfoSignal = pyqtSignal(str)  # по логину

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

        self.__Cameras = [None, None]

    def getLogin(self):
        return self.__login

    def getSocket(self):
        return self.__Socket

    # добавление камеры клиенту
    def addCamera(self, cameraClient):

        if cameraClient.getObjType() == 'Gate':
            self.__Cameras[typeObjCamera.Gate.value] = cameraClient
        if cameraClient.getObjType() == 'Barrier':
            self.__Cameras[typeObjCamera.Barrier.value] = cameraClient

        cameraClient.updateImage[str].connect(self.sendImageGuard)
        cameraClient.requestImage()

    def acceptImageGate(self):
        self.__Cameras[typeObjCamera.Gate.value].requestImage()

    def acceptImageBarrier(self):
        self.__Cameras[typeObjCamera.Barrier.value].requestImage()

    # отправка изображения с камеры охраннику
    def sendImageGuard(self, typeCamera):
        print(self.__Cameras)

        if typeCamera == 'Gate':
            outImage = self.__Cameras[typeObjCamera.Gate.value].getCurrentImage()
        if typeCamera == 'Barrier':
            outImage = self.__Cameras[typeObjCamera.Barrier.value].getCurrentImage()

        outImage = processingImage(outImage)

        outBits = pickle.dumps(Packer("acceptShot" + str(typeCamera), outImage))

        self.__Socket.send(outBits)

    def waitData(self):
        try:
            dataBits = self.__Socket.recv(2048)
            # преобразуем биты в объект класса Packer
            data = pickle.loads(dataBits)

            return data

        except:
            # отправка сигнла в ядро об потери соединения с  клиентом-охранником
            print("соединение с охранником потеряно!")

    # всегда ждет команды от охранника
    def run(self):
        while self.__work:
            # принятие команды
            dataPacker = self.waitData()
            command = dataPacker.getCommand()

            #   Действия по командам:
            # запросить передачу нового кадра у сервера
            if command == "getShotGate":
                # принимаем новое изображение
                self.acceptImageGate()

            if command == "getShotBarrier":
                # принимаем новое изображение
                self.acceptImageBarrier()

            # запросить инфу об клиенте (для теста!!!!!)
            if command == "getInfoVisits":
                self.getUserInfoSignal.emit(str(self.__login))

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
    updateImage = pyqtSignal(str)  # передаем свой тип

    def __init__(self, socket_, loginCamera_, objType, smartType=1, IPv4 = None):
        QObject.__init__(self)
        Thread.__init__(self)

        self.hVideo = 480
        self.wVideo = 640

        self.__objType = objType

        self.__smartType = smartType
        if (self.__smartType == 2):
            self.cap = cv2.VideoCapture('http://' + str(IPv4) +':8080/video')
            self.acceptImage()

        else:
            # сокет взаимодействия с камерой
            self.__Socket = socket_

        self.imageSize = self.hVideo * self.wVideo * 3

        self.login = loginCamera_

        self.__work = True

    def getObjType(self):
        return self.__objType

    def send(self, data):
        self.__Socket.sendall(data)

    # запросить изображение у камеры
    def requestImage(self):
        if (self.__smartType == 1):
            # если проводна то отправить запрос на ПО ПК с web-камерой
            self.__Socket.sendall("get".encode("utf-8"))
        else:
            # если камера сетевая то сразу взять изображение
            self.acceptImage()

    def getCurrentImage(self):
        return self.currentImage

    def acceptImage(self):
        if (self.__smartType == 1):
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

        else:
            _, image = self.cap.read()

            try:
                self.currentImage = cv2.resize(image, (self.wVideo, self.hVideo))
            except:
                print("потеря данных")

        # сообщаем об измененном изображении
        self.updateImage.emit(self.__objType)

    def remove(self):
        self.__work = False

        if (self.__smartType == 1):
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
        if (self.__smartType == 1):
            # сообщаем камере что готовы принимать видео
            self.__Socket.sendall(codecs.encode("readyGetVideo", 'UTF-8'))

        while self.__work:
            try:
                self.acceptImage()

            except:
                print("Соединение с камерой потеряно")

        sys.exit()

    def sendTextData(self, socket, data):
        socket.sendall(codecs.encode(str(data), 'UTF-8'))
