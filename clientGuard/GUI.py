from PyQt5.QtCore import QObject, pyqtSignal

from GUI_mainWindow import mainWindow

class gui(QObject):
    # getDataClient = pyqtSignal(str, list)  # сигнал получения данных
    openBarrier = pyqtSignal()  # сигнал открытия турникета
    closeBarrier = pyqtSignal() # сигнал закрытия турникета

    def __init__(self):
        QObject.__init__(self)
        
        self.mainWin = mainWindow()     
        
    def openMainWin(self):
        self.mainWin.show()
        
    