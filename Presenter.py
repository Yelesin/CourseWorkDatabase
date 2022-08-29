import sys
import model

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QHeaderView, QMessageBox, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
import PyQt5.QtCore

from view.login import Ui_Login_form
from view.main import Ui_MainWindow
from view.application import Ui_ApplicationWindow
from view.list_animals import Ui_ListAnimalsWindow
from view.change_feed_many import Ui_ChangeFeedSecond
from view.graphs import Ui_GraphWindow
from view.inspection import Ui_InspectionWindow


class MainForm(QMainWindow, Ui_MainWindow):

    images = {0: 'view/icons/roles/medical-doctor.png', 1: 'view/icons/roles/fraud.png',
              2: 'view/icons/roles/hardworking--v2.png', 3: 'view/icons/roles/school-director.png'}

    def __init__(self):
        super().__init__()
        self.main_form = Ui_MainWindow()
        self.main_form.setupUi(self)
        self.setWindowIcon(QIcon('view/icons/page/home-page.png'))
        self.main_form.img_doctor.setPixmap(QPixmap(self.images[0]))
        self.main_form.img_worker.setPixmap(QPixmap(self.images[1]))
        self.main_form.img_admin.setPixmap(QPixmap(self.images[2]))
        self.main_form.img_house_hold.setPixmap(QPixmap(self.images[3]))


    def openWindow(self, role, position, info):  # вывод информации о сотруднике и блокирование страниц инных пользователей

        positions = {'Ветеринар': 0, 'Рабочий': 1, 'Администратор': 2, 'Заведующий хозяйством': 3}
        self.index = positions[position]
        self.position = position
        self.username = info[0]

        self.main_form.tabWidget.setCurrentIndex(self.index)
        if self.index == 0:
            self.main_form.lbl_hi_0.setText(f'Здравствуйте, {self.username}!')
            self.main_form.lbl_descript_0.setText(self.prepareInfo(info))
            self.disableTabs([1,2,3])
            self.main_form.btn_application.clicked.connect(self.App_btn)
            self.main_form.btn_list_animals.clicked.connect(self.Show_list_animals)
            self.main_form.btn_change_feet.clicked.connect(self.Change_feed_btn)
            self.main_form.btn_age_dead.clicked.connect(self.Graphs_age_dead_btn)
            self.main_form.btn_feed_dead.clicked.connect(self.Graphs_feed_dead_btn)
            self.main_form.btn_inspection.clicked.connect(self.Inspection_btn)

        elif self.index == 1:
            self.main_form.lbl_hi_1.setText(f'Здравствуйте, {self.username}!')
            self.main_form.lbl_descript_1.setText(self.prepareInfo(info))
            self.disableTabs([0, 2, 3])
        elif self.index == 2:
            self.main_form.lbl_hi2_2.setText(f'Здравствуйте, {self.username}!')
            self.main_form.lbl_descript_2.setText(self.prepareInfo(info))
            self.disableTabs([1, 0, 3])
        elif self.index == 3:
            self.main_form.lbl_hi_3.setText(f'Здравствуйте, {self.username}!')
            self.main_form.lbl_descript_3.setText(self.prepareInfo(info))
            self.disableTabs([1, 2, 0])

    def App_btn(self):
        self.app_form = ApplicationForm(self.position, self.username)
        self.app_form.show()

    def Show_list_animals(self):
        self.animalsList = ListAnimalsForm(self.position)
        self.animalsList.show()

    def Change_feed_btn(self):
        typeApplication = 'Заявка на изменение типа корма'
        self.change_feed = ChangeFeedForm(self.username, typeApplication)
        self.change_feed.show()

    def Graphs_age_dead_btn(self):
        self.graphs = GraphForm('Смертность от возраста')
        self.graphs.show()

    def Graphs_feed_dead_btn(self):
        self.graphs = GraphForm('Смертность от типа корма')
        self.graphs.show()


    def Inspection_btn(self):
        self.inspection = InspectionForm(self.username)
        self.inspection.show()

    def prepareInfo(self, info):
        res = ''
        res += f'Зарплата: {info[1]}\n'
        res += f'Дата начала работы: {info[2]}\n'
        res += f'Заявки на осмотр за год: {info[4]}\n'
        res += f'Заявки на списание за год: {info[5]}\n'
        res += f'Количество осмотров за год: {info[6]}'
        return res


    def disableTabs(self, indexes: []):
        for i in indexes:
            self.main_form.tabWidget.setTabEnabled(i, False)


    def closeEvent(self, event) -> None:
        model.closeConnection()




