from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject

from GUI import gui

class Core(QObject):

    def __init__(self, argv):
        QObject.__init__(self)
        self.__app = QApplication(argv)

        self.appGui = gui()

    #   запуск приложения
    def run(self):
        self.appGui.show()

        self.__app.exec_()