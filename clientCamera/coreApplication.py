from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject

from GUI import gui

from networkModule import Socket

class Core(QObject):

    def __init__(self, argv):
        QObject.__init__(self)
        self.__app = QApplication(argv)

        self.appGui = gui()

        self.netModule = Socket()

        self.appGui.connectServerSignal[str].connect(self.connectServer)

    def connectServer(self, host):
        self.netModule.connectServer(host, 2323, "Camera1", "F31415926")

    #   запуск приложения
    def run(self):
        self.appGui.show()

        self.__app.exec_()