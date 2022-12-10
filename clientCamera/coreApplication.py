from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject

from GUI import gui
from PyQt5.QtGui import QImage, QPixmap, QColor

from networkModule import Socket

from cameraModule import Camera

class Core(QObject):

    def __init__(self, argv):
        QObject.__init__(self)
        self.__app = QApplication(argv)

        self.appGui = gui()
        self.appGui.connectServerSignal[str, int, str, str].connect(self.connectServer)
        self.appGui.disconnectSignal.connect(self.disconnectServer)

        # создаем камеру
        self.camera = Camera()
        self.camera.readImageSignal[QPixmap].connect(self.updateShotGUI)
        # запускаем считывание изображения
        self.camera.start()

        self.netModule = Socket(self.camera)
        self.netModule.resultConnect[bool].connect(self.showConnectServerInfo)
        self.netModule.disabledConnectSignal.connect(self.disabledConnectServer)



    def showConnectServerInfo(self, status):
        self.appGui.showConnectServer(status)

    def disabledConnectServer(self):
        self.appGui.showDisabledConnect()

    def updateShotGUI(self, newShot):
        self.appGui.setShot(newShot)

    def connectServer(self, host, port, login, key):
        self.netModule.connectServer(host, port, login, key)

    def disconnectServer(self):
        self.netModule.disconnect()

    #   запуск приложения
    def run(self):
        self.appGui.show()

        self.__app.exec_()