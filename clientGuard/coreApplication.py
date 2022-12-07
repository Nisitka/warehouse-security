from GUI import gui
from networkModule import Socket

from PyQt5.QtCore import QObject, pyqtSignal

class Core(QObject):
    # run = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

        # инициализируем интерфейс всего приложения
        self.guiApp = gui()
        # соединяем сигналы взаимодействия ворот/турникета с ядром
        self.guiApp.openGateSignal.connect(self.openGate)
        self.guiApp.closeGateSignal.connect(self.closeGate)
        self.guiApp.openBarrierSignal.connect(self.openBarrier)
        self.guiApp.closeBarrierSignal.connect(self.closeBarrier)

        # инициализируем модуль сетевого соединения
        self.netModule = Socket()

    def run(self):
        # запускаем модуль сетевого соединения (в отдельном потоке)
        self.netModule.start()

        # открываем главное окно интерфейса
        self.guiApp.openMainWin()
        
    def openGate(self):
        print("Ворота открыты")
        # self.netModule.stop() # !!! тест чтобы быть спокойным

    def closeGate(self):
        print("Ворота закрыты")
        
    def openBarrier(self):
        print("Турникет открыт")

    def closeBarrier(self):
        print("Турникет закрыт")