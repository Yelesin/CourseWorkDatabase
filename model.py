import sys
from settings import *
import matplotlib.pyplot as plt
import psycopg2
from psycopg2.extras import DictCursor
from psycopg2 import sql

import matplotlib
from PyQt5.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
matplotlib.use('Qt5Agg')


role = 'login'
id = 0

def loginCheck(login:str, passwd:str, user = 'login') -> [str, str, ()]: # [ФИО пользователя, роль пользователя, информация о сотруднике]
    login = 'Miheev'
    passwd = 'StenOptiAvto6'
    with psycopg2.connect(dbname=database, user=user, host=host) as connect:
        with connect.cursor() as cursor:
            try:
                stmt = sql.SQL(f'SELECT password, fullname, position, status, id_employee FROM employee WHERE login=%s')
            except psycopg2.Error as e:
                print(e)

            cursor.execute(stmt, (login,))
            dat = cursor.fetchall()
            if len(dat) == 0:               # в случае, если логин неправильный, то запрос вернёт пустой массив
                print('No employee')
                return -1
            else:
                if passwd != dat[0][0] or dat[0][3] == 'Не работает':
                    return -1

    global role
    if dat[0][2] == 'Ветеринар':
        role = 'vet'
    elif dat[0][2] == 'Рабочий':
        role = 'worker'
    elif dat[0][2] == 'Администратор':
        role = 'administrator'
    elif dat[0][2] == 'Заведующий хозяйством':
        role = 'head_household'
    global id
    id = dat[0][4]

    return [dat[0][1], dat[0][2], getInfoEmployee(dat[0][4])]


def getInfoEmployee(id_employee: int) -> str: # возвращает информацию о сотруднике по идентификатору
    global role
    with psycopg2.connect(dbname=database, user=role, host=host) as connect:
        with connect.cursor() as cursor:
            try:
                stmt = sql.SQL(f'SELECT * FROM employee_info(%s)')
            except psycopg2.Error as e:
                print(e)
            cursor.execute(stmt, (id_employee,))
            dat = cursor.fetchall()
            return dat[0]


def getInfoAnimal(id_animal: int) -> (): # информация о конкретном животном
    global role
    with psycopg2.connect(dbname=database, user=role, host=host) as connect:
        with connect.cursor() as cursor:
            try:
                tmp = sql.SQL(f'SELECT * FROM animal_info(%s)')
                cursor.execute(tmp, (id_animal,))
                dat = cursor.fetchall()
                return dat[0]
            except psycopg2.Error as e:
                print(e)


def AddApplication(typeApplication: str, data: [], employee: str): # запрос на добавление заявки
    global role
    with psycopg2.connect(dbname=database, user=role, host=host) as connect:
        with connect.cursor() as cursor:
           try:
                tmp = sql.SQL(f'SELECT * FROM add_application(%s, %s, %s)')
                cursor.execute(tmp, (typeApplication,data, employee))
                dat = cursor.fetchall()
                return 1
           except psycopg2.Error as e:
               print(e)


def listSickAndHealthyAnimals(isHealthy: bool): # возвращает список больных или здоровых животных
    global role
    with psycopg2.connect(dbname=database, user=role, host=host) as connect:
        with connect.cursor() as cursor:
            try:
                if isHealthy:
                    tmp = sql.SQL(f'SELECT * FROM info_animals_healthy')
                else:
                    tmp = sql.SQL(f'SELECT * FROM info_animals_sick')
                cursor.execute(tmp, ())
                dat = cursor.fetchall()
                return dat
            except psycopg2.Error as e:
                print(e)


def listApplications(typeApplication: str): # возвращает все заявки
    global role
    with psycopg2.connect(dbname=database, user=role, host=host) as connect:
        with connect.cursor() as cursor: # cursor_factory=DictCursor)
            try:
                tmp = sql.SQL(f'SELECT * FROM get_applications(%s)')
                cursor.execute(tmp, (typeApplication,))
                dat = cursor.fetchall()
                return dat
            except psycopg2.Error as e:
                print(e)


