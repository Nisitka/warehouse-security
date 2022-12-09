from PyQt5.QtCore import QObject, pyqtSignal

import socket
import codecs

from threading import Thread

import sys

from senderVideoModule import senderVideo

class Socket(QObject, Thread):

    def __init__(self):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__working = True

    def connectServer(self, host, port, login, password):
        # инициализируем свой сокет
        self.__Socket = socket.socket()
        # соеденяем его с сервером
        self.__Socket.connect((host, port))

        # отправляем логин с паролем
        message = str(login) + '/' + str(password)  # шифр из логина и пароля
        self.sendTextData(message)

        #
        data = self.waitTextData()
        print(data)
        if (data == "readyGetVideo"):
            self.sendVideo()

    def sendVideo(self):
        # создаем отправщика видео
        self.sender = senderVideo(self.__Socket)
        self.sender.start()

    # ожидание тестовых данных
    def waitTextData(self):
        while True:
            dataServer = self.__Socket.recv(100)
            dataServer = dataServer.decode("utf-8")
            if not dataServer:
                break
            else:
                return dataServer

    # отправка текстовых данных
    def sendTextData(self, textMessage):
        self.__Socket.sendall(textMessage.encode("utf-8"))