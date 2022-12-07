from PyQt5.QtCore import QObject, pyqtSignal

from threading import Thread

import cv2  # это временно!!!
from PyQt5.QtGui import QImage, QPixmap, QColor

import qimage2ndarray
import numpy

class Socket(QObject, Thread):
    # getDataClient = pyqtSignal(str, list)  # сигнал получения данных
    importData = pyqtSignal(QPixmap, QPixmap)

    def __init__(self):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__working = True

        # создать новый объект камеру
        self.cap = cv2.VideoCapture(0)  # временно!

    def run(self):
        i = 0
        while self.__working:
            i = 1 + 1
            self.getDataServer()

        print("Сетевой модуль выключен!")

    def getDataServer(self):
        # чтение изображения с камеры
        _, image = self.cap.read() # потом это будет инфа с сервера

        h = image.shape[0]
        w = image.shape[1]

        format = QImage.Format_BGR888
        qimage = QImage(image.data, w, h, format) # Format_Indexed8

        pix = QPixmap.fromImage(qimage)
        self.importData.emit(pix, pix)

    def stop(self):
        self.__working = False
        self.join()