def listAnimalsFromApplication(keyApplication: int): # Список животных с заявки
    global role
    with psycopg2.connect(ddbname=database, user=role, host=host) as connect:
        with connect.cursor() as cursor:
            try:
                sql1 = 'select numberanimal from clarification_to_app where keyapplication = %s'
                cursor.execute(sql1, (keyApplication,))
                dat = cursor.fetchall()
                return dat
            except psycopg2.Error as e:
                print(e)


def updateFeedAndRmApplication(numAndFeed: {}, numApplication):
    global role
    with psycopg2.connect(dbname=database, user=role, host=host) as connect:
        with connect.cursor() as cursor:
            try:
                sql1 = 'UPDATE animal SET key_feed = %s WHERE numberanimal = %s'
                sql2 = 'DELETE FROM clarification_to_app WHERE keyapplication= %s'
                sql3 = 'DELETE FROM application WHERE keyapplication = %s'
                for numAnimal, feed in numAndFeed.items():
                    cursor.execute(sql1, (feed,numAnimal,))
                    cursor.execute(sql2, (numApplication,))
                    cursor.execute(sql3, (numApplication,))
                return 1
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

    global role
    with psycopg2.connect(dbname='postgres', user=role, host='localhost') as connect:
        with connect.cursor() as cursor:
            try:
                if graph == 'Смертность от возраста':
                    sc.axes.xaxis.set_major_locator(ticker.MultipleLocator(1))
                    sc.axes.yaxis.set_major_locator(ticker.MultipleLocator(1))
                    if typeAnimal == 'Все животные':
                        sql1 = 'select age, count(*) from animal where write_off is not null group by age order by age'
                        cursor.execute(sql1, ())
                    else:
                        sql1 = """select age, count(*) from animal
                                  join type_animal on animal.typeanimal_key = type_animal.typeanimal_key
                                  where write_off is not null and name_of_type = %s group by age order by age"""
                        cursor.execute(sql1, (typeAnimal,))

                    dat = cursor.fetchall()
                    for i in range(len(dat)):
                        age.append(dat[i][0])
                        count.append(dat[i][1])
                    xlabel = 'Возраст'
                    ylabel = 'Количество списанных животных'
                    sc.axes.bar(age, count)

                elif graph == 'Темп роста':
                    sql2 = 'select * from get_weighing_history(%s)'
                    cursor.execute(sql2, (numAnimal,))
                    dat = cursor.fetchall()
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
                        cursor.execute(sql3, ())
                    else:
                        sql3 = """select title, count(*) from animal
                                join feed on animal.key_feed = feed.key_feed 
                                JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
                                where write_off is not null and name_of_type = %s
                                group by title
                                order by title"""
                        cursor.execute(sql3, (typeAnimal,))
                    dat = cursor.fetchall()
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
                        cursor.execute(sql4, ())
                    else:
                        sql4 = """select title, AVG(weight) from dynamic_growth
                                join animal on animal.numberanimal = dynamic_growth.numberanimal
                                join feed on feed.key_feed = animal.key_feed
                                JOIN type_animal ON animal.typeanimal_key = type_animal.typeanimal_key
                                where name_of_type = %s
                                group by title
                                order by title"""
                        cursor.execute(sql4, (typeAnimal,))
                    dat = cursor.fetchall()
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
    global role
    with psycopg2.connect(dbname=database, user=role, host=host) as connect:
        with connect.cursor() as cursor:
            try:
                sql = 'SELECT * FROM all_app_inspection'
                cursor.execute(sql, ())
                dat = cursor.fetchall()
                return dat
            except psycopg2.Error as e:
                print(e)


def inspect(numAnimal: int, numApp: int, status: str):
    global role
    with psycopg2.connect(dbname=database, user=role, host=host) as connect:
        with connect.cursor() as cursor:
            try:
                sql = 'SELECT * FROM inspect(%s, %s, %s, %s)'
                cursor.execute(sql, (numApp, numAnimal, status, id))
                dat = cursor.fetchall()
                return dat
            except psycopg2.Error as e:
                print(e)


#if __name__ == '__main__':
#    loginCheck('fdfd', 'fdfdf')
#    inspect(1, 5, 'Здоровое')
