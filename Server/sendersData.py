from threading import Thread
import socket as socketNetwork
from PyQt5.QtCore import QObject, pyqtSignal

import sys

import cv2

from Client import typeClient

class senderViideo(QObject, Thread):
    disabled = pyqtSignal(str, int)  # информируем об разрыве соединения

    def __init__(self, camera, clientGuard):
        QObject.__init__(self)
        Thread.__init__(self)

        self.cap = camera
        self.__clientGuard = clientGuard

        self.work = True

    def run(self):
        self.sendImagesData()
        while self.work:
            dataUser = self.waitData()
            if (dataUser == "Get"):
                self.sendImagesData()

        # закрываем поток
        sys.exit()

    def sendImagesData(self):
        _, image = self.cap.read()  # потом это будет инфа с сервера
        image = cv2.resize(image, dsize=(640, 480))

        outArr = image.reshape((-1,))

        try:
            self.__clientGuard.getSocket().sendall(outArr)
        except:
            print("соединение разорвано1")
            self.disabled.emit(str(self.__clientGuard.getLoginGuard()), typeClient.Guard.value)

    def waitData(self):
        while True:
            try:
                dataUser = self.__clientGuard.getSocket().recv(200)
                dataUser = dataUser.decode("utf-8")

            except:
                print("соединение разорвано2")
                self.disabled.emit(str(self.__clientGuard.getLoginGuard()), typeClient.Guard.value)

                self.work = False
                return

            if not dataUser:
                break
            else:
                return dataUser