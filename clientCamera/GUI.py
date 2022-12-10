from PyQt5.QtCore import QObject, pyqtSignal

from PyQt5.QtGui import QImage, QPixmap, QColor
from PyQt5 import QtGui, QtWidgets
import guiUI  # конвертированный файл дизайна

import datetime

class gui(QtWidgets.QWidget, guiUI.Ui_Form):
    # отправка данных для соединения в ядро приложения (адрес, порт, UID камеры, ключ)
    connectServerSignal = pyqtSignal(str, int, str, str)
    disconnectSignal = pyqtSignal()

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле guiUI.py
        super().__init__()
        QObject.__init__(self)
        # для инициализации нашего дизайна
        self.setupUi(self)

        # настройки визула
        self.setWindowTitle("client-camera")

        self.connectButton.clicked.connect(self.connectServer)
        self.disconnectButton.clicked.connect(self.disconnect)

        self.disconnectButton.setEnabled(False)

        self.hostLineEdit.setText("192.168.3.2")
        self.portLineEdit.setText("2323")
        self.keyLineEdit.setText("F31415926")  # "F31415926"
        self.cameraLineEdit.setText("northCamera")

    def showConnectServer(self, status):
        if status:
            self.addInfo("Выполнено подключение к серверу.")
            self.connectButton.setEnabled(False)
            self.disconnectButton.setEnabled(True)

        else:
            self.addInfo("Ошибка подключения к серверу.")
            self.connectButton.setEnabled(True)
            self.disconnectButton.setEnabled(False)

    def disconnect(self):
        self.disconnectSignal.emit()

    def showDisabledConnect(self):
        self.addInfo("Соединение с сервером потеряно")
        self.connectButton.setEnabled(True)
        self.disconnectButton.setEnabled(False)

    def addInfo(self, text):
        current_date_time = datetime.datetime.now()
        current_time = current_date_time.time()
        self.infoTextEdit.append(str(current_time)[0:-7] + ": " + text)

    def setShot(self, pix):
        self.shotLabel.setPixmap(pix)

    def connectServer(self):
        self.connectServerSignal.emit(self.hostLineEdit.text(),
                                      int(self.portLineEdit.text()),
                                      self.cameraLineEdit.text(),
                                      self.keyLineEdit.text())