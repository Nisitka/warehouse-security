from PyQt5.QtCore import QObject, pyqtSignal

from threading import Thread

class Socket(QObject, Thread):
    # getDataClient = pyqtSignal(str, list)  # сигнал получения данных

    def __init__(self):
        QObject.__init__(self)
        Thread.__init__(self)

        self.__working = True

    def run(self):
        i = 0
        while self.__working:
            i = 1 + 1
            # print("QwE")

        print("Сетевой модуль выключен!")

    def stop(self):
        self.__working = False
        self.join()

