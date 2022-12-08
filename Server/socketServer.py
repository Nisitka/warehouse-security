import numpy
from PyQt5.QtCore import QObject, pyqtSignal

from threading import Thread
import socket as socketNetwork

from Client import guardClient
from Client import typeClient

import codecs
from sendersData import senderViideo

import cv2  # это временно!!!

class socketServer(QObject, Thread):
    # Сигналы:
    # запрос на подключение
    requestConnection = pyqtSignal(str, str, str)  # имя, пароль и адрес клиента
    # инфа об удалении клиента
    delClient = pyqtSignal(str, int)  # логин и тип клиента

    # список клиентов
    __Clients = []
    # список отправщиков видео
    __sendersVideo = []

    # переменные для временного хранения очередного подключения
    __newConnection = "сокет"
    __newClientAddress = "адрес"

    def __init__(self, address, port_, numMaxClients):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__port = port_
        self.__serverSocket = socketNetwork.socket()

        # запуск сервера(сокета) для принятия соединений на
        # соотвествующий адресс и порт
        self.__serverSocket.bind((str(address), int(self.__port)))
        self.__serverSocket.listen(numMaxClients)  # максимальное кол-во подключений

    # преобразует полученные данные от потонциального клиента в логин и пароль
    def __decodeUserData(self):
        dataUser = self.__newConnection.recv(200)
        dataUser = dataUser.decode("utf-8")
        print(dataUser)

        # логин и пароль разделены символом '/'
        dividedData = dataUser.partition('/')
        login = dividedData[0]
        password = dividedData[2]

        return str(login), str(password)

    # выполняется в отдельном потоке (только этот метод!)
    def run(self):
        print("Server run on port: " + str(self.__port))

        self.__working = True
        # запуск ожидания нового подключения
        while(self.__working):
            # ожидание подключения: новый сокет и адрес клиента.
            # Именно этот сокет и будет использоваться для приема и посылке клиенту данных.
            self.__newConnection, self.__newClientAddress = self.__serverSocket.accept()
            # self.addNewClient()

            login, password = self.__decodeUserData()
            self.requestConnection.emit(login, password, str(self.__newClientAddress))

        print("Server stopped")

    def addNewClient(self, login):
        print("client add!")

        # добавляем в список клиентов нового клиента
        self.__Clients.append(guardClient(self.__newConnection, self.__newClientAddress, login))

        # информируем об удачной инициализации
        self.sendTextData(self.__Clients[-1].getSocket(), "initSuccessfully")

        # дожидаемся готовности клиента и только тогда начинаем транслировать видео
        data = self.waitData()
        print(data)

        # создать новый объект камеру
        self.cap = cv2.VideoCapture(0)  # временно!

        # оргнизация передача данных из камеры клиенту-охраннику в отдельном потоке
        newSender = senderViideo(self.cap, self.__Clients[-1])
        newSender.disabled[str, int].connect(self.disconnectClient)
        newSender.start()

    def disconnectClient(self, login, tClient):

        if (tClient == typeClient.Guard.value):
            for guardClient in self.__Clients:
                if str(guardClient.getLoginGuard()) == login:
                    guardClient.remove()  # разрушаем экземпляр клиента
                    self.__Clients.remove(guardClient)  # удаляем его из списка клиентов
                    self.delClient.emit(login, typeClient.Guard.value)  # сообщаем об удалении

    def lockNewClient(self):
        print("client lock!")

        # информируем об неудачной попытке инициализации
        self.sendTextData(self.__newConnection, "initFail")
        self.__newConnection.close()

    def waitData(self):
        while True:
            dataUser = self.__newConnection.recv(200)
            dataUser = dataUser.decode("utf-8")
            if not dataUser:
                break
            else:
                return dataUser

    # отправка данных через указанный сокет (кому, что)
    def sendTextData(self, socket, data):
        socket.sendall(codecs.encode(str(data), 'UTF-8'))

    def __offClients(self):
        if (len(self.__Clients) > 0):
            for i in range(len(self.__Clients)):
                self.__Clients[i].remove()
            self.__Clients.clear()  # очищаем список клиентов

    def stop(self):
        self.__serverSocket.close()  # выключаем сокет сервера

        self.__offClients()

        self.__working = False
        self.join()

        print("сервер отключен!")