import sys
import PyQt5
import PyQt5.QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QHeaderView, QTableWidgetItem, QComboBox
from PyQt5.QtGui import QIcon, QPixmap
from view.inspection_mod import Ui_InspectionWindow
import psycopg2
from psycopg2 import sql

import model

connect = psycopg2.connect(dbname='postgres', user='vet', password='1946', host='localhost')
cursor = connect.cursor()

class ApplicationForm(QMainWindow, Ui_InspectionWindow):
    def __init__(self, username):
        super().__init__()
        self.form = Ui_InspectionWindow()
        self.form.setupUi(self)
        self.username = username
        self.openWindow()
        self.fillTable()
        self.form.SelectApp.currentTextChanged.connect(self.fillTable)
        self.form.btn_confirm.clicked.connect(self.getDataFromComboboxes)


    def openWindow(self):
        self.setWindowTitle('Осмотр')
        self.setWindowIcon(QIcon('view/icons/page/stethoscope.png'))
        self.form.SelectEmployee.addItem(self.username)
        self.data = getData()
        app = self.getListApplications()
        for data in app:
            self.form.SelectApp.addItem(str(data))


    def getListApplications(self) -> []:
        applications = []
        for i in self.data:
            if i[0] not in applications:
                applications.append(i[0])
        return applications


    def setNotEnabled(self, indexes: []):
        model = self.form.tableWidget.model()
        for i in indexes:
            model.item(i).setEnabled(False)


    def settingTable(self) -> None:
        columns = 5
        self.form.tableWidget.setColumnCount(columns)
        header = self.form.tableWidget.horizontalHeader()
        for i in range(columns):
            if i != columns -1:
                header.setSectionResizeMode(i, QHeaderView.Stretch)
            else:
                header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
        self.form.tableWidget.setHorizontalHeaderLabels(['Номер','Тип', 'Пол', 'Возраст', 'Статус'])


    def AddValueToTable(self, numberAnimal):
        rowCount = self.form.tableWidget.rowCount()
        info = getInfoAnimal(numberAnimal)
        self.form.tableWidget.insertRow(rowCount)
        self.form.tableWidget.setRowHeight(rowCount, 40)
        for i in range(len(info)):
            item = QTableWidgetItem(f'{info[i]}')
            item.setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)
            self.form.tableWidget.setItem(rowCount, i, item)
        box = QComboBox()
        box.addItems(['Здоровое', 'Больное', 'В заявку на списание'])
        for row in self.data:
            if row[1] == numberAnimal:
                status = row[2]
        if status == 'Здоровое':
            box.setCurrentIndex(0)
        elif status == 'Больное':
            box.setCurrentIndex(1)
        self.form.tableWidget.setCellWidget(rowCount, len(info), box)


    def fillTable(self):
        self.form.tableWidget.clear()
        self.form.tableWidget.setRowCount(0)
        self.settingTable()
        numApplication = self.form.SelectApp.currentText()
        try:
            numApplication = int(numApplication)
        except:
            return
        for i in self.data:
            if i[0] == numApplication:
                self.AddValueToTable(i[1])


    def getDataFromComboboxes(self):
        rows = self.form.tableWidget.rowCount()
        values = {}
        for i in range(rows):
            values[self.form.tableWidget.item(i,0).text()] = self.form.tableWidget.cellWidget(i, 4).currentText()
        return values


def getData():
    try:
        stmt = sql.SQL(f'SELECT * FROM all_app_inspection')
        cursor.execute(stmt)
        dat = cursor.fetchall()
    except psycopg2.Error as e:
        print(e)
    return dat


def getInfoAnimal(id_animal: int) -> (): # информация о конкретном животном
    try:
        tmp = sql.SQL(f'SELECT * FROM animal_info(%s)')
        cursor.execute(tmp, (id_animal,))
        dat = cursor.fetchall()
        info = []
        i = 0
        while i != 4:
            info.append(dat[0][i])
            i+= 1
        return info
    except psycopg2.Error as e:
        print(e)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ApplicationForm('Chort')
    form.show()
    sys.exit(app.exec_())

