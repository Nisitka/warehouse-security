from PyQt5 import QtWidgets

# главное окно
import clientWindowGui

from PyQt5.QtGui import QPalette, QBrush, QPixmap

class guiClientWindow(QtWidgets.QMainWindow, clientWindowGui.Ui_Form):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле clientWindowGui.py
        super().__init__()
        # для инициализации нашего дизайна
        self.setupUi(self)