class LoginForm(QMainWindow, Ui_Login_form):
    def __init__(self):
        super().__init__()
        self.login = Ui_Login_form()
        self.login.setupUi(self)
        self.setupLoginUI()
        self.login.btn_confirm.clicked.connect(self.confirmPushedLogin)

    def setupLoginUI(self):
        self.setWindowTitle('Login form')
        self.setWindowIcon( QIcon('view/icons/page/login-rounded-right.png') )
        self.login.lineEdit_login.setPlaceholderText('Enter login')
        self.login.lineEdit_password.setPlaceholderText('Enter password')
        self.login.btn_confirm.setFocus()


    def confirmPushedLogin(self):
        login = self.login.lineEdit_login.text()
        passwd = self.login.lineEdit_password.text()

        result = model.loginCheck(login, passwd)

        if result == -1:
            self.login.lbl_error.setText('Ошибка. Такого сотрудника не существует !')
        elif result == -2:
            self.login.lbl_error.setText('Ошибка. Данный сотрудник не работает !')
        elif result == -3:
            self.login.lbl_error.setText('Ошибка. Неверный пароль !')
        else:
            role, position, info = result[0], result[1], result[2]
            login_window.close()
            model.createConnection(role)
            self.main = MainForm()
            self.main.openWindow(role, position, info)
            self.main.show()


    def closeEvent(self, event) -> None:
        model.closeConnection()


class ApplicationForm(QMainWindow, Ui_ApplicationWindow):

    def __init__(self, role: str, username: str):
        super().__init__()
        self.form = Ui_ApplicationWindow()
        self.form.setupUi(self)
        self.role = role
        self.id_animals = []
        self.username = username
        self.form.btn_add.clicked.connect(self.addToTable)
        self.form.btn_rm.clicked.connect(self.rmFromTable)
        self.form.btn_confirm.clicked.connect(self.clickConfirm)
        self.OpenWindow()

    def OpenWindow(self):
        self.setWindowTitle('Добавить заявку')
        self.setWindowIcon(QIcon('view/icons/page/file.png'))
        self.form.SelectEmployee.insertItem(0, self.username)
        model = self.form.SelectTypeApp.model()
        if self.role == 'Ветеринар':
            model.item(1).setEnabled(False) # заявка на осмотр
            model.item(2).setEnabled(False) # заявка на измененние типа корма
        elif self.role == 'Рабочий':
            model.item(0).setEnabled(False)  # заявка на списание

    def settingTable(self, columns: int):
        self.form.tableWidget.setColumnCount(columns)
        header = self.form.tableWidget.horizontalHeader()
        for i in range(columns):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
        self.form.tableWidget.setHorizontalHeaderLabels(['Номер','Тип', 'Пол', 'Возраст', 'Корм'])

    def addToTable(self):
        numberAnimal = self.form.SelectNumberAnimal.value()
        info_animal = model.getInfoAnimal(int(numberAnimal))
        if info_animal is None:
            self.showMessage("Выбранного животного не существует !")
            return
        elif info_animal[0] in self.id_animals:
            self.showMessage('Выбранное животное уже в списке !')
            return
        else:
            self.id_animals.append(int(info_animal[0]))

        self.settingTable(len(info_animal))
        rowCount = self.form.tableWidget.rowCount()
        self.form.tableWidget.insertRow(rowCount)
        for i in range(len(info_animal)):
            item = QTableWidgetItem(f'{info_animal[i]}')
            item.setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)
            self.form.tableWidget.setItem(rowCount, i, item)


    def rmFromTable(self):
        row = self.form.tableWidget.currentRow()
        if row > -1:  # Если есть выделенная строка/элемент
            self.id_animals.remove(int(self.form.tableWidget.item(row, 0).text()))
            self.form.tableWidget.removeRow(row)
            # Следующий вызов нужен для того, чтобы
            # сбросить индекс выбранной строки (чтобы currentRow установился в -1)
            self.form.tableWidget.selectionModel().clearCurrentIndex()


    def showMessage(self, text: str):
        msg = QMessageBox()
        msg.setWindowTitle("Предупреждение")
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def clickConfirm(self):
        if self.id_animals == []:
            self.showMessage('Отсутствуют животные в списке !')
            return
        else:
            res = model.AddApplication(self.form.SelectTypeApp.currentText(), self.id_animals, self.form.SelectEmployee.currentText())
            if res == -1:
                self.showMessage('Не удалось отправить заявку. Проверьте данные !')
                return
            else:
                self.form.tableWidget.clear()
                self.form.tableWidget.setRowCount(0)
                self.form.tableWidget.setColumnCount(0)
                self.id_animals = []
                self.form.SelectNumberAnimal.setValue(1)
                self.showMessage('Заявка успешно отправлена !')


