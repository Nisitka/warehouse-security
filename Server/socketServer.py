import numpy
from PyQt5.QtCore import QObject, pyqtSignal

from threading import Thread
import socket as socketNetwork

from Client import guardClient, typeClient, cameraClient

import codecs

import cv2

import sys

import pickle
from packerData import Packer

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
        # принимаем данные для авторизации пользователя
        dataBits = self.__newConnection.recv(2048)

        # преобразуем биты в объект класса Packer
        data = pickle.loads(dataBits)
        dataUser = data.getData()

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

    # добавление нового клиента
    def addNewClient(self, login, tClient):
        print("client add! " + str(tClient))

        # если клиент не охранник, то значит камера
        if (tClient == typeClient.Guard.value):
            # добавляем в список клиентов-охранников нового клиента
            self.__GuardClients.append(guardClient(self.__newConnection, login))

            # информируем об удачной инициализации ПО охранника
            dataUser_DataBase = "Данные аккаунта клинта-охранника"
            self.sendPacker(self.__GuardClients[-1].getSocket(), dataUser_DataBase, 'initUser')

            # выбирается нужная камера по логину охранника (если такой нет, то сообщаем об этом)
            self.cap = self.__requestCamera(self.__GuardClients[-1].getLogin())
            if self.cap is None:
                print("камеры для охранника не найдено")

                # информируем ПО охранника об отсутствии подключенных разрешенных камер
                self.sendPacker(self.__GuardClients[-1].getSocket(), None, 'infoCameras')

            else:
                # информируем ПО охранника об подключеннии разрешенных камер
                infoCameras = "информация об камерах и все такое"
                self.sendPacker(self.__GuardClients[-1].getSocket(), infoCameras, 'infoCameras')

                # добавляем камеру к клиенту охранника
                self.__GuardClients[-1].addCamera(self.cap)

                # запустить клиент-охранника в основном режиме
                self.__GuardClients[-1].start()

        else:
            # добаляем камеру в общий список подкл. камер
            self.__CameraClients.append(cameraClient(self.__newConnection, login))

            # проверяем, есть ли клинты-охранники, которые могут её видеть
            # если да, то добаляем камеры к этим клиентам
            '''
            какой-то код
            '''

            # запускаем клиента (начинает ожидание передачи данных)
            self.__CameraClients[-1].start()

            # сообщаем камере что готовы принимать видео
            self.sendTextData(self.__newConnection, "readyGetVideo")

    def __requestCamera(self, loginGuard):
        if len(self.__CameraClients) > 0:
            return self.__CameraClients[-1]
        else:
            return None

    # проверка наличия соединения со всеми клиентами
    def checkConnectAllClient(self):
        print("проверка соединений")

    # удалить клиента по логину указанного типа
    def removeClient(self, login, tClient):

        if (tClient == typeClient.Guard.value):
            for guardClient in self.__GuardClients:
                if str(guardClient.getLoginGuard()) == login:
                    guardClient.remove()  # разрушаем экземпляр клиента
                    self.__GuardClients.remove(guardClient)  # удаляем его из списка клиентов
                    self.delClient.emit(login, typeClient.Guard.value)  # сообщаем об удалении

    def lockNewClient(self):
        print("client lock!")

        # информируем об неудачной попытке инициализации
        self.sendPacker(self.__GuardClients[-1].getSocket(), None, 'initUser')

        # отключаем этого клиента
        self.__closeSocket(self.__newConnection)

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

    # отправка команды с данными
    def sendPacker(self, socket, data, command):
        outBits = pickle.dumps(Packer(command, data))
        socket.send(outBits)

    def sendTextData(self, socket, data):
        socket.sendall(codecs.encode(str(data), 'UTF-8'))

    def stop(self):
        # выходим из ожидания подключения клиента
        self.__working = False

        self.__closeSocket(self.__serverSocket)  # выключаем сокет сервера
        self.__offClients()

        print("сервер отключен!")