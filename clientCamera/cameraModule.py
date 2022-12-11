from threading import Thread
from PyQt5.QtCore import QObject, pyqtSignal

from PyQt5.QtGui import QImage, QPixmap, QColor

import sys

import cv2

class Camera(QObject, Thread):
    # передаем ядру изображение
    readImageSignal = pyqtSignal(QPixmap)

    def __init__(self):
        QObject.__init__(self)
        Thread.__init__(self)

        # создать новый объект камеру
        self.cap = cv2.VideoCapture(0)
        #self.cap = cv2.VideoCapture('http://192.168.3.9:8080')

        self.__work = True

    def readImage(self):
        return self.__currentImage

    def run(self):
        while self.__work:
            #try:
                # считываем изображение с камеры
                _, image = self.cap.read()
                #print(image)

                self.__currentImage = image
                cv2.imwrite("img.jpg", image)
                pix = QPixmap("img.jpg")

                self.readImageSignal.emit(pix)

            # except:
                #print("Камера не обнаружена")
                #self.__work = False

        sys.exit()
