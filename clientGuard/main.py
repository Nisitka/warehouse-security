import sys  # sys нужен для передачи argv в QApplication

from PyQt5 import QtWidgets

from coreApplication import Core


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication

    securityMaster = Core()
    securityMaster.run()

    app.exec_()  # и запускаем приложение