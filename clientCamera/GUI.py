from PyQt5.QtCore import QObject, pyqtSignal

from PyQt5 import QtGui, QtWidgets
import guiUI  # конвертированный файл дизайна

class gui(QtWidgets.QWidget, guiUI.Ui_Form):
    connectServerSignal = pyqtSignal(str)

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле guiUI.py
        super().__init__()
        QObject.__init__(self)
        # для инициализации нашего дизайна
        self.setupUi(self)

        # настройки визула
        self.setWindowTitle("client-camera")

        self.pushButton.clicked.connect(self.connectServer)
        self.lineEdit.setText("192.168.3.2")

    def connectServer(self):
        self.connectServerSignal.emit(self.lineEdit.text())