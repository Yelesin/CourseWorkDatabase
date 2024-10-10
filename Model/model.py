import sys
from settings import *
import matplotlib.pyplot as plt
import psycopg2
from psycopg2.extras import DictCursor
from psycopg2 import sql
import hashlib

import matplotlib
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
matplotlib.use('Qt5Agg')


__connection = object
#__cursor = object


def createConnection(role):
    global __connection
    try:
        __connection = psycopg2.connect(dbname=database, user=role, host=host)
        #__cursor = __connection.cursor()
        print(f'Connection with role "{role}" successful !')
    except psycopg2.Error as e:
        print(e)


def closeConnection():
    global __connection
    __connection.close()
    print('Connection closed !')


def loginCheck(login:str, passwd:str, user = 'login') -> [str, str, ()]: # [ФИО пользователя, роль пользователя, информация о сотруднике]
    #household
    login = 'Djachkov'
    passwd = 'Dolg0Ekon7Zatv67'

    #admin
    #login = 'Voronov'
    #passwd = 'Dolg0Ekon7Zatv67'

    #worker
    #login = 'Zaharov'
    #passwd = 'BosiYavnPerl'

    #vet
    #login = 'Zhuravlev'
    #passwd = 'SaraUpolAnga'

    with __connection:
        try:
            __cursor = __connection.cursor()
            stmt = sql.SQL(f'SELECT password, fullname, position, status, id_employee FROM employee WHERE login=%s')
            __cursor = __connection.cursor()
        except psycopg2.Error as e:
            print(e)

        __cursor.execute(stmt, (login,))
        dat = __cursor.fetchall()
        if len(dat) == 0:               # в случае, если логин неправильный, то запрос вернёт пустой массив
            print('No employee')
            return -1
        else:
            if dat[0][3] == 'Не работает':  # проверка работает ли сотрудник
                return -2
            elif hashPassword(passwd) != dat[0][0]:       # проверка хеша пароля
                return -3

    global role
    if dat[0][2] == 'Ветеринар':
        role = 'vet'
    elif dat[0][2] == 'Рабочий':
        role = 'worker'
    elif dat[0][2] == 'Администратор':
        role = 'administrator'
    elif dat[0][2] == 'Заведующий хозяйством':
        role = 'head_household'

    id = dat[0][4]
    fullname = dat[0][1]
    position = dat[0][2]
    __cursor.close()
    return [role, position, getInfoEmployee(id)]


def hashPassword(passwd: str):
    hashed_string = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
    return hashed_string



def getInfoEmployee(id_employee: int) -> str: # возвращает информацию о сотруднике по идентификатору
    with __connection:
        try:
            __cursor = __connection.cursor()
            stmt = sql.SQL(f'SELECT * FROM employee_info(%s)')
        except psycopg2.Error as e:
            print(e)
        __cursor.execute(stmt, (id_employee,))
        dat = __cursor.fetchall()
        __cursor.close()
        return dat[0]



def getInfoAnimal(id_animal: int) -> (): # информация о конкретном животном
    with __connection:
        try:
            __cursor = __connection.cursor()
            tmp = sql.SQL(f'SELECT * FROM animal_info(%s)')
            __cursor.execute(tmp, (id_animal,))
            dat = __cursor.fetchall()
            __cursor.close()
            return dat[0]
        except psycopg2.Error as e:
            print(e)


def AddApplication(typeApplication: str, data: [], employee: str) -> int: # запрос на добавление заявки
   with __connection:
       try:
            __cursor = __connection.cursor()
            tmp = f'SELECT * FROM add_application(%s, %s, %s)'
            __cursor.execute(tmp, (typeApplication,data, employee))
            dat = __cursor.fetchall()
            __cursor.close()
            return 1
       except psycopg2.Error as e:
           print(e)
           __cursor.close()
           return -1


def listSickAndHealthyAnimals(isHealthy: bool) -> []: # возвращает список больных или здоровых животных
    with __connection:
        try:
            __cursor = __connection.cursor()
            if isHealthy:
                tmp = sql.SQL(f'SELECT * FROM info_animals_healthy')
            else:
                tmp = sql.SQL(f'SELECT * FROM info_animals_sick')
            __cursor.execute(tmp, ())
            dat = __cursor.fetchall()
            return dat
        except psycopg2.Error as e:
            print(e)


