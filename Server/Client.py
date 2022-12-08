from PyQt5.QtCore import QObject, pyqtSignal
from threading import Thread

import datetime
import codecs

class threadClient(QObject, Thread):
    # при получении данных
    getData = pyqtSignal(list, str)  # отправка принятого массива данных и комментария

    hVideo = 480
    wVideo = 640
    dataPackageSize = hVideo * wVideo * 3
    # dataPackageSize = 2048 * 1000 * 1000

    def __init__(self, socket_, address_, loginGuard):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__loginGuard = loginGuard

        self.__socket = socket_
        self.__address = address_

        self.__working = False
        self.__init = False

        # как только создаем клиента сразу же запускаем поток на принятие данных
        self.start()

    def run(self):
        self.__working = True

        self.__waitData()

    def getSocket(self):
        return self.__socket

    def __stopGetData(self):
        self.__working = False

    def __waitData(self):
        while(self.__working):
            data = self.__socket.recv(self.dataPackageSize)

            if not data:
                print("данные не переданы!")

    def remove(self):
        self.__stopGetData()
        self.__socket.close()

        print("Клиент удален!!!!!")

    def getLoginGuard(self):
        return self.__loginGuard
