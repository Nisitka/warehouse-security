from PyQt5.QtCore import QObject, pyqtSignal

import sqlite3
from sqlite3 import Error

from Client import typeClient

class dataBase(QObject):

    authorizationClient = pyqtSignal(str, str, int)
    blockingClient = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)

        connection = self.createСonnection("serverDatabase.db")
        q = "SELECT name from users;"
        strData = str(self.execute_read_query(connection, q))

        print(strData)

    # подключение к бд через путь/имя файла *.db
    def createСonnection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")

        return connection

    def execute_query(self, connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_read_query(self, connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    # инициализация клиента в базе данных
    def initClient(self, login, password, address):
        print("инициализация в базе данных")

        # при получении особого шифра вместо пароля мы понимаем что это камера
        if password == "f8o13_vn2fk84ds_43f":
            print("присоединение камеры!")
            self.authorizationClient.emit(login, address, typeClient.Guard.value)

        else:
            print("присоединение охранника!")
            if (password == "123"):
                self.authorizationClient.emit(login, address, typeClient.Guard.value)
            else:
                self.blockingClient.emit()