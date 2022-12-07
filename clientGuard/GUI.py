from PyQt5.QtCore import QObject, pyqtSignal

from GUI_mainWindow import mainWindow
from GUI_initUserWindow import initWindow

class gui(QObject):
    # getDataClient = pyqtSignal(str, list)  # сигнал получения данных
    openBarrierSignal = pyqtSignal()   # сигнал открытия турникета
    closeBarrierSignal = pyqtSignal()  # сигнал закрытия турникета

    openGateSignal = pyqtSignal()   # сигнал открытия ворот
    closeGateSignal = pyqtSignal()  # сигнал закрытия ворот

    def __init__(self):
        QObject.__init__(self)

        self.mainWin = mainWindow()
        self.mainWin.openGate.connect(self.openGate)
        self.mainWin.closeGate.connect(self.closeGate)
        self.mainWin.openBarrier.connect(self.openBarrier)
        self.mainWin.closeBarrier.connect(self.closeBarrier)

        self.initUserWin = initWindow()

    def openGate(self):
        self.openGateSignal.emit()

    def closeGate(self):
        self.closeGateSignal.emit()

    def openBarrier(self):
        self.openBarrierSignal.emit()

    def closeBarrier(self):
        self.closeBarrierSignal.emit()
        
    def showMainWin(self):
        self.mainWin.show()

    def showInitUserWin(self):
        self.initUserWin.show()

    def closeInitUserWin(self):
        self.initUserWin.close()
        
    