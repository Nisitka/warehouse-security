from GUI import gui
from networkModule import Socket

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap

from PyQt5.QtWidgets import QMessageBox

class Core(QObject):
    # run = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

        # инициализируем интерфейс всего приложения
        self.guiApp = gui()

        #
        self.guiApp.initUserWin.initUserSignal[str, int, str, str].connect(self.autheUser)

        # соединяем сигналы взаимодействия ворот/турникета с ядром
        self.guiApp.openGateSignal.connect(self.openGate)
        self.guiApp.closeGateSignal.connect(self.closeGate)
        self.guiApp.openBarrierSignal.connect(self.openBarrier)
        self.guiApp.closeBarrierSignal.connect(self.closeBarrier)

        # инициализируем модуль сетевого соединения
        self.netModule = Socket()
        self.netModule.initUserInfo[bool].connect(self.authorizationUser)
        self.netModule.importData[QPixmap, QPixmap].connect(self.getDataServer)
        self.netModule.startAcceptVideo.connect(self.acceptVideo)
        self.netModule.disconnectServer.connect(self.eventDisconnectServer)

    def eventDisconnectServer(self):
        self.guiApp.mainWin.eventDisconnectServer()

    def acceptVideo(self):
        print("start accept video!")
        # запускаем модуль сетевого соединения (в отдельном потоке)
        self.netModule.start()

    def authorizationUser(self, key):
        if (key):
            # запускаем модуль сетевого соединения (в отдельном потоке)
            # self.netModule.start()

            # открываем главное окно интерфейса
            self.guiApp.showMainWin()
            # закрываем окно авторизации
            self.guiApp.closeInitUserWin()
        else:
            QMessageBox.about(self.guiApp.initUserWin, "ошибка аутентификации: ", "Неверный логин или пароль!")

    def autheUser(self, host, port, login, password):
        try:
            self.netModule.connectServer(host, port, login, password)
        except:
            QMessageBox.about(self.guiApp.initUserWin, "ошибка аутентификации: ", "Cервер по такому адресу не запущен!")

    def getDataServer(self, imagePeople, imageCar):
        self.guiApp.mainWin.updateVideoBarrier(imagePeople)
        self.guiApp.mainWin.updateVideoCar(imageCar)

    def run(self):
        # открываем окно авторизации пользователя
        self.guiApp.showInitUserWin()
        
    def openGate(self):
        print("Ворота открыты")
        # self.netModule.stop() # !!! тест чтобы быть спокойным

    def closeGate(self):
        print("Ворота закрыты")
        
    def openBarrier(self):
        print("Турникет открыт")

    def closeBarrier(self):
        print("Турникет закрыт")