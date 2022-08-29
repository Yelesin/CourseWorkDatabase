from settings import *
import psycopg2


role = 'vet'
connect = psycopg2.connect(dbname=database, user=role, host=host)
cursor = connect.cursor()


def listAppInspection():
    global role
    try:
        sql = 'SELECT * FROM all_app_inspection'
        cursor.execute(sql, ())
        dat = cursor.fetchall()
        return dat
    except psycopg2.Error as e:
        print(e)


    if __name__ == '__main__':
        print(listAppInspection())
