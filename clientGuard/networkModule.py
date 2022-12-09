from PyQt5.QtCore import QObject, pyqtSignal

from threading import Thread

import cv2  # это временно!!!
from PyQt5.QtGui import QImage, QPixmap, QColor

import time

import numpy

import socket
import codecs
import pickle
import json

class Socket(QObject, Thread):
    importData = pyqtSignal(QPixmap, QPixmap)

    # результат авторизации пользователя
    initUserInfo = pyqtSignal(bool)

    # результы поиска разрешенных камер
    initCamerasInfo = pyqtSignal(bool)

    # запрос ядру на принятие изображений с сервера
    startAcceptVideo = pyqtSignal()

    # сообщаем ядру о потери соединения
    disconnectServer = pyqtSignal()

    hVideo = 480
    wVideo = 640
    dataPackageSize = hVideo * wVideo * 3

    def __init__(self):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__working = True

        # кол-во принятых пакетов
        self.currentPacked = 0

    def connectServer(self, host, port, login, password):
        # инициализируем свой сокет
        self.__clientSocket = socket.socket()
        self.__clientSocket.connect((host, port))

        # отправляем логин с паролем
        message = str(login) + '/' + str(password)  # шифр из логина и пароля
        self.sendTextData(message)

        # ждем результатов аутентификации
        dataServer = self.waitTextData()

        if (dataServer == "initSuccessfully"):
            # информиркем ядро приложения об результатах аутентификации
            self.initUserInfo.emit(True)

            # информируем сервер об принятии результатов авторизации
            self.sendTextData("getInfoInit")

            # ждем информации об камерах
            dataCameras = self.waitTextData()
            # информируем сервер об принятии инфы об камерах
            self.sendTextData("getInfoCameras")
            if (dataCameras == "readyCameras"):
                # сообщаем ядру об присутсвии разрешенных камер
                self.initCamerasInfo.emit(True)

                # ждем запроса на отправку видео
                request = self.waitTextData()
                print(request)

                # подготовка к принятию видео

                # запускаем прием видео
                self.startAcceptVideo.emit()

            else:
                # сообщаем ядру об отсутсвии разрешенных камер
                self.initCamerasInfo(False)
        else:
            # информиркем ядро приложения об результатах аутентификации
            self.initUserInfo.emit(False)

    # получение изображений от сервера
    def run(self):
        # сообщаем об готовности принимать видео
        self.sendTextData("readyGetVideo")
        print("readyGetVideo")

        while self.__working:
            self.getDataServer()

        print("Принятие изображений прекращено!")

    def getDataServer(self):
        try:
            data = self.__clientSocket.recv(self.dataPackageSize + 10)
            data = list(data)

            if (len(data) != self.dataPackageSize):
                print("потеря данных!")

                # запрос следующего изображения
                self.sendTextData("Get")
            else:
                # print("accept!")
                npImage = numpy.array(data).reshape(self.hVideo, self.wVideo, 3)
                cv2.imwrite("img1.jpg", npImage)
                cv2.imwrite("img2.jpg", npImage)

                pix = QPixmap("img1.jpg")

                self.importData.emit(pix, pix)

                # сообщаем о том, что готовы к след. изображению
                self.sendTextData("Get")

        except:
            print("соединение с сервером потеряно!")
            # сообщаем ядру об потери соединения
            self.disconnectServer.emit()

            # прекращаем получение данных
            self.__working = False

    def sendTextData(self, textMessage):
        self.__clientSocket.sendall(textMessage.encode("utf-8"))

    # ожидание текстовой информации
    def waitTextData(self):
        while True:
            dataServer = self.__clientSocket.recv(512)
            dataServer = dataServer.decode("utf-8")
            if not dataServer:
                break
            else:
                return dataServer

    def stop(self):
        self.__working = False
        self.join()

