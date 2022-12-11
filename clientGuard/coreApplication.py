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

        # повторное подключение к серверу
        self.guiApp.mainWin.repeatConnectServerSignal.connect(self.repeatConnect)

        # инициализируем модуль сетевого соединения
        self.netModule = Socket()
        self.netModule.initUserInfo[bool].connect(self.authorizationUser)
        self.netModule.initCamerasInfo[bool].connect(self.displayInfoCameras)
        self.netModule.importVideoSignal[QPixmap, QPixmap].connect(self.getVideoServer)
        # self.netModule.startAcceptData.connect(self.acceptData)
        self.netModule.disconnectServerSignal.connect(self.eventDisconnectServer)

    def eventDisconnectServer(self):
        self.guiApp.mainWin.eventDisconnectServer()

    def acceptData(self):
        print("start accept data!")
        # запускаем в сетевом модуле принятие видео
        self.netModule.acceptData()

    def displayInfoCameras(self, status):
        if not status:
            print("сигнал интерфейсу об отсутсвии камер")

    def authorizationUser(self, statusKey):
        if (statusKey):
            # открываем главное окно интерфейса
            self.guiApp.showMainWin()
            #
            self.guiApp.mainWin.eventConnectServer()

            # закрываем окно авторизации
            self.guiApp.closeInitUserWin()

        else:
            QMessageBox.about(self.guiApp.initUserWin, "ошибка аутентификации: ", "Неверный логин или пароль!")

    def autheUser(self, host_, port_, login_, password_):
        self.netModule.connectServer(host_, port_, login_, password_)
        try:
            # если удалось подключиться сохраняем для повторного подкл.
            self.host = host_
            self.port = port_
            self.login = login_
            self.password = password_
        except:
            QMessageBox.about(self.guiApp.initUserWin, "ошибка аутентификации: ", "Cервер по такому адресу не запущен!")

    def repeatConnect(self):
        try:
            self.netModule.connectServer(self.host, self.port, self.login, self.password)

        except:
            print("Не удалось повторно подключиться")

    def getVideoServer(self, imagePeople, imageCar):
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