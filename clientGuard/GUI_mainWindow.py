from PyQt5.QtCore import QObject, pyqtSignal

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem

from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtCore import QSize

from PyQt5.QtGui import QPalette, QBrush, QPixmap, QColor, QImage

import PyQt5.Qt

import mainWindowUI  # конвертированный файл дизайна

from functionGUI import setStyleButton

from entries import Barrier, Gate

import datetime

class mainWindow(QtWidgets.QWidget, mainWindowUI.Ui_Form):
    openBarrier = pyqtSignal()   # сигнал открытия турникета
    closeBarrier = pyqtSignal()  # сигнал закрытия турникета
    
    openGate = pyqtSignal()   # сигнал открытия ворот
    closeGate = pyqtSignal()  # сигнал закрытия ворот

    # сигнал повторного подключения к серверу
    repeatConnectServerSignal = pyqtSignal()

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # для инициализации нашего дизайна
        
        self.setWindowTitle("securityMaster")
        
        self.timerCurrentTime = QTimer()
        self.timerCurrentTime.timeout.connect(self.updateTime)
        self.timerCurrentTime.start(1000)
        
        # ворота и турникет
        self.barrier = Barrier() 
        self.gate = Gate()         
        
        # 
        setStyleButton(self.openBarrierButton, [200, 0, 0], "Открыть")
        setStyleButton(self.openGateButton,    [200, 0, 0], "Открыть")
        
        # соеденяем кнопки с использованием турникета и ворот
        self.openBarrierButton.clicked.connect(self.useBarrier)
        self.openGateButton.clicked.connect(self.useGate)
        
        palette = QPalette()
        
        palette.setBrush(QPalette.Background, QBrush(QColor(255, 255, 255)))
        self.setPalette(palette)
        
        self.setTableHistory()

        self.d = 0.7

        # кнопка повторного подключения
        self.repeatConnectButton.clicked.connect(self.repeatConnectServer)

        # кнопка "выход"
        self.exitButton.setStyleSheet('''
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

    def eventConnectServer(self):
        self.repeatConnectButton.setEnabled(False)

    def repeatConnectServer(self):
        self.repeatConnectServerSignal.emit()
       
    def setTableHistory(self):
        
        columns = ["ФИО", "Дата и время", "Транспорт"]
        
        self.historyTableWidget.setColumnCount(len(columns))
        self.historyTableWidget.setHorizontalHeaderLabels(columns)
        
        self.historyTableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        
    def updateVideoCar(self, pix):

        pix = pix.scaled(int(pix.width() * self.d), int(pix.height() * self.d))
        self.videoCarLabel.setPixmap(pix)
        
    def updateVideoBarrier(self, pix):

        pix = pix.scaled(int(pix.width() * self.d), int(pix.height() * self.d))
        self.videoPeopleLabel.setPixmap(pix)
        
    def updateTime(self):
        time = QTime.currentTime()
        items = [time.hour(), time.minute(), time.second()]
        for i in range(0, len(items)):
            if (items[i] < 10):
                items[i] = "0" + str(items[i])               
            else:
                items[i] = str(items[i])
        
        self.timeLabel.setText(items[0] + ":" + items[1] + ":" + items[2])
        
    def useBarrier(self):
        if (self.barrier.isOpen()):
            
            self.closeBarrier.emit()
            self.barrier.Close()
            setStyleButton(self.openBarrierButton, [200, 0, 0], "Открыть")
            
        else:
            self.openBarrier.emit()
            self.barrier.Open()
            setStyleButton(self.openBarrierButton, [0, 200, 0], "Закрыть")
            
    def useGate(self):
        if (self.gate.isOpen()):
            
            self.closeGate.emit()
            self.gate.Close()
            setStyleButton(self.openGateButton, [200, 0, 0], "Открыть")
            
        else:
            self.openGate.emit()
            self.gate.Open()
            setStyleButton(self.openGateButton, [0, 200, 0], "Закрыть")

    def __appendInfoWindow(self, text):
        current_date_time = datetime.datetime.now()
        current_time = current_date_time.time()
        self.textInfoServer.append(str(current_time)[0:-7] + ": " + text)

    # сообщаем пользователю об потери соединения
    def eventDisconnectServer(self):
        self.repeatConnectButton.setEnabled(True)

        self.videoPeopleLabel.clear()
        self.videoCarLabel.clear()

        self.gifNoise = QtGui.QMovie("noSiganlGif.gif")
        self.gifNoise.setScaledSize(QSize(int(self.d*640), int(self.d*480)))

        self.videoCarLabel.setMovie(self.gifNoise)
        self.videoPeopleLabel.setMovie(self.gifNoise)

        self.gifNoise.start()

        self.__appendInfoWindow("Соединение с сервером потеряно")