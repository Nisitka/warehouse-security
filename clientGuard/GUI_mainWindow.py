from PyQt5.QtCore import QObject, pyqtSignal

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem

from PyQt5.QtCore import QTimer, QTime

from PyQt5.QtGui import QPalette, QBrush, QPixmap, QColor, QImage

import PyQt5.Qt

import mainWindowUI # конвертированный файл дизайна

from functionGUI import setStyleButton

from entries import Barrier, Gate

class mainWindow(QtWidgets.QWidget, mainWindowUI.Ui_Form):
    openBarrier = pyqtSignal()   # сигнал открытия турникета
    closeBarrier = pyqtSignal()  # сигнал закрытия турникета
    
    openGate = pyqtSignal()   # сигнал открытия ворот
    closeGate = pyqtSignal()  # сигнал закрытия ворот

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self) # для инициализации нашего дизайна
        
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
       
    def setTableHistory(self):
        
        columns = ["ФИО", "Дата и время", "Транспорт"]
        
        self.historyTableWidget.setColumnCount(len(columns))
        self.historyTableWidget.setHorizontalHeaderLabels(columns)
        
        self.historyTableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        
    def updateVideoCar(self, pix):

        d = 0.7
        pix = pix.scaled(pix.width() * d, pix.height() * d)
        self.videoCarLabel.setPixmap(pix)
        
    def updateVideoBarrier(self, pix):

        d = 0.7
        pix = pix.scaled(pix.width() * d, pix.height() * d)
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
            
        
        
        