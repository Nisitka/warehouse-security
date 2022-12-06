from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication

# Класс ядра всего приложения
class Core(QObject):
    # signals:
    launch = pyqtSignal() # уведомление об запуске приложения

    def __init__(self, argv):
        QObject.__init__(self)
        self.__app = QApplication(argv)

    def run(self):
        print('application run!')