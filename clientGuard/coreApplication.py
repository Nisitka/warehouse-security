from GUI import gui
from networkModule import Socket

from PyQt5.QtCore import QObject, pyqtSignal, QThread

class Core(QObject):
    run = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

        self.guiApp = gui()

        self.socket = Socket()
        self.threadSocket = QThread()
        self.threadSocket.start()
        self.socket.moveToThread(self.threadSocket)

        self.run.connect(self.socket.run)

    def run(self):
        self.run()

        self.guiApp.openMainWin()
        
    def openGate(self):
        print("Ворота открыты")
        
    def openBarrier(self):
        print("Турникет открыт")