from PyQt5.QtCore import QObject, pyqtSignal

from threading import Thread

import cv2  # это временно!!!
from PyQt5.QtGui import QImage, QPixmap, QColor

import time

import numpy

import socket as socketNetwork
import codecs

import sys

import pickle
from packerData import Packer

#from threadersAcceptData import threadAcceptCommand

class Socket(QObject, Thread):
    importVideoSignal = pyqtSignal(QPixmap, QPixmap)

    # результат авторизации пользователя
    initUserInfo = pyqtSignal(bool)

    # результы поиска разрешенных камер
    initCamerasInfo = pyqtSignal(bool)

    # запрос ядру на принятие изображений с сервера
    startAcceptData = pyqtSignal()

    # сообщаем ядру о потери соединения
    disconnectServerSignal = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)
        Thread.__init__(self)

        self.hVideo = 480
        self.wVideo = 640
        self.numPixImage = self.hVideo * self.wVideo * 3

        self.__working = True

    def run(self):
        while self.__working:
            print("_")
            self.getDataServer()

        print("Принятие изображений прекращено!")
        sys.exit()

    def getDataServer(self):
        #try:
            # принимаем любые данные
            dataBits = self.__Socket.recv(self.numPixImage * 10)

            # преобразуем биты в объект класса Packer
            data = pickle.loads(dataBits)
            command = data.getCommand()

            #   Дейсвия в зависимости от команды
            # принять изображение для видео
            if (command == "acceptShot"):
                npImage = numpy.array(data.getData()).reshape(self.hVideo, self.wVideo, 3)
                cv2.imwrite("img1.jpg", npImage)
                # cv2.imwrite("img2.jpg", npImage)

                pix = QPixmap("img1.jpg")

                self.importVideoSignal.emit(pix, pix)

                # запрос на следующие изображение
                self.sendPacker(None, "getShot")

                # запрос информации об пользователе
                self.sendPacker(None, "getInfoVisits")

            #
            if (command == "setInfoVisits"):
                print("Принятие информации об визитах")

            # установка информации об пользователе (охраннике)
            if (command == "initUser"):
                infoUser = data.getData()
                if infoUser is None:
                    self.initUserInfo.emit(False)
                    print("Неверный логин или пароль")
                else:
                    self.initUserInfo.emit(True)
                    print(infoUser)

            if (command == "infoCameras"):
                infoCameras = data.getData()
                if infoCameras is None:
                    print("нет разрешенных камер")
                    self.initCamerasInfo.emit(False)
                else:
                    print("разрешенные камеры есть: " + infoCameras)
                    self.initCamerasInfo.emit(True)

            '''
            # except:
            print("соединение с сервером потеряно!")
            # сообщаем ядру об потери соединения
            self.disconnectServer.emit()

            # прекращаем получение данных
            self.__working = False
            '''

    def connectServer(self, host, port, login, password):
        # инициализируем свой сокет
        # self.__Socket = socket.socket()
        self.__Socket = socketNetwork.socket(socketNetwork.AF_INET, socketNetwork.SOCK_STREAM)
        self.__Socket.setsockopt(socketNetwork.SOL_SOCKET, socketNetwork.SO_REUSEADDR, 1)
        # соеденяем его с сервером
        # try:
        self.__Socket.connect((host, port))
            # отправляем запрос на подключение
        authData = str(login) + '/' + str(password)  # шифр из логина и пароля
        self.sendPacker(authData, "authUser")

            # запускаем модуль на принятие команд с сервера
        self.start()

        #except:
            #print("неверные данные для авторизации!!!")

    def disconnectServer(self):
        # сообщаем ядру об отключении сервера
        self.disconnectServerSignal.emit()

    def outVideo(self, pix):
        self.importVideoSignal.emit(pix, pix)

    # отправка команды с данными
    def sendPacker(self, data, command):
        outBits = pickle.dumps(Packer(command, data))
        self.__Socket.send(outBits)