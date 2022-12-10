from threading import Thread
import socket as socketNetwork
from PyQt5.QtCore import QObject, pyqtSignal

import sys

import cv2

class senderVideo(QObject, Thread):
    disabled = pyqtSignal()  # информируем об разрыве соединения

    def __init__(self, socketServer, camera):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__camera = camera

        self.hVideo = 480
        self.wVideo = 640

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
                self.disabled.emit()
                self.__work = False

        # закрываем поток
        sys.exit()

    def readImage(self):
        # считываем изображение с камеры
        self.currentImage = self.__camera.readImage()

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
            self.disabled.emit()

        print("send")

    def waitCommand(self):
        command = self.__socketServer.recv(200)
        return command.decode("utf-8")