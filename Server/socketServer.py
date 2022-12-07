from PyQt5.QtCore import QObject, pyqtSignal

from threading import Thread
import socket as socketNetwork

from Client import threadClient

import codecs

class socketServer(QObject, Thread):
    # список клиентов
    __Clients = []

    # запрос на подключение
    requestConnection = pyqtSignal(str, str, str)  # имя, пароль и адрес клиента

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

    # выполняется в отдельном потоке
    def run(self):
        print("Server run on port: " + str(self.__port))

        self.__working = True
        # запуск ожидания нового подключения
        while(self.__working):
            # ожидание подключения: новый сокет и адрес клиента.
            # Именно этот сокет и будет использоваться для приема и посылке клиенту данных.
            self.__newConnection, self.__newClientAddress = self.__serverSocket.accept()

            login, password = self.__decodeUserData()
            self.requestConnection.emit(login, password, str(self.__newClientAddress))
            #  self.__Clients.append(threadClient(connection, clientAddress))

        print("Server stopped")

    def addNewClient(self):
        print("client add!")

        # добавляем в список клиентов
        self.__Clients.append(threadClient(self.__newConnection, self.__newClientAddress))

        # информируем об удачной инициализации
        self.sendData(self.__Clients[-1].getSocket(), "Авторизация произведена успешно")

    def lockNewClient(self):
        print("client lock!")

        # информируем об неудачной попытке инициализации
        self.sendData(self.__newConnection, "Неверный логин или пароль!")
        self.__newConnection.close()

    # отправка данных через указанный сокет (кому, что)
    def sendData(self, socket, data):
        if (type(data) == str):
            data = codecs.encode(data, 'UTF-8')

        socket.sendall(data)

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