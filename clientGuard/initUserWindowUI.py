# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Programming\warehouse-security\clientGuard\initUserWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 390)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(40, 40, 511, 301))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titleWinLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.titleWinLabel.setFont(font)
        self.titleWinLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleWinLabel.setObjectName("titleWinLabel")
        self.verticalLayout_3.addWidget(self.titleWinLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.loginLabel.setFont(font)
        self.loginLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.loginLabel.setObjectName("loginLabel")
        self.horizontalLayout.addWidget(self.loginLabel)
        self.loginLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.loginLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loginLineEdit.setFont(font)
        self.loginLineEdit.setObjectName("loginLineEdit")
        self.horizontalLayout.addWidget(self.loginLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.passwordLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.passwordLabel.setObjectName("passwordLabel")
        self.horizontalLayout_2.addWidget(self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.horizontalLayout_2.addWidget(self.passwordLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.titleSetNETLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(15)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.titleSetNETLabel.setFont(font)
        self.titleSetNETLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleSetNETLabel.setObjectName("titleSetNETLabel")
        self.horizontalLayout_5.addWidget(self.titleSetNETLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.hostLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.hostLabel.setFont(font)
        self.hostLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hostLabel.setObjectName("hostLabel")
        self.horizontalLayout_3.addWidget(self.hostLabel)
        self.hostLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.hostLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hostLineEdit.setFont(font)
        self.hostLineEdit.setObjectName("hostLineEdit")
        self.horizontalLayout_3.addWidget(self.hostLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.portLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.portLabel.setFont(font)
        self.portLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.portLabel.setObjectName("portLabel")
        self.horizontalLayout_4.addWidget(self.portLabel)
        self.portLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.portLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.portLineEdit.setFont(font)
        self.portLineEdit.setObjectName("portLineEdit")
        self.horizontalLayout_4.addWidget(self.portLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gifBackgroundLabel = QtWidgets.QLabel(Form)
        self.gifBackgroundLabel.setGeometry(QtCore.QRect(0, 0, 511, 301))
        self.gifBackgroundLabel.setText("")
        self.gifBackgroundLabel.setObjectName("gifBackgroundLabel")
        self.connectButton = QtWidgets.QPushButton(Form)
        self.connectButton.setGeometry(QtCore.QRect(220, 330, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.connectButton.setFont(font)
        self.connectButton.setObjectName("connectButton")
        self.gifBackgroundLabel.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.connectButton.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.titleWinLabel.setText(_translate("Form", "АВТОРИЗАЦИЯ"))
        self.loginLabel.setText(_translate("Form", "Логин:"))
        self.passwordLabel.setText(_translate("Form", "Пароль:"))
        self.titleSetNETLabel.setText(_translate("Form", "Параметры сервера"))
        self.hostLabel.setText(_translate("Form", "IPv4-адрес:"))
        self.portLabel.setText(_translate("Form", "Порт:"))
        self.connectButton.setText(_translate("Form", "Авторизоваться"))
