# Сердце всего приложения, все взаимодействие
# между компонетами определется здесь

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# интерфейс
from GUI import guiApplication
# сервер
from Server import Server
# база данных
from DataBase import dataBase

class Core(QObject):

    def __init__(self, argv):
        QObject.__init__(self)

        self.__app = QApplication(argv)

        # инициализация опций интерфейса
        self.__gui = guiApplication()

        # инициализация базы данных
        self.__DataBase = dataBase()

        # Логика взаимодействия всех компонентов:
        # сигналы компонентов соединяются с методами ядра, в которых вызываются методы компонент,
        # связанных с соответствующим сигналом
        self.__gui.getMainWindow().startServerSignal[int, int].connect(self.startServer)
        self.__gui.getMainWindow().stopServerSignal.connect(self.stopServer)

        # ответы базы данных на запрос от сервера
        self.__DataBase.authorizationClient[str, str].connect(self.__authorizationClient)
        self.__DataBase.blockingClient.connect(self.__blockingClient)

    def startServer(self, port, numClients):
        # при каждом запуске создается новый объект класса сервер,
        # который запускается в отдельном потоке
        self.__server = Server()

        # при успешном запуске сокета сервера, пройдет сигнал об имени хоста и адресе
        self.__server.runServer[str, str].connect(self.setInfoServerGUI)

        # запускаем сокет на определенном порте с огр. кол-ом клиентов
        self.__server.run(port, numClients)

        # сокет запрашивает разрешение на поключение клиента
        self.__server.getSocket().requestConnection[str, str, str].connect(self.initClient)

    def __authorizationClient(self, name, address):
        self.__server.getSocket().addNewClient()
        self.__gui.getMainWindow().addNewClient(name, address)

    def __blockingClient(self):
        self.__server.getSocket().lockNewClient()

    def initClient(self, login, password, address):
        print("инициализация клиента")
        self.__DataBase.initClient(login, password, address)

    def setInfoServerGUI(self, nameHost, IP):
        self.__gui.getMainWindow().setInfoServer(nameHost, IP)

    def stopServer(self):
        self.__server.stop()

    #   запуск ядра приложения
    def run(self):
        self.__gui.getMainWindow().show()
        self.__app.exec_()
