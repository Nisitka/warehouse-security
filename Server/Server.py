from PyQt5.QtCore import QObject, pyqtSignal
from socketServer import socketServer

import socket as socketNetwork

class Server(QObject):
    # сигнал об запуске сокета сервера
    runServer = pyqtSignal(str, str)  # имя хоста и адрес
    # сигнал подключения клиента
    newClientConnection = pyqtSignal(str, str)

    def __init__(self):
        QObject.__init__(self)

        # имя хоста сервера
        self.__nameHost = socketNetwork.gethostname()
        # адрес сервера
        self.__address = socketNetwork.gethostbyname(self.__nameHost)

    # запуск сервера (сокета, который его олицетворяет в сети)
    def run(self, port, numClients):
        self.__socket = socketServer(self.__address, port, numClients)
        self.__socket.start()

        self.runServer.emit(self.__nameHost, self.__address)

    # обратиться к сокету сервера
    def getSocket(self):
        return self.__socket

    # выключить сервер
    def stop(self):
        self.__socket.stop()
        # del self.__socket

