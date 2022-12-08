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
    initUserInfo = pyqtSignal(bool) # результат авторизации пользователя

    hVideo = 480
    wVideo = 640
    dataPackageSize = hVideo * wVideo * 3

    def __init__(self):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__working = True

        # создать новый объект камеру
        self.cap = cv2.VideoCapture(0)  # временно!

    def connectServer(self, host, port, login, password):
        # инициализируем свой сокет
        self.__clientSocket = socket.socket()
        self.__clientSocket.connect((host, port))

        message = str(login) + '/' + str(password)  # шифр из логина и пароля
        self.__clientSocket.sendall(message.encode("utf-8"))

        dataServer = self.waitData()

        # информируем об принятии результатов авторизации
        message = "getInfoInit"
        self.__clientSocket.sendall(message.encode("utf-8"))

        print(dataServer)
        self.initUserInfo.emit(not dataServer == "initFail")

    def run(self):
        while self.__working:
            self.getDataServer()

        print("Сетевой модуль выключен!")

    # ожидание текстовой информации
    def waitData(self):
        while True:
            dataServer = self.__clientSocket.recv(200)
            dataServer = dataServer.decode("utf-8")
            if not dataServer:
                break
            else:
                return dataServer

    def getDataServer(self):
        data = self.__clientSocket.recv(self.dataPackageSize + 10)  # self.dataPackageSize
        # print(len(list(data)))

        data = list(data)
        if (len(data) != self.dataPackageSize):
            print("потеря данных!")
        else:
            npImage = numpy.array(data).reshape(self.hVideo, self.wVideo, 3)
            cv2.imwrite("img1.jpg", npImage)
            cv2.imwrite("img2.jpg", npImage)

            pix = QPixmap("img1.jpg")

            self.importData.emit(pix, pix)

        # сообщаем о том, что готовы к след. изображению
        message = "Get"
        for i in range(5):
            self.__clientSocket.sendall(message.encode("utf-8"))

        # _, image = self.cap.read()  # потом это будет инфа с сервера

        # h = image.shape[0]
        # w = image.shape[1]

        # format = QImage.Format_BGR888
        # qimage = QImage(image.data, w, h, format) # Format_Indexed8

        # pix = QPixmap.fromImage(qimage)
        # self.importData.emit(pix, pix)

    def stop(self):
        self.__working = False
        self.join()

