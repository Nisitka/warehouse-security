from PyQt5 import QtWidgets

# главное окно
import mainWindowGui

from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem

from PyQt5.QtCore import QObject, pyqtSignal

from Client import typeClient

import datetime

class mainWindow(QtWidgets.QMainWindow, mainWindowGui.Ui_Form):
    startServerSignal = pyqtSignal(int, int)  # сигнал для запуска сервера (порт, макс. кол-во клиентов)
    stopServerSignal = pyqtSignal()           # сигнал для остановки сервера

    def __init__(self):
        self.__serverWorking = False

        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле mainWindowGui.py
        super().__init__()
        QObject.__init__(self)
        # для инициализации нашего дизайна
        self.setupUi(self)

        # сигналы и слоты
        self.StartStopPushButton.clicked.connect(self.__toRunningServer)

        # доп. настройки интерфейса
        self.__setBackground()
        self.__setTabBar()
        self.__setServer()
        self.__setGuardClients()
        self.__setCamerasClients()
        self.__setNeuralNet()
        self.__setToolBoxSettings()

    def delClient(self, login, type):
        print(str(login) + " " + str(type))

        # выбираем таблицу
        if (type == typeClient.Guard.value):
            table = self.guardsTableWidget

        # находим строку с эти логином и очищаем её
        row = 0
        while row <= table.rowCount():
            if table.item(row, 0).text() == login:
                table.removeRow(row)
                break
            row += 1

        self.__appendInfoWindow("Соединение с клиентом \"" + login + "\" разорвано")

    # установка фона
    def __setBackground(self):
        self.setWindowTitle("Server neural network")
        self.setFixedSize(610, 540)

        '''
        palette = QPalette()
        pixFon = QPixmap("fon.jpg")
        palette.setBrush(QPalette.Background, QBrush(pixFon))
        self.setPalette(palette)
        '''

        #  гифка для сервера
        self.gifFon = QtGui.QMovie("particle-background.gif")
        self.gifFon.setScaledSize(self.size())
        self.gifFonLabel.setMovie(self.gifFon)
        self.gifFon.start()

    # установка визуала бара табов
    def __setTabBar(self):
        styleSheet = """
                QTabBar::tab {
                    border: 2px solid #C4C4C3;
                    border-bottom-color: #C2C7CB;
                    border-top-left-radius: 12px;
                    border-top-right-radius: 12px;
                    min-width: 32ex;  
                    padding: 2px;

                    color: rgb(0,0,0);
                }

                QTabBar::tab:selected {
                    background: #FFFFFF;
                    color: rgb(0,0,0);
                }

                QTabBar::tab:hover {
                    background: white;
                    color: rgb(0,0,0);
                }

                QTabBar::tab:selected {
                    border-bottom-color: white;
                    color: rgb(0,0,0);
                }

                QTabBar::tab:!selected {
                    margin-top: 3px;
                    color: rgb(97,197,242);
                }
                """

        self.TabWidgetApp.setStyleSheet(styleSheet)

    def __toRunningServer(self):
        if (self.__serverWorking):
            self.stopServer()
        else:
            self.__startServer()

        self.__setStartButton()

    def __setToolBoxSettings(self):
        self.settingsToolBox.setStyleSheet("""
                 QToolBox::tab {
                    background: rgb(0,0,0);
                    color: white;
                 }
                 QToolBox::tab:hover {
                    background: rgb(0,0,0);
                    color: rgb(97,197,242);
                 }
                 QToolBox::tab:selected { /* italicize selected tabs */
                    background: rgb(97,197,242);
                    color: rgb(0,0,0);
                    font: bold;
                 }
                """)

    def addNewClient(self, login, address, tClient):

        if (tClient == typeClient.Guard.value):
            self.__addGuardToTable(login, address)
        else:
            self.__addCameraToTable(login, address)

        self.__appendInfoWindow("Подключен новый клиент (" + login + ")")

    def __addCameraToTable(self, login, address):
        self.camersTableWidget.setRowCount(self.camersTableWidget.rowCount() + 1)

        self.camersTableWidget.setItem(self.camersTableWidget.rowCount() - 1, 0, QTableWidgetItem(login))
        self.camersTableWidget.setItem(self.camersTableWidget.rowCount() - 1, 1, QTableWidgetItem(address))

    def __addGuardToTable(self, login, address):
        self.guardsTableWidget.setRowCount(self.guardsTableWidget.rowCount() + 1)

        self.guardsTableWidget.setItem(self.guardsTableWidget.rowCount() - 1, 0, QTableWidgetItem(login))
        self.guardsTableWidget.setItem(self.guardsTableWidget.rowCount() - 1, 1, QTableWidgetItem(address))

    def __clearClientsTable(self):
        while (self.guardsTableWidget.rowCount() > 0):
            self.guardsTableWidget.removeRow(0)

        while (self.camersTableWidget.rowCount() > 0):
            self.camersTableWidget.removeRow(0)

    def setInfoServer(self, nameHost, IP):
        # установить пар-ры сокета сервера
        self.hostLabel.setText("Хост: " + nameHost)
        self.IPLabel.setText("IPv4-адрес: " + IP)

        # выдать информацию в инф. табло
        self.__appendInfoWindow("Сервер запущен")

    def __clearInfoServer(self):
        # стереть пар-ры сокета сервера
        self.hostLabel.setText("Хост: ")
        self.IPLabel.setText("IPv4-адрес: ")

        # выдать информацию в инф. табло
        self.__appendInfoWindow("Сервер выключен")

    def __appendInfoWindow(self, text):
        current_date_time = datetime.datetime.now()
        current_time = current_date_time.time()
        self.textInfoServer.append(str(current_time)[0:-7] + ": " + text)

    def __startServer(self):
        self.__serverWorking = True

        self.startServerSignal.emit(int(self.portLineEdit.text()), int(self.numClientsLineEdit.text()))

        self.gifServer.start()
        self.gifServer.jumpToFrame(0)

        # блокировка полей для ввода пар-ов сервера
        self.portLineEdit.setEnabled(False)
        self.numClientsLineEdit.setEnabled(False)

        # разблокирование таблицы с клиентами
        self.guardsTableWidget.setEnabled(True)

    def stopServer(self):
        self.__serverWorking = False

        self.stopServerSignal.emit()

        self.gifServer.jumpToFrame(0)
        self.gifServer.stop()

        # очистка информации об хосте и адресе клиента
        self.__clearInfoServer()

        # разблокировка полей для ввода пар-ов сервера
        self.portLineEdit.setEnabled(True)
        self.numClientsLineEdit.setEnabled(True)

        # очистка полей таблицы от клиентов и блокировка таблицы
        self.__clearClientsTable()
        self.guardsTableWidget.setEnabled(False)

    # установка визуала кнопки запуска\остановки сервера
    def __setStartButton(self):
        if (not self.__serverWorking):
            self.StartStopPushButton.setText("старт")
            self.StartStopPushButton.setStyleSheet('''
                                            QPushButton {
                                                background-color: rgb(78,198,26); color: rgb(9,100,24);

                                                border-style: outset;
                                                border-radius: 5px;
                                                border-width: 1px;
                                                border-color: rgb(0,0,0);
                                            }
                                            QPushButton:hover {
                                                background-color : rgb(98,218,46); color: rgb(29,120,44);
                                                border-color: rgb(0,0,0);
                                            }
                                        ''')
        else:
            self.StartStopPushButton.setText("стоп")
            self.StartStopPushButton.setStyleSheet('''
                                            QPushButton {
                                                background-color: rgb(204,0,0); color: rgb(104,0,0);

                                                border-style: outset;
                                                border-radius: 5px;
                                                border-width: 1px;
                                                border-color: rgb(0,0,0);
                                            }
                                            QPushButton:hover {
                                                background-color : rgb(224,0,0); color: rgb(104,0,0);
                                                border-color: rgb(0,0,0);
                                            }
                                        ''')

    # установка визула сервера
    def __setServer(self):
        # порт сервера по умолчанию
        self.portLineEdit.setText("2323")

        # макс. кол-во подключений
        self.numClientsLineEdit.setText("5")

        # кнопка сервера
        self.__setStartButton()

        #  гифка для сервера
        self.gifServer = QtGui.QMovie("stp.gif")
        self.gifServer.setScaledSize(QSize(130, 130))
        self.gifServerLabel.setMovie(self.gifServer)
        self.gifServer.start()
        self.gifServer.jumpToFrame(2)
        self.gifServer.stop()

        # кнопка "отсоединить всех" в клиентах охраны
        self.closeAllGuardClientButton.setStyleSheet('''
                                            QPushButton {
                                                background-color: rgb(255,255,255); color: rgb(0,0,0);

                                                border-style: outset;
                                                border-radius: 3px;
                                                border-width: 1px;
                                                border-color: rgb(0,0,0);
                                            }
                                            QPushButton:hover {
                                                background-color : rgb(224,0,0); color: rgb(104,0,0);
                                                border-color: rgb(0,0,0);
                                            }
                                        ''')

    # установка визуала клиентов-охранников
    def __setGuardClients(self):
        self.guardsTableWidget.setColumnCount(2)
        self.guardsTableWidget.setHorizontalHeaderLabels(["Логин охранника", "Адрес"])
        self.guardsTableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

        # блокировка таблицы до включения сервера
        self.guardsTableWidget.setEnabled(False)

    def __setCamerasClients(self):
        self.camersTableWidget.setColumnCount(2)
        self.camersTableWidget.setHorizontalHeaderLabels(["Логин камеры", "Адрес"])
        self.camersTableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

        # блокировка таблицы до включения сервера
        self.guardsTableWidget.setEnabled(False)

    def __setNeuralNet(self):
        #  гифка для нейронной сети
        '''
        self.__gifNeuron = QtGui.QMovie("neuron.gif")
        self.__gifNeuron.setScaledSize(QSize(400, 200))
        self.neuronGifLabel.setMovie(self.__gifNeuron)
        self.__gifNeuron.start()
        '''