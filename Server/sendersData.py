from threading import Thread
import socket as socketNetwork
from PyQt5.QtCore import QObject, pyqtSignal

import cv2

class senderViideo(QObject, Thread):

    def __init__(self, camera, socketGuard):
        QObject.__init__(self)
        Thread.__init__(self)

        self.cap = camera
        self.clientSocket = socketGuard

    def run(self):
        self.sendImagesData()
        while True:
            dataUser = self.waitData()
            if (dataUser == "Get"):
                self.sendImagesData()

    def sendImagesData(self):
        _, image = self.cap.read()  # потом это будет инфа с сервера
        image = cv2.resize(image, dsize=(640, 480))

        outArr = image.reshape((-1,))

        self.clientSocket.sendall(outArr)

    def waitData(self):
        while True:
            dataUser = self.clientSocket.recv(200)
            dataUser = dataUser.decode("utf-8")
            if not dataUser:
                break
            else:
                return dataUser