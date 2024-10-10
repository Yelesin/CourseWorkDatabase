import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon, QPixmap
from view.add_animal import Ui_AddAnimalForm

images_animal = {
    'Корова' : 'view/icons/animals/__cow.png',
    'Курица' : 'view/icons/animals/__chiken.png',
    'Хрюша' : 'view/icons/animals/__pig.png',
    'Индейка' : 'view/icons/animals/__turkey.png',
    'Кролик' : 'view/icons/animals/__rabbit.png',
    'Страус' : 'view/icons/animals/__ostrich.png'
}

images_feed = {
    'Пшеница' : 'view/icons/feed/__wheat.png',
    'Морковь' : 'view/icons/feed/__carrot.png',
    'Овёс': 'view/icons/feed/__barley.png',
    'Биокорм' : 'view/icons/feed/__organic.png',
    'Комбикорм': 'view/icons/feed/__sunflower.png'
}

images_gender = {
    'Женский' : 'view/icons/gender/female.png',
    'Мужской' : 'view/icons/gender/male.png'
}


class MainForm(QMainWindow, Ui_AddAnimalForm):

    def __init__(self):
        super().__init__()
        self.main_form = Ui_AddAnimalForm()
        self.main_form.setupUi(self)
        self.setupAddAnimalPage()


    def setupAddAnimalPage(self):
        self.setWindowIcon(QIcon('view/icons/page/butterfly.png'))
        self.setWindowTitle('Добавить новое животное')
        self.main_form.btn_confirm.setText("Добавить")

        self.main_form.combo_animal.currentTextChanged.connect(self.comboAnimal_change)
        self.main_form.image_animal.setPixmap(QPixmap(images_animal['Курица']))

        self.main_form.combo_feed.currentTextChanged.connect(self.comboFeed_change)
        self.main_form.image_feed.setPixmap(QPixmap(images_feed['Пшеница']))

        self.main_form.combo_gender.currentTextChanged.connect(self.comboGender_change)

    def comboAnimal_change(self):
        animal = self.main_form.combo_animal.currentText()
        self.main_form.image_animal.setPixmap(QPixmap(images_animal[animal]))


    def comboFeed_change(self):
        feed = self.main_form.combo_feed.currentText()
        self.main_form.image_feed.setPixmap(QPixmap(images_feed[feed]))

    def comboGender_change(self):
        gender = self.main_form.combo_gender.currentText()
        self.main_form.image_gender.setPixmap(QPixmap(images_gender[gender]))


app = QApplication(sys.argv)
application = MainForm()
application.show()
sys.exit(app.exec_())