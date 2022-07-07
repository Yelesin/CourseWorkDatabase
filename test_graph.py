import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5.QtGui import QIcon, QPixmap
from view.application import *
import psycopg2
from psycopg2.extras import DictCursor




class MainForm(QMainWindow, Ui_ApplicationWindow):

    def __init__(self):
        super().__init__()
        self.main_form = Ui_ApplicationWindow()
        self.main_form.setupUi(self)
        self.table()
        self.main_form.btn_add.clicked.connect(self.add_item)

    def table(self):

        self.main_form.tableWidget.setSortingEnabled(True)
        self.main_form.tableWidget.setColumnCount(1)
        self.main_form.tableWidget.setRowCount(6)
        self.main_form.tableWidget.setHorizontalHeaderLabels(['Название животных'])

    def add_item(self):
        data = self.main_form.SelectTypeApp.currentText()
        #for i, row in enumerate(data):
         #   for j, item in enumerate(row[1:]):
          #      self.main_form.tableWidget.setItem(i,j, QTableWidgetItem(item))

           #     print(item)
        count = self.main_form.tableWidget.rowCount()
        data = self.main_form.SelectNumberAnimal.value()
        #self.main_form.tableWidget.insertRow(count)
        connect = psycopg2.connect(dbname='postgres', user='postgres', password='1946', host='localhost')
        cursor = connect.cursor()  # cursor_factory=DictCursor)
        cursor.execute(f'SELECT gender FROM animal WHERE numberanimal={int(data)}')
        dat = cursor.fetchall()
        cursor.close()
        self.main_form.tableWidget.setItem(count, 2, QTableWidgetItem(f'{dat[0]}'))
        print(data)


app = QApplication(sys.argv)
application = MainForm()
application.show()
sys.exit(app.exec_())