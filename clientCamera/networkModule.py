from PyQt5.QtCore import QObject, pyqtSignal

import socket as socketNetwork
import codecs

from threading import Thread

import sys

from senderVideoModule import senderVideo

class Socket(QObject, Thread):
    resultConnect = pyqtSignal(bool)

    def __init__(self):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__working = True

    def connectServer(self, host, port, login, password):
        # инициализируем сокет
        self.__Socket = socketNetwork.socket(socketNetwork.AF_INET, socketNetwork.SOCK_STREAM)
        self.__Socket.setsockopt(socketNetwork.SOL_SOCKET, socketNetwork.SO_REUSEADDR, 1)

        # попытка присоединиться к серверу
        try:
            # соединение с сервером
            self.__Socket.connect((host, port))

            # сообщаем интерфейсу об результатах попытки присоединиться
            self.resultConnect.emit(True)

            # отправляем логин с паролем
            message = str(login) + '/' + str(password)  # шифр из логина и пароля
            self.sendTextData(message)

            # ждем команды о том, что сервер готов принмать изображения
            command = self.waitTextData()
            if (command == "readyGetVideo"):
                self.setSenderVideo()

        except:
            self.resultConnect.emit(False)

    def setSenderVideo(self):
        # создаем отправщика видео
        self.sender = senderVideo(self.__Socket)

        # сразу запускаем его в отдельном потоке:
        #   (всегда ждем команды на отправки изображения)
        self.sender.start()

    # ожидание текстовых данных
    def waitTextData(self):
        dataServer = self.__Socket.recv(100)
        return dataServer.decode("utf-8")

    # отправка текстовых данных
    def sendTextData(self, textMessage):
        self.__Socket.sendall(textMessage.encode("utf-8"))