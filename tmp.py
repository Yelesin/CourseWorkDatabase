import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
from view.login import Ui_Login_form
from view.main import Ui_MainWindow


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.main_form = Ui_MainWindow()
        self.main_form.setupUi(self)
        self.setWindowIcon(QIcon('icons/page/home-page.png'))


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
        self.login.lbl_error.setText('Error. Wrong data')
        #login_window.close()
        self.main_window = MainForm()
        self.main_window.show()
        self.main_window.main_form.tabWidget.setTabEnabled(3,False)



app = QApplication(sys.argv)
login_window = LoginForm()
login_window.show()
sys.exit(app.exec_())