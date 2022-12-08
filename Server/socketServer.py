import numpy
from PyQt5.QtCore import QObject, pyqtSignal

from threading import Thread
import socket as socketNetwork

from Client import guardClient, typeClient, cameraClient

import codecs
from sendersData import senderViideo

import cv2  # это временно!!!

import sys

class socketServer(QObject, Thread):
    # Сигналы:
    # запрос на подключение клиента-охранника
    requestConnectionGuard = pyqtSignal(str, str, str)  # логин, пароль и адрес клиента
    # запрос на подключение клиента-камеры
    requestConnectionCamera = pyqtSignal(str, str)  # логин и адрес клиента

    # инфа об удалении клиента
    delClient = pyqtSignal(str, int)  # логин и тип клиента

    # список клиентов-охранников
    __GuardClients = []
    # список камер
    __Camers = []
    # список отправщиков видео
    __sendersVideo = []

    # переменные для временного хранения очередного подключения
    __newConnection = "сокет"
    __newClientAddress = "адрес"

    def __init__(self, address, port_, numMaxClients):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__address = address
        self.__port = port_
        self.__serverSocket = socketNetwork.socket()

        # запуск сервера(сокета) для принятия соединений на
        # соотвествующий адресс и порт
        self.__serverSocket.bind((str(self.__address), int(self.__port)))
        self.__serverSocket.listen(numMaxClients)  # максимальное кол-во подключений

        self.__working = True
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
        print("Server run on " + str(self.__address) + ":" + str(self.__port))

        # запуск ожидания нового подключения
        while(self.__working):
            # ожидание подключения: новый сокет и адрес клиента.
            # Именно этот сокет и будет использоваться для приема и посылке клиенту данных.
            try:
                self.__newConnection, self.__newClientAddress = self.__serverSocket.accept()
            except:
                break
            login, password = self.__decodeUserData()
            # при получении особого шифра вместо пароля мы понимаем что это камера
            if password == "f8o13_vn2fk84ds_43f":
                print("присоединение камеры!")

            else:
                # аутентификация
                self.requestConnectionGuard.emit(login, password, str(self.__newClientAddress))

        sys.exit()

    def addNewClient(self, login):
        print("client add!")

        # добавляем в список клиентов нового клиента
        self.__GuardClients.append(guardClient(self.__newConnection, self.__newClientAddress, login))

        # информируем об удачной инициализации
        self.sendTextData(self.__GuardClients[-1].getSocket(), "initSuccessfully")

        # дожидаемся готовности клиента и только тогда начинаем транслировать видео
        data = self.waitData()
        print(data)

        # создать новый объект камеру
        self.cap = cv2.VideoCapture(0)  # временно!

        # оргнизация передача данных из камеры клиенту-охраннику в отдельном потоке
        newSender = senderViideo(self.cap, self.__GuardClients[-1])
        newSender.disabled[str, int].connect(self.disconnectClient)
        newSender.start()

    def disconnectClient(self, login, tClient):

        if (tClient == typeClient.Guard.value):
            for guardClient in self.__GuardClients:
                if str(guardClient.getLoginGuard()) == login:
                    guardClient.remove()  # разрушаем экземпляр клиента
                    self.__GuardClients.remove(guardClient)  # удаляем его из списка клиентов
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
        if (len(self.__GuardClients) > 0):
            for i in range(len(self.__Clients)):
                self.__GuardClients[i].remove()
            self.__GuardClients.clear()  # очищаем список клиентов

    def stop(self):
        # выходим из ожидания подключения клиента
        self.__working = False

        self.__serverSocket.close()  # выключаем сокет сервера
        self.__offClients()

        print("сервер отключен!")