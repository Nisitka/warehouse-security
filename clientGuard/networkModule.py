from PyQt5.QtCore import QObject, pyqtSignal

from threading import Thread

import cv2  # это временно!!!
from PyQt5.QtGui import QImage, QPixmap, QColor

import time

import numpy

import socket as socketNetwork
import codecs

import sys

from threadersAcceptData import threadVideo

class Socket(QObject, Thread):
    importVideoSignal = pyqtSignal(QPixmap, QPixmap)

    # результат авторизации пользователя
    initUserInfo = pyqtSignal(bool)

    # результы поиска разрешенных камер
    initCamerasInfo = pyqtSignal(bool)

    # запрос ядру на принятие изображений с сервера
    startAcceptVideo = pyqtSignal()

    # сообщаем ядру о потери соединения
    disconnectServerSignal = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__working = True

    def connectServer(self, host, port, login, password):
        # инициализируем свой сокет
        # self.__Socket = socket.socket()
        self.__Socket = socketNetwork.socket(socketNetwork.AF_INET, socketNetwork.SOCK_STREAM)
        self.__Socket.setsockopt(socketNetwork.SOL_SOCKET, socketNetwork.SO_REUSEADDR, 1)
        # соеденяем его с сервером
        self.__Socket.connect((host, port))

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
    def acceptVideo(self):
        # создаем примщика видео потока
        self.threadAcceptVideo = threadVideo(self.__Socket)
        self.threadAcceptVideo.importVideo[QPixmap].connect(self.outVideo)
        self.threadAcceptVideo.disconnectServer.connect(self.disconnectServer)

        self.threadAcceptVideo.start()

    def disconnectServer(self):
        # очищаем ссылку
        del self.threadAcceptVideo

        # сообщаем ядру об отключении сервера
        self.disconnectServerSignal.emit()

    def outVideo(self, pix):
        self.importVideoSignal.emit(pix, pix)

    # отправка текстовых данных
    def sendTextData(self, textMessage):
        self.__Socket.sendall(textMessage.encode("utf-8"))

    # ожидание текстовой информации
    def waitTextData(self):
        while True:
            dataServer = self.__Socket.recv(512)
            dataServer = dataServer.decode("utf-8")
            if not dataServer:
                break
            else:
                return dataServer