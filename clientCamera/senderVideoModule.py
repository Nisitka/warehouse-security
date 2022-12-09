from threading import Thread
import socket as socketNetwork
from PyQt5.QtCore import QObject, pyqtSignal

import sys

import cv2

class senderVideo(QObject, Thread):
    disabled = pyqtSignal(str, int)  # информируем об разрыве соединения

    def __init__(self, socketServer):
        QObject.__init__(self)
        Thread.__init__(self)

        self.hVideo = 480
        self.wVideo = 640

        # создать новый объект камеру
        self.cap = cv2.VideoCapture(0)

        self.__socketServer = socketServer

        self.work = True

    def run(self):
        self.sendImagesData()
        while self.work:
            # ждем инфы об принятии файла
            dataServer = self.waitData()
            if (dataServer == "Get"):
                self.sendImagesData()

        # закрываем поток
        sys.exit()

    def sendImagesData(self):
        # считываем изображение с камеры
        _, image = self.cap.read()

        # подгоняем под размер для интерфейса ПО охранника
        image = cv2.resize(image, dsize=(640, 480))

        # преобразуем в одномерный numpy массив
        outArr = image.reshape((-1,))

        try:
            self.__socketServer.send(outArr)
        # соединение разорвано
        except:
            print("соединение разорвано")

        print("send")

    def waitData(self):
        while True:
            try:
                dataServer = self.__socketServer.recv(200)
                dataServer = dataServer.decode("utf-8")
                print(dataServer)
            # соединение разорвано
            except:
                print("соединение разорвано")

                self.work = False
                return

            if not dataServer:
                break
            else:
                return dataServer