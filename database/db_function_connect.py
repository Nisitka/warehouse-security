import sqlite3
import hashlib
class dbConnect:

    def connectionOpen():
        connection = sqlite3.connect('db.sqlite3')  # подключение к бд
        cursor = connection.cursor()
        return (connection, cursor)


    def connectionClose(connection, cursor):
        cursor.close()
        connection.close()


    def array_creator(self, array_of_values):  # функция перегона кортежа в массив 
        temp_storage = array_of_values
        array_of_values = []
        for value in temp_storage:
            array_of_values += [value[0]]
        return array_of_values


    def getCarsNumbers(self):  # функция для вывода всех автомобильных номеров
        connection, cursor = dbConnect.connectionOpen()
        cursor.execute('SELECT NUMBER FROM CAR')
        cars_numbers = cursor.fetchall()
        cars_numbers = array_creator(cars_numbers)
        
        return cars_numbers  # выводится из бд в обратном порядке, от последних к первым


    def getDataOfCar(self,car_number):  # вывод сведений об автомобиле по его номеру  
        connection, cursor = dbConnect.connectionOpen()
        cursor.execute('SELECT CAR.PHOTO, PEOPLES.NAME FROM CAR JOIN PEOPLES ON CAR.ID_OWNER = PEOPLES.ID WHERE NUMBER=?', (car_number, ))
        car_data = cursor.fetchone()
        dbConnect.connectionClose(connection, cursor)
        return car_data  # данные в форме кортежа (путь_к_фото_авто, ФИО)


    def getDataOfPeople(self,people_id): # вывод сведений о человеке по его id
        connection, cursor = dbConnect.connectionOpen()
        people_data = cursor.execute('SELECT PHOTO, NAME, STATUS FROM PEOPLES WHERE ID=?', (people_id, ))
        dbConnect.connectionClose(connection, cursor)
        return people_data  # данные в форме кортежа (путь_к_фото_человека, ФИО, должность)


    def addVisit(self,status_car, people_id, datetime): # функция добавления посещений
        connection, cursor = dbConnect.connectionOpen()
        cursor.execute('INSERT INTO VISITS (ID_PEOPLE, IS_CAR, DATETIME) VALUES (?, ?, ?)', (people_id, status_car, datetime, ))
        connection.commit()
        dbConnect.connectionClose(connection, cursor)


    def getAllVisits(self):  # функция для вывода всех посещений как классов
        connection, cursor = dbConnect.connectionOpen()
        cursor.execute('SELECT PEOPLES.NAME, VISITS.DATETIME, VISITS.IS_CAR FROM VISITS JOIN PEOPLES ON VISITS.ID_PEOPLE=PEOPLES.ID ORDER BY DATETIME')
        visits = cursor.fetchall()
        dbConnect.connectionClose(connection, cursor)
        class visit:
            def __init__(self, name, date_time, is_car):
                self.name = name
                self.date = date_time
                self.is_car = is_car

            def name(self):
                return self.name

            def date_time(self):
                return self.date_time

            def is_car(self):
                return self.is_car

        visits_objects_list = []
        for vis in visits:
            vis = visit(vis[0],vis[1],vis[2])
            visits_objects_list += [vis]
        return visits_objects_list



    def is_authenticate(login, password):  # функция для проверки правильности аутентификации
        connection, cursor = dbConnect.connectionOpen()
        cursor.execute('SELECT PASSWORD FROM SECURITIES WHERE LOGIN=?', (login, ))
        password_db = cursor.fetchall()[0][0]
        dbConnect.connectionClose(connection, cursor)
        # сюда тоже вставить хешер
        if password_db == password:
            return('TRUE')
        else:
            return('FALSE')



    def camera_select(security_id):  # функция для выборки id камер по id охранника (сначала камера ворот, потом- шлагбаума), можно обратиться по индексам 0 и 1 соответственно
        connection, cursor = dbConnect.connectionOpen()
        cursor.execute('SELECT ID_GATE_CAMERA, ID_BARRIER_CAMERA  FROM SECURITIES WHERE ID=?', (security_id, ))
        cameras = cursor.fetchall()
        dbConnect.connectionClose(connection, cursor)
        return cameras


    def addSecurity(lastname, firstname, patronym, login, password, id_gate_camera, id_barrier_camera):  # какой-то ужасный запрос получается
        connection, cursor = dbConnect.connectionOpen()
        password = password.encode()
        password = hashlib.md5(password)
        password = password.hexdigest()
        print(password)

        cursor.execute('INSERT INTO SECURITIES (LASTNAME, FIRSTNAME, PATHRONYM, LOGIN, PASSWORD, ID_GATE_CAMERA, ID_BARRIER_CAMERA) VALUES (?, ?, ?, ?, ?, ?, ?)', (lastname, firstname, patronym, login, password, id_gate_camera, id_barrier_camera, ))
        connection.commit()
        dbConnect.connectionClose(connection, cursor)
        


    def editPassword(login, password, nev_password):  # функция для замены пароля охранника
        if len(passvord) < 6:
            return('FALSE')
        connection, cursor = dbConnect.connectionOpen()
        cursor.execute('SELECT PASSWORD FROM SECURITIES WHERE LOGIN=?', (login, ))
        password_db = cursor.fetchall()[0][0]
        password = password.encode()
        password = hashlib.md5(password)
        password = password.hexdigest()
        print(password)
        print(password_db)
        if password_db == password:
            nev_password = nev_password.encode()
            nev_password = hashlib.md5(nev_password)
            nev_password = nev_password.hexdigest()
            print(nev_password)
            cursor.execute('UPDATE SECURITIES SET PASSWORD=? WHERE LOGIN=?', (nev_password, login, ))
            connection.commit()
            dbConnect.connectionClose(connection, cursor)
            # заменить в бд запись с паролем на новую
        else:
            dbConnect.connectionClose(connection, cursor)
            return('FALSE')

    def accessAttempts(computer_id, datetime):  # функция для записи неужачных попыток входа
        connection, cursor = dbConnect.connectionOpen()
        cursor.execute('INSERT INTO access_attempts (computer_id, datetime) VALUES (?, ?)', (computer_id, datetime, ))
        connection.commit()
        dbConnect.connectionClose(connection, cursor)

    def getAccessAttempts(): # функция для вывода всех неудачных попыток входа в систему
        connection, cursor = dbConnect.connectionOpen()
        cursor.execute('SELECT computer_id, datetime FROM access_attempts ORDER BY ')
dbConnect.editPassword('ivanov', '1', '2')


