import sqlite3
import hashlib

class DataBase:

    def __init__(self, dirDataBase):
        self.connection, self.cursor = self.connectionOpen(dirDataBase)

    def connectionOpen(self, dir='db.sqlite3'):
        try:
            connection = sqlite3.connect(dir)  # подключение к бд
            cursor = connection.cursor()

            return connection, cursor

        except:
            print("Не удалось подключиться к БД")

    def connectionClose(self):
        self.cursor.close()
        self.connection.close()

    
    def array_creator(self, array_of_values):  # функция перегона кортежа в массив 
        temp_storage = array_of_values
        array_of_values = []
        for value in temp_storage:
            array_of_values += [value[0]]

        return array_of_values


    def getCarsNumbers(self):  # функция для вывода всех автомобильных номеров
        self.cursor.execute('SELECT NUMBER FROM CAR')
        cars_numbers = self.cursor.fetchall()
        cars_numbers = self.array_creator(cars_numbers)
        
        return cars_numbers  # выводится из бд в обратном порядке, от последних к первым


    def getDataOfCar(self, car_number):  # вывод сведений об автомобиле по его номеру
        self.cursor.execute('SELECT CAR.PHOTO, PEOPLES.NAME FROM CAR JOIN PEOPLES ON CAR.ID_OWNER = PEOPLES.ID WHERE NUMBER=?', (car_number, ))
        car_data = self.cursor.fetchone()
        return car_data  # данные в форме кортежа (путь_к_фото_авто, ФИО)


    def getDataOfPeople(self, people_id):  # вывод сведений о человеке по его id
        self.cursor.execute('SELECT PHOTO, NAME, STATUS FROM PEOPLES WHERE ID=?', (people_id, ))
        people_data = self.cursor.fetchone()
        return people_data  # данные в форме кортежа (путь_к_фото_человека, ФИО, должность)


    def addVisit(self,status_car, people_id, datetime): # функция добавления посещений
        try:
            self.cursor.execute('INSERT INTO VISITS (ID_PEOPLE, IS_CAR, DATETIME) VALUES (?, ?, ?)', (people_id, status_car, datetime, ))
            self.connection.commit()
            return True
        except:
            return False

    def getAllVisits(self):  # функция для вывода всех посещений
        self.cursor.execute('SELECT PEOPLES.NAME, VISITS.DATETIME, VISITS.IS_CAR FROM VISITS JOIN PEOPLES ON VISITS.ID_PEOPLE=PEOPLES.ID ORDER BY DATETIME')
        visits = self.cursor.fetchall()
    
        visits_objects_list = []
        for vis in visits:
            vis = visit(vis[0], vis[1], vis[2])
            visits_objects_list += [vis]
        return visits_objects_list

    def isAuthenticate(self, login, password):  # функция для проверки правильности аутентификации
        try:
            self.cursor.execute('SELECT PASSWORD FROM SECURITIES WHERE LOGIN=?', (login, ))
            password_db = self.cursor.fetchall()[0][0]
            password = password.encode()
            password = hashlib.md5(password)
            password = password.hexdigest()
            if password_db == password:
                return True
            else:
                return False
        except:
            return False

    def cameraSelect(self, security_id):  # функция для выборки id камер по id охранника (сначала камера ворот, потом- шлагбаума), можно обратиться по индексам 0 и 1 соответственно
        self.cursor.execute('SELECT ID_GATE_CAMERA, ID_BARRIER_CAMERA  FROM SECURITIES WHERE ID=?', (security_id, ))
        cameras = self.cursor.fetchall()
        return cameras


    def addSecurity(self, lastname, firstname, patronym, login, password, id_gate_camera, id_barrier_camera):  # функция для добавления охранника
        try:
            password = password.encode()
            password = hashlib.md5(password)
            password = password.hexdigest()
            self.cursor.execute('INSERT INTO SECURITIES (LASTNAME, FIRSTNAME, PATHRONYM, LOGIN, PASSWORD, ID_GATE_CAMERA, ID_BARRIER_CAMERA) VALUES (?, ?, ?, ?, ?, ?, ?)', (lastname, firstname, patronym, login, password, id_gate_camera, id_barrier_camera, ))
            self.connection.commit()
            return True
        except:
            return False

    def editPassword(self, login, password, new_password):  # функция для замены пароля охранника
        if len(new_password) < 6:
            return False
        self.cursor.execute('SELECT PASSWORD FROM SECURITIES WHERE LOGIN=?', (login, ))
        password_db = self.cursor.fetchall()[0][0]
        password = password.encode()
        password = hashlib.md5(password)
        password = password.hexdigest()
        if password_db == password:
            new_password = new_password.encode()
            new_password = hashlib.md5(new_password)
            new_password = new_password.hexdigest()
            self.cursor.execute('UPDATE SECURITIES SET PASSWORD=? WHERE LOGIN=?', (new_password, login, ))
            self.connection.commit()
            return True
            # заменить в бд запись с паролем на новую
        else:
            return False

    def accessAttempts(self, computer_id, datetime):  # функция для записи неудачных попыток входа
        try:
            self.cursor.execute('INSERT INTO access_attempts (computer_id, datetime) VALUES (?, ?)', (computer_id, datetime, ))
            self.connection.commit()
            return True
        except:
            return False

    # функция для вывода всех неудачных попыток входа в систему
    def getAccessAttempts(self):
        self.cursor.execute('SELECT computer_id, datetime FROM access_attempts ORDER BY datetime')
        access_attempts = self.cursor.fetchall()
        return access_attempts        



class visit:
    def __init__(self, name, date_time, is_car):
        self.name = str(name)
        self.date = str(date_time)
        self.is_car = str(is_car)

    def getName(self):
        return self.name

    def getDateTime(self):
        return self.date_time

    def getCar(self):
        return self.is_car


# проверки

#print(DataBase('db.sqlite3').getCarsNumbers()) # вывод всех автомобильных номеров
#print(DataBase('db.sqlite3').getDataOfCar('QWW')) # вывод сведений об автомобиле по его номеру (путь_к_фото_авто, ФИО)
#print(DataBase('db.sqlite3').getDataOfPeople('1'))# вывод сведений о посетителе по его id
#print(DataBase('db.sqlite3').getAllVisits()) # вывод всех посещений


# функция добавления посещений
#print(DataBase('db.sqlite3').addVisit( 'TRUE', 1, '12.12.2022')) # правильные входные данные

#функция для проверки правильности аутентификации:
#print(DataBase('db.sqlite3').isAuthenticate('ivanov.i.i', '123')) #не существует в бд
#print(DataBase('db.sqlite3').isAuthenticate('ertrtert', 'fghghfghb')) # неверный пароль
#print(DataBase('db.sqlite3').isAuthenticate('konkova', '123')) # верный логин и пароль


# функция для выборки id камер по id охранника (сначала камера ворот, потом- шлагбаума), можно обратиться по индексам 0 и 1 соответственно
#print(DataBase('db.sqlite3').cameraSelect(1))

# функция для добавления охранника
#print(DataBase('db.sqlite3').addSecurity('Konkov', 'A', 'N', 'konkova', '234', 1, 1)) # тк уже есть в бд выводит false


# функция для замены пароля охранника
#print(DataBase('db.sqlite3').editPassword('konkova', '123', '234567')) 

# функция для записи неудачных попыток входа
#print(DataBase('db.sqlite3').accessAttempts('122.123', '12.12.2022')) 


# функция для вывода всех неудачных попыток входа в систему
#print(DataBase('db.sqlite3').getAccessAttempts()) 