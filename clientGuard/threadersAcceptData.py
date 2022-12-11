from PyQt5.QtCore import QObject, pyqtSignal

from threading import Thread

import pickle
from packerData import Packer

class receiverData(QObject, Thread):
    # сообщаем ядру о потери соединения


    def __init__(self, socket):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__Socket = socket

        self.hVideo = 480
        self.wVideo = 640
        self.dataPackageSize = self.hVideo * self.wVideo * 3

        self.__working = True

    def run(self):
        while self.__working:
            self.getDataServer()

        print("Принятие изображений прекращено!")
        sys.exit()

    def getDataServer(self):
        try:
            dataBits = self.__Socket.recv(self.dataPackageSize * 2)

        except:
            print("соединение с сервером потеряно!")
            # сообщаем ядру об потери соединения
            self.disconnectServer.emit()

            # прекращаем получение данных
            self.__working = False