class ListAnimalsForm(QMainWindow, Ui_ListAnimalsWindow):
    def __init__(self, role):
        super().__init__()
        self.form = Ui_ListAnimalsWindow()
        self.form.setupUi(self)
        self.role = role
        self.OpenWindow()
        self.showListSick()
        self.form.comboBox.currentTextChanged.connect(self.showListSick)

    def OpenWindow(self):
        self.setWindowTitle('Список животных')
        self.setWindowIcon(QIcon('view/icons/page/show-property.png'))
        model = self.form.comboBox.model()
        if self.role == 'Ветеринар':
            self.form.comboBox.setCurrentIndex(1)
            self.setNotEnabled([0,3,4,5])
        elif self.role == 'Рабочий':
            self.setNotEnabled([0,1,2,3])
        elif self.role == 'Заведующий предприятием':
            self.setNotEnabled([1, 2, 3, 4])


    def setNotEnabled(self, indexes: []):
        model = self.form.comboBox.model()
        for i in indexes:
            model.item(i).setEnabled(False)


    def settingTableForVet(self, columns: int):
        self.form.tableWidget.setColumnCount(columns)
        header = self.form.tableWidget.horizontalHeader()
        for i in range(columns):
            if i != 2:
                header.setSectionResizeMode(i, QHeaderView.Stretch)
            else:
                header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
        self.form.tableWidget.setHorizontalHeaderLabels(['Номер','Тип', 'Последний осмотр', 'Корм', 'Статус', 'Возраст', 'Пол'])


    def showListSick(self):
        self.form.tableWidget.clear()
        self.form.tableWidget.setRowCount(0)
        self.form.tableWidget.setColumnCount(0)
        index = self.form.comboBox.currentIndex()
        if index == 1:
            data = model.listSickAndHealthyAnimals(False)
        elif index == 2:
            data = model.listSickAndHealthyAnimals(True)
        self.settingTableForVet(len(data[0]))
        for i in range(len(data)):
            rowCount = self.form.tableWidget.rowCount()
            self.form.tableWidget.insertRow(rowCount)
            for j in range(len(data[i])):
                item = QTableWidgetItem(f'{data[i][j]}')
                item.setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)
                self.form.tableWidget.setItem(rowCount, j, item)


