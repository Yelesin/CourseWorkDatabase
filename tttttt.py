import matplotlib.pyplot as plt
import psycopg2
from psycopg2.extras import DictCursor
from psycopg2 import sql

connect = psycopg2.connect(dbname='postgres', user='vet', password='1946', host='localhost')
cursor = connect.cursor()
try:
    sql1 = 'select age, count(*) from animal where write_off is not null group by age order by age'
    sql2 = ''
    cursor.execute(sql1, ())
    dat = cursor.fetchall()
    age = []
    count = []
    for i in range(len(dat)):
        age.append(dat[i][0])
        count.append(dat[i][1])

    fig = plt.figure()
    plt.bar(age, count)
    plt.title('Simple bar chart')
    plt.grid(True)  # линии вспомогательной сетки
    plt.show()
except psycopg2.Error as e:
    print(e)
finally:
    connect.close()
    cursor.close()