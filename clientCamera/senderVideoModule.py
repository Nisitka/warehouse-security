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

        self.__work = True

    def run(self):
        self.readImage()
        while self.__work:
            # ждем запроса на изображение
            # self.__socketServer.recv(200)
            try:
                command = self.waitCommand()
                if command == "get":
                    # считываем изображение с камеры
                    self.readImage()

                    # отправляем изображение
                    self.sendImagesData()

            # соединение разорвано
            except:
                print("соединение разорвано")
                self.__work = False

        # закрываем поток
        sys.exit()

    def readImage(self):
        # считываем изображение с камеры
        _, image = self.cap.read()

        self.currentImage = image

    def sendImagesData(self):
        # подгоняем под размер для интерфейса ПО охранника
        # image = cv2.resize(self.currentImage, dsize=(640, 480))

        image = self.currentImage
        cv2.imwrite("img.jpg", image)
        # преобразуем в одномерный numpy массив
        outArr = image.reshape((-1,))

        try:
            self.__socketServer.sendall(outArr)
        # соединение разорвано
        except:
            print("соединение разорвано")

        print("send")

    def waitCommand(self):
        command = self.__socketServer.recv(200)
        return command.decode("utf-8")