class ChangeFeedForm(QMainWindow, Ui_ChangeFeedSecond):
    def __init__(self, username: str, typeApplication: str):
        super().__init__()
        self.form = Ui_ChangeFeedSecond()
        self.form.setupUi(self)
        self.feed = {'Овёс': 0, 'Пшеница': 1, 'Морковка': 2, 'Биокорм': 3, 'Комбикорм': 4}
        self.typeApp = typeApplication
        self.username = username
        self.OpenWindow()
        self.settingTable()
        self.changeApp()
        self.form.selectApp.currentTextChanged.connect(self.changeApp)
        self.form.btn_confirm.clicked.connect(self.btnConfirmClick)



    def OpenWindow(self):
        self.setWindowTitle('Изменить тип корма')
        self.setWindowIcon(QIcon('view/icons/page/meal.png'))
        self.form.selectEmployee.insertItem(0, self.username)
        self.applications = model.listApplications(self.typeApp)
        list = [i for i in self.applications if 'Заявка на изменение типа корма' in i]
        if list == []:
            self.showMessage('Нет доступных заявок !')
            self.isEmpty = True
        else:
            for i in range(len(list)):
                typeApplication, numApplication = list[i][0], list[i][1]
                self.numApp = numApplication
                text = f'{typeApplication} № {numApplication}'
                self.form.selectApp.insertItem(i,text)


    def settingTable(self):
        columns = len(model.getInfoAnimal(1))
        self.form.tableWidget.setColumnCount(columns)
        header = self.form.tableWidget.horizontalHeader()
        for i in range(columns):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
        self.form.tableWidget.setHorizontalHeaderLabels(['Номер','Тип', 'Пол', 'Возраст', 'Корм'])


    def changeApp(self):
        if self.isEmpty:
            return
        self.form.tableWidget.clear()
        self.form.tableWidget.setRowCount(0)
        self.settingTable()
        num = self.numApp
        animals = model.listAnimalsFromApplication(num)
        info_animals = []
        for i in range(len(animals)):
            info_animals.append(model.getInfoAnimal(animals[i][0]))

        for i in range(len(info_animals)):
            rowCount = self.form.tableWidget.rowCount()
            self.form.tableWidget.insertRow(rowCount)
            for j in range(len(info_animals[i])):
                if j == len(info_animals[i]) -1:
                    feed = info_animals[i][j]
                    self.form.tableWidget.setCellWidget(i,j, self.createComboBox(self.feed[feed]))
                else:
                    item = QTableWidgetItem(f'{info_animals[i][j]}')
                    item.setTextAlignment(PyQt5.QtCore.Qt.AlignCenter)
                    self.form.tableWidget.setItem(i, j, item)


    def createComboBox(self, index):
        combo = PyQt5.QtWidgets.QComboBox()
        combo.setStyleSheet('QComboBox{background-color:  #313335;}')
        for i in self.feed:
            combo.addItem(i)
        combo.setCurrentIndex(index)
        return combo


    def btnConfirmClick(self):
        if self.isEmpty:
            return
        data = {}
        rows = self.form.tableWidget.rowCount()
        columns = self.form.tableWidget.columnCount()
        for i in range(rows):
            feed = self.form.tableWidget.cellWidget(i, columns-1).currentText()
            numAnimal = int(self.form.tableWidget.item(i, 0).text())
            data[numAnimal] = self.feed[feed] + 1
        res = model.updateFeedAndRmApplication(data, self.numApp)
        if res == 1:
            self.showMessage('Изменения успешно внесены !')
            self.close()

    def showMessage(self, text: str):
        msg = QMessageBox()
        msg.setWindowTitle("Изменения")
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()


class GraphForm(QMainWindow, Ui_GraphWindow):
    def __init__(self, typeGraph: str):
        super().__init__()
        self.form = Ui_GraphWindow()
        self.form.setupUi(self)
        self.typeGraph = typeGraph
        self.openWindow()
        self.form.ChooseGraph.currentTextChanged.connect(self.changeGraph)
        self.form.typeAnimal.currentTextChanged.connect(self.changeGraph)
        self.form.numberAnimal.valueChanged.connect(self.changeGraph)


    def openWindow(self):
        self.setWindowTitle('Построение графиков')
        self.setWindowIcon(QIcon('view/icons/page/combo-chart.png'))
        if self.typeGraph == 'Смертность от возраста':
            self.form.ChooseGraph.setCurrentIndex(0)
            self.setNotEnabled([1, 2, 3])
            self.form.numberAnimal.setEnabled(False)
        elif self.typeGraph == 'Смертность от типа корма':
            self.form.ChooseGraph.setCurrentIndex(1)
            self.setNotEnabled([0, 2, 3])
            self.form.numberAnimal.setEnabled(False)
        elif self.typeGraph == 'Темп роста':
            self.form.ChooseGraph.setCurrentIndex(2)
            self.setNotEnabled([0, 1, 3])
            self.form.typeAnimal.setEnabled(False)
        elif self.typeGraph == 'Зависимость веса от типа корма':
            self.form.ChooseGraph.setCurrentIndex(1)
            self.setNotEnabled([0, 1, 2])
            self.form.numberAnimal.setEnabled(False)

        self.changeGraph()


    def changeGraph(self):
        self.clearGraph()
        self.graph = self.form.ChooseGraph.currentText()
        self.typeAnimal = self.form.typeAnimal.currentText()
        self.numberAnimal = int(self.form.numberAnimal.value())
        layout = model.buildGraphs(self.graph, self.typeAnimal, self.numberAnimal)
        self.form.horizontalLayoutForGraph.addLayout(layout)


    def clearGraph(self):
        for i in reversed(range(self.form.horizontalLayoutForGraph.layout().count())):
            self.form.horizontalLayoutForGraph.layout().itemAt(i).setParent(None)


    def setNotEnabled(self, indexes: []):
        model = self.form.ChooseGraph.model()
        for i in indexes:
            model.item(i).setEnabled(False)


