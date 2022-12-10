from PyQt5.QtCore import QObject, pyqtSignal, QSize
from PyQt5 import QtGui, QtWidgets
import initUserWindowUI  # конвертированный файл дизайна

class initWindow(QtWidgets.QWidget, initUserWindowUI.Ui_Form):
    initUserSignal = pyqtSignal(str, int, str, str)  # сигнал запроса авторизации

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # для инициализации нашего дизайна

        self.connectButton.clicked.connect(self.initUser)

        self.setWindowTitle("securityMaster: авторизация")
        size = QSize(490, 365)
        self.setFixedSize(size)

        # гифка для фона
        self.gifNeuron = QtGui.QMovie("neuron.gif")
        self.gifNeuron.setScaledSize(QSize(650, 400))
        self.gifBackgroundLabel.setMovie(self.gifNeuron)
        self.gifBackgroundLabel.setFixedSize(size)
        self.gifNeuron.start()

        # цвет текста в Label's
        style = "color: rgb(97,197,242);"
        self.titleWinLabel.setStyleSheet(style)
        self.hostLabel.setStyleSheet(style)
        self.loginLabel.setStyleSheet(style)
        self.portLabel.setStyleSheet(style)
        self.passwordLabel.setStyleSheet(style)
        self.titleSetNETLabel.setStyleSheet(style)

        # временно для отладки
        self.hostLineEdit.setText('192.168.3.2')
        self.loginLineEdit.setText('Nisitka')
        self.portLineEdit.setText('2323')

        # кнопка "выход"
        self.connectButton.setStyleSheet('''
                                                            QPushButton {
                                                                background-color: rgb(20,20,21); color: rgb(97,197,242);

                                                                border-style: outset;
                                                                border-radius: 3px;
                                                                border-width: 1px;
                                                                border-color: rgb(97,197,242);
                                                            }
                                                            QPushButton:hover {
                                                                background-color : rgb(97,197,242); color: rgb(0,0,0);
                                                                border-color: rgb(0,0,0);
                                                            }
                                                        ''')

    def initUser(self):
        host = self.hostLineEdit.text()
        port = int(self.portLineEdit.text())

        login = self.loginLineEdit.text()
        password = self.passwordLineEdit.text()

        self.initUserSignal.emit(host, port, login, password)