def listHungryAndFed(isHungry: bool):
    with __connection:
        try:
            __cursor = __connection.cursor()
            if isHungry:
                tmp = sql.SQL(f'SELECT * FROM info_animals_hungry')
            else:
                tmp = sql.SQL(f'SELECT * FROM info_animals_not_hungry')
            __cursor.execute(tmp, ())
            dat = __cursor.fetchall()
            return dat
        except psycopg2.Error as e:
            print(e)


def listApplications(typeApplication: str): # возвращает все заявки
    with __connection:
        try:
            __cursor = __connection.cursor()
            tmp = sql.SQL(f'SELECT * FROM get_applications(%s)')
            __cursor.execute(tmp, (typeApplication,))
            dat = __cursor.fetchall()
            #print(dat)
            return dat
        except psycopg2.Error as e:
            print(e)


def listAnimalsFromApplication(keyApplication: int): # Список животных с заявки
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql1 = 'select numberanimal from clarification_to_app where keyapplication = %s'
            __cursor.execute(sql1, (keyApplication,))
            dat = __cursor.fetchall()
            return dat
        except psycopg2.Error as e:
            print(e)


def changeFeed(employee: str, numApplication : int, numAnimals : [], feedAnimals: []):
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = 'SELECT * FROM change_feed(%s, %s, %s, %s)'
            __cursor.execute(sql, (employee, numApplication, numAnimals, feedAnimals,))
            return 0
        except psycopg2.Error as e:
            print(e)


def buildGraphs(graph: str, typeAnimal: str, numAnimal: int):
    age = []
    count = []
    weight = []
    date = []
    feed = []
    xlabel = ''
    ylabel = ''

    layout = QVBoxLayout()
    plt.style.use('seaborn-darkgrid')
    sc = MplCanvas()  # , width=5, height=4, dpi=100)

    with __connection:
        try:
            __cursor = __connection.cursor()
            if graph == 'Смертность от возраста':
                sc.axes.xaxis.set_major_locator(ticker.MultipleLocator(1))
                sc.axes.yaxis.set_major_locator(ticker.MultipleLocator(1))
                if typeAnimal == 'Все животные':
                    sql1 = 'select age, count(*) from animal where write_off is not null group by age order by age'
                    __cursor.execute(sql1, ())
                else:
                    sql1 = """select age, count(*) from animal
                              join type_animal on animal.typeanimal_key = type_animal.typeanimal_key
                              where write_off is not null and name_of_type = %s group by age order by age"""
                    __cursor.execute(sql1, (typeAnimal,))

                dat = __cursor.fetchall()
                for i in range(len(dat)):
                    age.append(dat[i][0])
                    count.append(dat[i][1])
                xlabel = 'Возраст'
                ylabel = 'Количество списанных животных'
                sc.axes.bar(age, count)

            elif graph == 'Темп роста':
                sql2 = 'select * from get_weighing_history(%s)'
                __cursor.execute(sql2, (numAnimal,))
                dat = __cursor.fetchall()
                for i in range(len(dat)):
                    date.append(dat[i][0])
                    weight.append(dat[i][1])
                xlabel = 'Дата'
                ylabel = 'Вес'
                sc.axes.plot(date, weight, marker='o')

            elif graph == 'Смертность от типа корма':
                sc.axes.xaxis.set_major_locator(ticker.MultipleLocator(1))
                if typeAnimal == 'Все животные':
                    sql3 = """select title, count(*) from animal
                            join feed on animal.key_feed = feed.key_feed 
                            where write_off is not null
                            group by title
                            order by title"""
                    __cursor.execute(sql3, ())
                else:
                    sql3 = """select title, count(*) from animal
                            join feed on animal.key_feed = feed.key_feed 
                            JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
                            where write_off is not null and name_of_type = %s
                            group by title
                            order by title"""
                    __cursor.execute(sql3, (typeAnimal,))
                dat = __cursor.fetchall()
                for i in range(len(dat)):
                    feed.append(dat[i][0])
                    count.append(dat[i][1])
                xlabel = 'Тип корма'
                ylabel = 'Количество списанных животных'
                sc.axes.bar(feed, count)

            elif graph == 'Зависимость веса от типа корма':
                sc.axes.xaxis.set_major_locator(ticker.MultipleLocator(1))
                if typeAnimal == 'Все животные':
                    sql4 = """select title, AVG(weight) from dynamic_growth
                            join animal on animal.numberanimal = dynamic_growth.numberanimal
                            join feed on feed.key_feed = animal.key_feed
                            group by title
                            order by title"""
                    __cursor.execute(sql4, ())
                else:
                    sql4 = """select title, AVG(weight) from dynamic_growth
                            join animal on animal.numberanimal = dynamic_growth.numberanimal
                            join feed on feed.key_feed = animal.key_feed
                            JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
                            where name_of_type = %s
                            group by title
                            order by title"""
                    __cursor.execute(sql4, (typeAnimal,))
                dat = __cursor.fetchall()
                for i in range(len(dat)):
                    feed.append(dat[i][0])
                    weight.append(dat[i][1])

                xlabel = 'Тип корма'
                ylabel = 'Вес'
                sc.axes.bar(feed, weight)
        except psycopg2.Error as e:
            print(e)

    sc.axes.set_xlabel(xlabel)
    sc.axes.set_ylabel(ylabel)
    layout.addWidget(sc)
    return layout


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure()  # figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


