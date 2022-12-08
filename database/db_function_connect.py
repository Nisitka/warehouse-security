import sqlite3


def array_creator(array_of_values):  # функция перегона кортежа в массив (fetchall выводит все в виде кортежа-
    # иногда неудобно работать)
    temp_storage = array_of_values
    array_of_values = []
    for value in temp_storage:

        array_of_values += [value[0]]
    return array_of_values


def select_cars_numbers():  # функция для вывода всех автомобильных номеров
    connection = sqlite3.connect('db.sqlite3')  # подключение к бд
    cursor = connection.cursor()
    cursor.execute('SELECT NUMBER FROM CAR')
    cars_numbers = cursor.fetchall()
    cars_numbers = array_creator(cars_numbers)
    cursor.close()
    connection.close()
    return cars_numbers  # выводится из бд в обратном порядке, от последних к первым


def data_of_car(car_number):  # вывод сведений об автомобиле по его номеру
    connection = sqlite3.connect('db.sqlite3')  # подключение к бд
    cursor = connection.cursor()
    cursor.execute('SELECT CAR.PHOTO, PEOPLES.NAME FROM CAR JOIN PEOPLES ON CAR.ID_OWNER = PEOPLES.ID WHERE NUMBER=?', (car_number, ))
    car_data = cursor.fetchone()
    cursor.close()
    connection.close()
    return car_data  # данные в форме кортежа (путь_к_фото_авто, ФИО)


def data_of_people(people_id): # вывод сведений о человеке по его id
    connection = sqlite3.connect('db.sqlite3')  # подключение к бд
    cursor = connection.cursor()
    people_data = cursor.execute('SELECT PHOTO, NAME, STATUS FROM PEOPLES WHERE ID=?', (people_id, ))
    cursor.close()
    connection.close()
    return people_data  # данные в форме кортежа (путь_к_фото_человека, ФИО, должность)


def add_visit(status_car, people_id, datetime): # функция добавления посещений
    connection = sqlite3.connect('db.sqlite3')  # подключение к бд
    cursor = connection.cursor()
    cursor.execute('INSERT INTO VISITS (ID_PEOPLE, IS_CAR, DATETIME) VALUES (?, ?, ?)', (people_id, status_car, datetime, ))
    connection.commit()
    cursor.close()
    connection.close()


def all_visits():  # функция для вывода всех посещений как классов
    connection = sqlite3.connect('db.sqlite3')  # подключение к бд
    cursor = connection.cursor()
    cursor.execute('SELECT PEOPLES.NAME, VISITS.DATETIME, VISITS.IS_CAR FROM VISITS JOIN PEOPLES ON VISITS.ID_PEOPLE=PEOPLES.ID ORDER BY DATETIME')
    visits = cursor.fetchall()
    cursor.close()
    connection.close()
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

print(all_visits()[0].name())