class InspectionForm(QMainWindow, Ui_InspectionWindow):
    def __init__(self, fullname: str):
        super().__init__()
        self.form = Ui_InspectionWindow()
        self.form.setupUi(self)

        self.fullname = fullname
        self.openWindow()
        self.form.animal_box.currentTextChanged.connect(self.changeInfo)
        self.form.pushButton.clicked.connect(self.btnInspectionClicked)


    def openWindow(self):
        self.setWindowTitle('Осмотр')
        self.setWindowIcon(QIcon('view/icons/page/stethoscope.png'))
        self.form.employee_box.addItem(self.fullname)
        dat = model.listAppInspection()
        if dat == []:
            self.isEmpty = True
            self.showMessage('Отсутствуют заявки на осмотр !')
            return
        else:
            self.isEmpty = False
        self.data = dat
        self.form.animal_box.clear()
        for row in dat:
            info = f'Заявка на осмотр № {row[0]}, животное номер: {row[1]}'
            self.form.animal_box.addItem(info)
        self.changeInfo()


    def changeInfo(self):

        if self.isEmpty:
            return

        numAnimal = int(self.form.animal_box.currentText().split(':')[-1])
        for row in self.data:
            if numAnimal in row:
                status = row[-1]

        info = model.getInfoAnimal(numAnimal)
        self.form.status_box.setCurrentText(status)
        if info is None:
            self.form.info_animal.setText('Не существует животного с данным номером или оно списано')
            self.form.img_animal_1 .setPixmap(QPixmap('/view/icons/fone.png'))
            self.form.img_feed_1.setPixmap(QPixmap('/view/icons/fone.png'))
            self.form.img_gender_1.setPixmap(QPixmap('/view/icons/fone.png'))
        else:
            inf = f'Тип - {info[1]}, Пол - {info[2]}, Возраст - {info[3]}, Корм - {info[4]}'
            self.form.info_animal.setText(inf)
            self.setImages(info[1], info[4], info[2])


    def setImages(self, animal, feed, gender):
        images_animal = {
            'Корова': 'view/icons/animals/__cow.png',
            'Курица': 'view/icons/animals/__chiken.png',
            'Хрюша': 'view/icons/animals/__pig.png',
            'Индейка': 'view/icons/animals/__turkey.png',
            'Кролик': 'view/icons/animals/__rabbit.png',
            'Страус': 'view/icons/animals/__ostrich.png'
        }

        images_feed = {
            'Пшеница': 'view/icons/feed/__wheat.png',
            'Морковка': 'view/icons/feed/__carrot.png',
            'Овёс': 'view/icons/feed/__barley.png',
            'Биокорм': 'view/icons/feed/__organic.png',
            'Комбикорм': 'view/icons/feed/__sunflower.png'
        }

        images_gender = {
            'Женский': 'view/icons/gender/female.png',
            'Мужской': 'view/icons/gender/male.png'
        }
        self.form.img_animal_1.setPixmap(QPixmap(images_animal[animal]))
        self.form.img_feed_1.setPixmap(QPixmap(images_feed[feed]))
        self.form.img_gender_1.setPixmap(QPixmap(images_gender[gender]))


    def showMessage(self, text: str):
        msg = QMessageBox()
        msg.setWindowTitle("Изменения")
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()


    def btnInspectionClicked(self):
        if self.isEmpty:
            return
        row = self.form.animal_box.currentText()
        numAnimal = int(row.split(':')[-1])
        numApp = int(row.split('№')[1][1])
        status = self.form.status_box.currentText()
        print(status)
        try:
            model.inspect(numAnimal, numApp, status)
            self.showMessage('Изменения успешно внесены !')
            self.openWindow()
        except:
            return


if __name__ == '__main__':
    model.createConnection('login')
    app = QApplication(sys.argv)
    login_window = LoginForm()
    login_window.show()

    sys.exit(app.exec_())