def listAppInspection():
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql1 = sql.SQL('SELECT * FROM all_app_inspection')
            __cursor.execute(sql1, ())
            dat = __cursor.fetchall()
            return dat
        except psycopg2.Error as e:
            print(e)


def inspect(employee: str, numApp: int, animals: [], statuses: []):
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = 'SELECT * FROM inspection(%s, %s, %s, %s)'
            __cursor.execute(sql, (employee, numApp, animals, statuses,))
            dat = __cursor.fetchall()
        except psycopg2.Error as e:
            print(e)


def add_animal(employee, typeAnimal, typeFeed, gender, weight, age):
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = 'SELECT * FROM insert_animal(%s, %s, %s, %s, %s, %s)'
            __cursor.execute(sql, (employee, typeAnimal, typeFeed, gender, weight, age,))
            dat = __cursor.fetchall()
            return 0
        except psycopg2.Error as e:
            print(e)
            return -1

def get_weight(idAnimal):
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = 'SELECT * FROM current_weight(%s)'
            __cursor.execute(sql, (idAnimal,))
            dat = __cursor.fetchall()
            return dat[0][0]
        except psycopg2.Error as e:
            print(e)
            return -1

def change_weight(employee:str, idAnimal: int, weight: int) -> int:
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = 'SELECT * FROM weight_animal(%s, %s, %s)'
            __cursor.execute(sql, (employee, idAnimal, weight,))
            dat = __cursor.fetchall()
            return 0
        except psycopg2.Error as e:
            print(e)
            return -1

def feed_animals(employee: str, idAnimals: []):
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = 'SELECT * FROM feed_animal(%s, %s)'
            __cursor.execute(sql, (employee, idAnimals,))
            dat = __cursor.fetchall()
            return 0
        except psycopg2.Error as e:
            print(e)
            return -1

def isHungry(idAnimal: int):
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = 'SELECT * FROM info_animals_not_hungry WHERE номер = %s'
            __cursor.execute(sql, (idAnimal,))
            dat = __cursor.fetchall()
        except psycopg2.Error as e:
            print(e)
            return -1

        if len(dat) == 0:
            return True
        else:
            return False

def addEmployee(fullname: str, login: str, passwd: str, position: str, salary: str):
    roles = ['Рабочий', 'Ветеринар', 'Администратор', 'Заведующий хозяйством']
    if len(fullname) == 0:
        return 'Заполните форму ФИО !'
    elif len(login) == 0:
        return 'Заполните форму логина !'
    elif len(passwd) == 0:
        return 'Заполните форму пароля !'
    elif len(position) == 0 or position not in roles:
        return 'Заполните форму должности !'
    try:
        salary = int(salary)
    except:
        return 'Неправильное значение зарплаты !'

    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = 'SELECT * FROM add_employee(%s, %s, %s, %s, %s)'
            __cursor.execute(sql, (login, passwd, fullname, position, salary,))
            dat = __cursor.fetchall()
            return 0
        except psycopg2.Error as e:
            return e.pgerror

def rmEmployee(idEmployee: int):
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = 'SELECT * FROM rm_employee(%s)'
            __cursor.execute(sql, (idEmployee,))
            dat = __cursor.fetchall()
            return 0
        except psycopg2.Error as e:
            return e.pgerror


def all_app_write_off():
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = 'SELECT * FROM all_app_write_off'
            __cursor.execute(sql, ())
            dat = __cursor.fetchall()
            return dat
        except psycopg2.Error as e:
            print(e)


