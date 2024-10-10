# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editEmployee.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editEmployee(object):
    def setupUi(self, editEmployee):
        editEmployee.setObjectName("editEmployee")
        editEmployee.resize(712, 703)
        self.centralwidget = QtWidgets.QWidget(editEmployee)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background-color: #242424;\n"
"    font-family: Roboto;\n"
"    color: white;\n"
"    font-size: 20px;\n"
"    font-weight: 100px;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.lbl_position_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_position_2.setMinimumSize(QtCore.QSize(200, 35))
        self.lbl_position_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_position_2.setObjectName("lbl_position_2")
        self.horizontalLayout_6.addWidget(self.lbl_position_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.numEmployee = QtWidgets.QComboBox(self.centralwidget)
        self.numEmployee.setMinimumSize(QtCore.QSize(350, 40))
        self.numEmployee.setStyleSheet("QComboBox{\n"
"    background-color:  #313335;\n"
"}")
        self.numEmployee.setObjectName("numEmployee")
        self.horizontalLayout_6.addWidget(self.numEmployee)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.lbl_FullName = QtWidgets.QLabel(self.centralwidget)
        self.lbl_FullName.setMinimumSize(QtCore.QSize(200, 35))
        self.lbl_FullName.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_FullName.setObjectName("lbl_FullName")
        self.horizontalLayout.addWidget(self.lbl_FullName)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.Full_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Full_name_edit.setMinimumSize(QtCore.QSize(350, 40))
        self.Full_name_edit.setStyleSheet("QLineEdit{\n"
"    background-color: #3C3F41;\n"
"    border-radius: 12%;\n"
"    color: white;\n"
"    font-size: 20px;\n"
"}")
        self.Full_name_edit.setObjectName("Full_name_edit")
        self.horizontalLayout.addWidget(self.Full_name_edit)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.lbl_Login = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Login.setMinimumSize(QtCore.QSize(200, 35))
        self.lbl_Login.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_Login.setObjectName("lbl_Login")
        self.horizontalLayout_2.addWidget(self.lbl_Login)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.Login_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Login_edit.setMinimumSize(QtCore.QSize(350, 40))
        self.Login_edit.setStyleSheet("QLineEdit{\n"
"    background-color: #3C3F41;\n"
"    border-radius: 12%;\n"
"    color: white;\n"
"    font-size: 20px;\n"
"}")
        self.Login_edit.setObjectName("Login_edit")
        self.horizontalLayout_2.addWidget(self.Login_edit)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem12 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.lbl_passwd = QtWidgets.QLabel(self.centralwidget)
        self.lbl_passwd.setMinimumSize(QtCore.QSize(200, 35))
        self.lbl_passwd.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_passwd.setObjectName("lbl_passwd")
        self.horizontalLayout_3.addWidget(self.lbl_passwd)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.Passwd_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.Passwd_edit.setMinimumSize(QtCore.QSize(350, 40))
        self.Passwd_edit.setStyleSheet("QLineEdit{\n"
"    background-color: #3C3F41;\n"
"    border-radius: 12%;\n"
"    color: white;\n"
"    font-size: 20px;\n"
"}")
        self.Passwd_edit.setObjectName("Passwd_edit")
        self.horizontalLayout_3.addWidget(self.Passwd_edit)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem15)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem16 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem16)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem17)
        self.lbl_position = QtWidgets.QLabel(self.centralwidget)
        self.lbl_position.setMinimumSize(QtCore.QSize(200, 35))
        self.lbl_position.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_position.setObjectName("lbl_position")
        self.horizontalLayout_5.addWidget(self.lbl_position)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem18)
        self.Position = QtWidgets.QComboBox(self.centralwidget)
        self.Position.setMinimumSize(QtCore.QSize(350, 40))
        self.Position.setStyleSheet("QComboBox{\n"
"    background-color:  #313335;\n"
"}")
        self.Position.setObjectName("Position")
        self.Position.addItem("")
        self.Position.addItem("")
        self.Position.addItem("")
        self.Position.addItem("")
        self.horizontalLayout_5.addWidget(self.Position)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem19)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem20 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem20)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem21)
        self.lbl_salary = QtWidgets.QLabel(self.centralwidget)
        self.lbl_salary.setMinimumSize(QtCore.QSize(200, 35))
        self.lbl_salary.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_salary.setObjectName("lbl_salary")
        self.horizontalLayout_7.addWidget(self.lbl_salary)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem22)
        self.Salary = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Salary.setMinimumSize(QtCore.QSize(350, 40))
        self.Salary.setStyleSheet("QDoubleSpinBox\n"
"{\n"
"    background-color:  #313335;\n"
"}")
        self.Salary.setDecimals(0)
        self.Salary.setMaximum(1000000.0)
        self.Salary.setObjectName("Salary")
        self.horizontalLayout_7.addWidget(self.Salary)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem23)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem24 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem24)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem25)
        self.image_worker = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.image_worker.sizePolicy().hasHeightForWidth())
        self.image_worker.setSizePolicy(sizePolicy)
        self.image_worker.setMinimumSize(QtCore.QSize(200, 200))
        self.image_worker.setMaximumSize(QtCore.QSize(150, 150))
        self.image_worker.setText("")
        self.image_worker.setPixmap(QtGui.QPixmap("icons/roles/fraud.png"))
        self.image_worker.setScaledContents(True)
        self.image_worker.setObjectName("image_worker")
        self.horizontalLayout_8.addWidget(self.image_worker)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem26)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        spacerItem27 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem27)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem28)
        self.btn_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_confirm.setMinimumSize(QtCore.QSize(250, 40))
        self.btn_confirm.setStyleSheet("QPushButton{\n"
"    background-color: #313335;\n"
"    border: 3px qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #C622FF, stop:1 #1D6BFF);\n"
"    border-style: solid;\n"
"    border-radius: 12%;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:  #5C6164;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:  #5C6164;\n"
"}\n"
"\n"
"QPushButton:after{\n"
"background-color:  #5C6164;\n"
"}")
        self.btn_confirm.setObjectName("btn_confirm")
        self.horizontalLayout_9.addWidget(self.btn_confirm)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem29)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        spacerItem30 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem30)
        editEmployee.setCentralWidget(self.centralwidget)

        self.retranslateUi(editEmployee)
        QtCore.QMetaObject.connectSlotsByName(editEmployee)

    def retranslateUi(self, editEmployee):
        _translate = QtCore.QCoreApplication.translate
        editEmployee.setWindowTitle(_translate("editEmployee", "MainWindow"))
        self.lbl_position_2.setText(_translate("editEmployee", "Номер сотрудника"))
        self.lbl_FullName.setText(_translate("editEmployee", "ФИО"))
        self.lbl_Login.setText(_translate("editEmployee", "Логин"))
        self.lbl_passwd.setText(_translate("editEmployee", "Пароль"))
        self.lbl_position.setText(_translate("editEmployee", "Должность"))
        self.Position.setItemText(0, _translate("editEmployee", "Рабочий"))
        self.Position.setItemText(1, _translate("editEmployee", "Ветеринар"))
        self.Position.setItemText(2, _translate("editEmployee", "Администратор"))
        self.Position.setItemText(3, _translate("editEmployee", "Заведующий хозяйством"))
        self.lbl_salary.setText(_translate("editEmployee", "Зарплата"))
        self.btn_confirm.setText(_translate("editEmployee", "Добавить"))
        self.btn_confirm.setShortcut(_translate("editEmployee", "Return"))
