# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\18-belousov.n.d\Documents\Diplom\Progarms\Python\security\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1382, 676)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.mainhLayout = QtWidgets.QHBoxLayout()
        self.mainhLayout.setObjectName("mainhLayout")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.timeLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout_13.addWidget(self.timeLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_13.addItem(spacerItem)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.CPPLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.CPPLabel.setFont(font)
        self.CPPLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CPPLabel.setObjectName("CPPLabel")
        self.verticalLayout.addWidget(self.CPPLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.videoPeopleLabel = QtWidgets.QLabel(self.widget)
        self.videoPeopleLabel.setObjectName("videoPeopleLabel")
        self.horizontalLayout.addWidget(self.videoPeopleLabel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.openBarrierButton = QtWidgets.QPushButton(self.widget)
        self.openBarrierButton.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.openBarrierButton.setFont(font)
        self.openBarrierButton.setObjectName("openBarrierButton")
        self.horizontalLayout_4.addWidget(self.openBarrierButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.GateLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.GateLabel.setFont(font)
        self.GateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GateLabel.setObjectName("GateLabel")
        self.verticalLayout_4.addWidget(self.GateLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.videoCarLabel = QtWidgets.QLabel(self.widget)
        self.videoCarLabel.setObjectName("videoCarLabel")
        self.horizontalLayout_2.addWidget(self.videoCarLabel)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.openGateButton = QtWidgets.QPushButton(self.widget)
        self.openGateButton.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.openGateButton.setFont(font)
        self.openGateButton.setObjectName("openGateButton")
        self.horizontalLayout_3.addWidget(self.openGateButton)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.mainhLayout.addLayout(self.verticalLayout_13)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem14 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem14)
        self.historyTitleLabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.historyTitleLabel.setFont(font)
        self.historyTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.historyTitleLabel.setObjectName("historyTitleLabel")
        self.horizontalLayout_10.addWidget(self.historyTitleLabel)
        spacerItem15 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem15)
        self.verticalLayout_12.addLayout(self.horizontalLayout_10)
        self.historyTableWidget = QtWidgets.QTableWidget(self.widget)
        self.historyTableWidget.setObjectName("historyTableWidget")
        self.historyTableWidget.setColumnCount(0)
        self.historyTableWidget.setRowCount(0)
        self.verticalLayout_12.addWidget(self.historyTableWidget)
        self.mainhLayout.addLayout(self.verticalLayout_12)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem16 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem16)
        self.peopleNameLabel = QtWidgets.QLabel(self.page)
        self.peopleNameLabel.setMinimumSize(QtCore.QSize(290, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.peopleNameLabel.setFont(font)
        self.peopleNameLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.peopleNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.peopleNameLabel.setObjectName("peopleNameLabel")
        self.horizontalLayout_11.addWidget(self.peopleNameLabel)
        spacerItem17 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem17)
        self.verticalLayout_22.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem18)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem19)
        self.photoPeopleLabel = QtWidgets.QLabel(self.page)
        self.photoPeopleLabel.setObjectName("photoPeopleLabel")
        self.horizontalLayout_7.addWidget(self.photoPeopleLabel)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem20)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem21)
        self.horizontalLayout_8.addLayout(self.verticalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.statusTitleLabel = QtWidgets.QLabel(self.page)
        self.statusTitleLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.statusTitleLabel.setFont(font)
        self.statusTitleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusTitleLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.statusTitleLabel.setObjectName("statusTitleLabel")
        self.horizontalLayout_5.addWidget(self.statusTitleLabel)
        self.statusValueLabel = QtWidgets.QLabel(self.page)
        self.statusValueLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.statusValueLabel.setFont(font)
        self.statusValueLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statusValueLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.statusValueLabel.setObjectName("statusValueLabel")
        self.horizontalLayout_5.addWidget(self.statusValueLabel)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.numPhoneTitleLabel = QtWidgets.QLabel(self.page)
        self.numPhoneTitleLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numPhoneTitleLabel.setFont(font)
        self.numPhoneTitleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.numPhoneTitleLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numPhoneTitleLabel.setObjectName("numPhoneTitleLabel")
        self.horizontalLayout_6.addWidget(self.numPhoneTitleLabel)
        self.numPhoneValueLabel = QtWidgets.QLabel(self.page)
        self.numPhoneValueLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.numPhoneValueLabel.setFont(font)
        self.numPhoneValueLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.numPhoneValueLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.numPhoneValueLabel.setObjectName("numPhoneValueLabel")
        self.horizontalLayout_6.addWidget(self.numPhoneValueLabel)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem22)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_22.addLayout(self.horizontalLayout_8)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        spacerItem23 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem23)
        self.carNameLabel = QtWidgets.QLabel(self.page_2)
        self.carNameLabel.setMinimumSize(QtCore.QSize(290, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.carNameLabel.setFont(font)
        self.carNameLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.carNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.carNameLabel.setObjectName("carNameLabel")
        self.horizontalLayout_24.addWidget(self.carNameLabel)
        spacerItem24 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem24)
        self.verticalLayout_21.addLayout(self.horizontalLayout_24)
        spacerItem25 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_21.addItem(spacerItem25)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.userTitleLabel = QtWidgets.QLabel(self.page_2)
        self.userTitleLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userTitleLabel.setFont(font)
        self.userTitleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.userTitleLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userTitleLabel.setObjectName("userTitleLabel")
        self.horizontalLayout_27.addWidget(self.userTitleLabel)
        self.userValueLabel = QtWidgets.QLabel(self.page_2)
        self.userValueLabel.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userValueLabel.setFont(font)
        self.userValueLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.userValueLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.userValueLabel.setObjectName("userValueLabel")
        self.horizontalLayout_27.addWidget(self.userValueLabel)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem26)
        self.verticalLayout_20.addLayout(self.horizontalLayout_27)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem27)
        self.verticalLayout_21.addLayout(self.verticalLayout_20)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem28 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem28)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem29)
        self.photoCarLabel = QtWidgets.QLabel(self.page_2)
        self.photoCarLabel.setObjectName("photoCarLabel")
        self.horizontalLayout_26.addWidget(self.photoCarLabel)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem30)
        self.verticalLayout_11.addLayout(self.horizontalLayout_26)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem31)
        self.verticalLayout_21.addLayout(self.verticalLayout_11)
        self.stackedWidget.addWidget(self.page_2)
        self.mainhLayout.addWidget(self.stackedWidget)
        self.horizontalLayout_12.addLayout(self.mainhLayout)
        self.horizontalLayout_13.addWidget(self.widget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.timeLabel.setText(_translate("Form", "12:57:23"))
        self.CPPLabel.setText(_translate("Form", "КПП"))
        self.videoPeopleLabel.setText(_translate("Form", "TextLabel"))
        self.openBarrierButton.setText(_translate("Form", "barrier"))
        self.GateLabel.setText(_translate("Form", "Ворота"))
        self.videoCarLabel.setText(_translate("Form", "TextLabel"))
        self.openGateButton.setText(_translate("Form", "Gate"))
        self.historyTitleLabel.setText(_translate("Form", "история посещений"))
        self.peopleNameLabel.setText(_translate("Form", "Белоусов Никита Дмитриевич"))
        self.photoPeopleLabel.setText(_translate("Form", "TextLabel"))
        self.statusTitleLabel.setText(_translate("Form", "Должность:"))
        self.statusValueLabel.setText(_translate("Form", "Уборщик"))
        self.numPhoneTitleLabel.setText(_translate("Form", "Номер телефона:"))
        self.numPhoneValueLabel.setText(_translate("Form", "+7 (923) 374 01 25"))
        self.carNameLabel.setText(_translate("Form", "номер и марка авто"))
        self.userTitleLabel.setText(_translate("Form", "Владелец:"))
        self.userValueLabel.setText(_translate("Form", "Белоусов Никита Дмитриевич"))
        self.photoCarLabel.setText(_translate("Form", "TextLabel"))