def write_off_animals(numAnimals:[], statuses: [], numApplication:int, employee: str):
    data = []
    for i in range(len(numAnimals)):
        if statuses[i] == 'Списать':
            data.append(numAnimals[i])

    with __connection:
        try:
            __cursor = __connection.cursor()
            if len(data) == 0:
                sql = 'SELECT * FROM rm_application(%s)'
                __cursor.execute(sql, (numApplication,))
                dat = __cursor.fetchall()
            else:
                sql = 'SELECT * FROM write_off_animals(%s,%s,%s)'
                __cursor.execute(sql, (data, numApplication, employee,))
                dat = __cursor.fetchall()
        except psycopg2.Error as e:
            print(e)


def list_write_off():
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = 'SELECT numberanimal, name_of_type, title, age, gender FROM info_animals WHERE write_off IS NOT NULL'
            __cursor.execute(sql, ())
            dat = __cursor.fetchall()
            return dat
        except psycopg2.Error as e:
            print(e)

def list_animals():
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = 'SELECT numberanimal, name_of_type, title, age, gender FROM info_animals WHERE write_off IS NULL'
            __cursor.execute(sql, ())
            dat = __cursor.fetchall()
            return dat
        except psycopg2.Error as e:
            print(e)

def list_employees(isWork: bool):
    with __connection:
        try:
            __cursor = __connection.cursor()
            if isWork:
                sql = "SELECT id_employee, fullname, position, startdate, salary, status FROM employees WHERE status='Работает'"
            else:
                sql = "SELECT id_employee, fullname, position, startdate, salary, status FROM employees WHERE status='Не работает'"

            __cursor.execute(sql, ())
            dat = __cursor.fetchall()
            return dat
        except psycopg2.Error as e:
            print(e)

def list_employees_for_combo():
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = "SELECT id_employee, position, fullname FROM employees WHERE status='Работает'"
            __cursor.execute(sql, ())
            dat = __cursor.fetchall()
            return dat
        except psycopg2.Error as e:
            print(e)

def getSalary(idEmployee: int):
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = "SELECT salary FROM employees WHERE id_employee = %s"
            __cursor.execute(sql, (idEmployee,))
            dat = __cursor.fetchall()
            return dat
        except psycopg2.Error as e:
            print(e)


def setSalary(id:int, salary: int):
    try:
        salary = int(salary)
    except:
        return 'Невозможно обновить зарплату!'
    if salary == 0:
        return 'Зарплата не может быть равно 0!'

    try:
        id = int(id)
    except:
        return 'Неверно задан сотрудник!'

    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = "SELECT * FROM updateSalary(%s, %s)"
            __cursor.execute(sql, (id,salary,))
            dat = __cursor.fetchall()
            return 0
        except psycopg2.Error as e:
            print(e)

def getFullInfoEmployee(idEmployee: int):
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = "SELECT * FROM employee WHERE id_employee=%s AND status = 'Работает'"
            __cursor.execute(sql, (idEmployee,))
            dat = __cursor.fetchall()
            return dat
        except psycopg2.Error as e:
            print(e)
            return -1

def saveInfoEmployee(idEmployee: int, login: str, passwd: str, fullname: str, position: str, salary: int):
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = "SELECT * FROM updateInfoEmployee(%s, %s, %s, %s, %s, %s)"
            __cursor.execute(sql, (idEmployee, login, passwd, fullname, position, salary,))
            dat = __cursor.fetchall()
            return 0
        except psycopg2.Error as e:
            return e.pgerror


def all_applications():
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = "SELECT * FROM all_applications"
            __cursor.execute(sql, ())
            dat = __cursor.fetchall()
            return dat
        except psycopg2.Error as e:
            return e.pgerror


def rmApplication(id: int):
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = "SELECT * FROM rm_application(%s)"
            __cursor.execute(sql, (id,))
            dat = __cursor.fetchall()
            return 0
        except psycopg2.Error as e:
            return e.pgerror

def all_app_change_feed():
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = "SELECT * FROM all_app_change_feed"
            __cursor.execute(sql, (id,))
            dat = __cursor.fetchall()
            return dat
        except psycopg2.Error as e:
            print(e)
            return -1

def updateApplication(numApplication: int, animals: []):
    with __connection:
        try:
            __cursor = __connection.cursor()
            sql = "SELECT * FROM update_application(%s, %s)"
            __cursor.execute(sql, (numApplication, animals))
            dat = __cursor.fetchall()
            return 0
        except psycopg2.Error as e:
            return e.pgerror

#if __name__ == '__main__':
#    loginCheck('fdfd', 'fdfdf')
#    inspect(1, 5, 'Здоровое')
