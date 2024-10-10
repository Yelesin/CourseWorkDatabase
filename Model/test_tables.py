import sys

from PyQt5 import Qt
import pyqtgraph as pg
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from list_animals import Ui_MainWindow
import psycopg2
from psycopg2.extras import DictCursor

connect = psycopg2.connect(dbname='postgres', user='postgres', password='1946', host='localhost')
cursor = connect.cursor()#cursor_factory=DictCursor)
cursor.execute('SELECT * FROM type_animal')
data = cursor.fetchall()
cursor.close()



class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.main_form = Ui_MainWindow()
        self.main_form.setupUi(self)
        self.table()



        self.view = view = pg.PlotWidget()
        self.curve = view.plot(name="Line")

        self.btn = Qt.QPushButton("Random plot")
        self.btn.clicked.connect(self.random_plot)

        self.main_form.widget_2.addWidget(Qt.QLabel("Some text"))
        self.main_form.widget_2.addWidget(self.view)
        self.main_form.widget_2.addWidget(self.btn)


    def random_plot(self):
        random_array = np.random.random_sample(20)
        self.curve.setData({1:34,43:32})
        print(random_array)

    def table(self):

        self.main_form.tableWidget.setSortingEnabled(True)
        self.main_form.tableWidget.setColumnCount(1)
        self.main_form.tableWidget.setRowCount(6)
        for i, row in enumerate(data):
            for j, item in enumerate(row[1:]):
                self.main_form.tableWidget.setItem(i,j, QTableWidgetItem(item))
                print(item)

        self.main_form.tableWidget.setHorizontalHeaderLabels(['Название животных'])


app = QApplication(sys.argv)
application = MainForm()
application.show()
sys.exit(app.exec_())