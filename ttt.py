import matplotlib.pyplot as plt
import psycopg2
from psycopg2.extras import DictCursor
from psycopg2 import sql
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from view.login import Ui_Login_form

connect = psycopg2.connect(dbname='postgres', user='login', password='1946', host='localhost')
cursor = connect.cursor()


class LoginForm(QMainWindow, Ui_Login_form):
    def __init__(self):
        super().__init__()
        self.login = Ui_Login_form()
        self.login.setupUi(self)
        self.setupFormUI()


    def setupFormUI(self):
        self.setWindowTitle('Login form')
        self.setWindowIcon( QIcon('icons/page/login-rounded-right.png') )
        self.login.lineEdit_login.setPlaceholderText('Enter login')
        self.login.lineEdit_password.setPlaceholderText('Enter password')
        self.login.btn_confirm.setFocus()
        self.login.btn_confirm.clicked.connect(self.confirm_pushed)


    def confirm_pushed(self):
        print(loginCheck(self.login.lineEdit_login.text(), self.login.lineEdit_password.text()))

    def closeEvent(self, event) -> None:
        print('close window')
        connect.close()
        cursor.close()



def loginCheck(login='dd', passwd = 'dd', user = 'login') -> [str, str, ()]: # [ФИО пользователя, роль пользователя, информация о сотруднике]
    #login = 'Miheev'
    passwd = 'StenOptiAvto6'
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
        print('Exit from while')
        return dat




if __name__ == '__main__':


    app = QApplication(sys.argv)
    login_window = LoginForm()
    login_window.show()

    sys.exit(app.exec_())

