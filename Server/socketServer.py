import numpy
from PyQt5.QtCore import QObject, pyqtSignal

from threading import Thread
import socket as socketNetwork

from Client import guardClient, typeClient, cameraClient

import codecs
from sendersData import senderVideo

import cv2  # это временно!!!

import sys

class socketServer(QObject, Thread):
    # Сигналы:
    # запрос на подключение клиента
    requestConnectionClient = pyqtSignal(str, str, str)  # логин, пароль и адрес клиента

    # инфа об удалении клиента
    delClient = pyqtSignal(str, int)  # логин и тип клиента

    # список клиентов-охранников
    __GuardClients = []
    # список камер
    __CameraClients = []
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
        self.__serverSocket = socketNetwork.socket(socketNetwork.AF_INET, socketNetwork.SOCK_STREAM)
        self.__serverSocket.setsockopt(socketNetwork.SOL_SOCKET, socketNetwork.SO_REUSEADDR, 1)

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
            # аутентификация
            self.requestConnectionClient.emit(login, password, str(self.__newClientAddress))

        sys.exit()

    def addNewClient(self, login, tClient):
        print("client add! " + str(tClient))

        # если клиент не охранник, то значит камера
        if (tClient == typeClient.Guard.value):
            # добавляем в список клиентов-охранников нового клиента
            self.__GuardClients.append(guardClient(self.__newConnection, login))

            # информируем об удачной инициализации ПО охранника
            self.sendTextData(self.__GuardClients[-1].getSocket(), "initSuccessfully")

            # дожидаемся готовности клиента и только тогда отправляем инфу об камерах
            data = self.waitTextData(self.__GuardClients[-1].getSocket())
            print(data + "!!!!")

            # выбирается нужная камера (если такой нет, то сообщаем об этом)
            self.cap = self.__requestCamera(self.__GuardClients[-1].getLogin())
            if self.cap is None:
                print("камеры для охранника не найдено")

                # информируем ПО охранника об отсутствии подключенных разрешенных камер
                self.sendTextData(self.__GuardClients[-1].getSocket(), "notCameras")

            else:
                self.sendTextData(self.__GuardClients[-1].getSocket(), "readyCameras")

                # дожидаемся ответа кдиента об принятии инфы об камерах
                data = self.waitTextData(self.__GuardClients[-1].getSocket())
                print(data)

                # отправляем запрос на отправку видео
                self.sendTextData(self.__GuardClients[-1].getSocket(), "sendVideo")

                # результат запроса (в этот момент клиент готов принимать карнинки)
                data = self.waitTextData(self.__GuardClients[-1].getSocket())
                print(data)
                if (data == "readyGetVideo"):
                    # запустить клиент-охранника в основном режиме
                    self.__GuardClients[-1].start()

                    # оргнизация передача данных из камеры клиенту-охраннику в отдельном потоке
                    self.newSender = senderVideo(self.cap, self.__GuardClients[-1])
                    self.newSender.run()  # запускаем его

        else:
            # добаляем камеру в общий список подкл. камер
            self.__CameraClients.append(cameraClient(self.__newConnection, login))

            # запускаем клиента (начинает ожидание передачи данных)
            self.__CameraClients[-1].start()

            # сообщаем камере что готовы принимать видео
            self.sendTextData(self.__newConnection, "readyGetVideo")

    def __requestCamera(self, loginGuard):
        if len(self.__CameraClients) > 0:
            return self.__CameraClients[-1]
        else:
            return None

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

        # отключаем этого клиента
        self.__closeSocket(self.__newConnection)

    def waitTextData(self, socket):
        while True:
            dataUser = socket.recv(200)
            dataUser = dataUser.decode("utf-8")
            if not dataUser:
                break
            else:
                return dataUser

    # отправка данных через указанный сокет (кому, что)
    def sendTextData(self, socket, data):
        socket.sendall(codecs.encode(str(data), 'UTF-8'))

    # отключаем всех клиентов
    def __offClients(self):
        if (len(self.__GuardClients) > 0):
            # разрушаем каждоного клиента
            for i in range(len(self.__GuardClients)):
                self.__GuardClients[i].remove()

            # очищаем список клиентов
            self.__GuardClients.clear()

        if (len(self.__CameraClients) > 0):
            # разрушаем каждоного клиента
            for i in range(len(self.__CameraClients)):
                self.__CameraClients[i].remove()

            # очищаем список клиентов
            self.__CameraClients.clear()

    def __closeSocket(self, socket):
        try:
            socket.shutdown(socketNetwork.SHUT_RDWR)
            print("Это Linux")
        except:
            print("Это windows детка")

        socket.close()  # отключаем сокет

    def stop(self):
        # выходим из ожидания подключения клиента
        self.__working = False

        self.__closeSocket(self.__serverSocket)  # выключаем сокет сервера
        self.__offClients()

        print("сервер отключен!")