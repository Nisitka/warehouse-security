from PyQt5.QtGui import QImage, QPixmap, QColor

class test:

    def __init__(self, command_, data_):
        self.command = str(command_)
        self.data = data_

    def getData(self):
        return self.data

    def getCommand(self):
        return self.command