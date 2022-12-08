# GUI.py
'''
Класс, отвечающий за взаимодействие ядра
с интерфейсом приложения
'''

# главное окно
# from mainWindow import guiMainWindow
from GUI_mainWindow import mainWindow

# окно редакции клиента
from clientWindow import guiClientWindow

from PyQt5.QtCore import QObject, pyqtSignal

class guiApplication(QObject):

    def __init__(self):
        QObject.__init__(self)

        # при запуске сразуже открываем главное окно
        self.__mainWin = mainWindow()

        # список с окнами клиентов
        self.__clientWindowList = []

        # тестирование открытия окна клиента
        '''
        for i in range(0, 10):
            self.__clientWindowList.append(guiClientWindow())
        for i in range(0, 10):
            self.showClient(i)
        '''

    def getMainWindow(self):
        return self.__mainWin

    # открытие определенного окна работы с клиентом
    def showClient(self, numberClient):
        self.__clientWindowList[numberClient].show()

