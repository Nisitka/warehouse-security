from PyQt5.QtCore import QObject, pyqtSignal

from GUI_mainWindow import mainWindow


class Socket(QObject):
    # getDataClient = pyqtSignal(str, list)  # сигнал получения данных

    def __init__(self):
        QObject.__init__(self)

    def run(self):
        while True:
            print("QwE")

