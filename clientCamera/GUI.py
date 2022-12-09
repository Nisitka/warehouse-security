from PyQt5.QtCore import QObject, pyqtSignal

from PyQt5 import QtGui, QtWidgets
import guiUI  # конвертированный файл дизайна

class gui(QtWidgets.QWidget, guiUI.Ui_Form):

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле guiUI.py
        super().__init__()
        QObject.__init__(self)
        # для инициализации нашего дизайна
        self.setupUi(self)

        # настройки визула
        self.setWindowTitle("client-camera")