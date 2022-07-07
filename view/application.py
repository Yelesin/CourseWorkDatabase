# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'application.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ApplicationWindow(object):
    def setupUi(self, ApplicationWindow):
        ApplicationWindow.setObjectName("ApplicationWindow")
        ApplicationWindow.resize(788, 743)
        self.centralwidget = QtWidgets.QWidget(ApplicationWindow)
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
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.SelectTypeApp = QtWidgets.QComboBox(self.centralwidget)
        self.SelectTypeApp.setMinimumSize(QtCore.QSize(350, 40))
        self.SelectTypeApp.setStyleSheet("QComboBox{\n"
"    background-color:  #313335;\n"
"}")
        self.SelectTypeApp.setObjectName("SelectTypeApp")
        self.SelectTypeApp.addItem("")
        self.SelectTypeApp.addItem("")
        self.SelectTypeApp.addItem("")
        self.horizontalLayout.addWidget(self.SelectTypeApp)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 40))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.SelectEmployee = QtWidgets.QComboBox(self.centralwidget)
        self.SelectEmployee.setMinimumSize(QtCore.QSize(350, 40))
        self.SelectEmployee.setStyleSheet("QComboBox{\n"
"    background-color:  #313335;\n"
"}")
        self.SelectEmployee.setObjectName("SelectEmployee")
        self.horizontalLayout_3.addWidget(self.SelectEmployee)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 40))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem10 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.SelectNumberAnimal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.SelectNumberAnimal.setMinimumSize(QtCore.QSize(200, 40))
        self.SelectNumberAnimal.setStyleSheet("QDoubleSpinBox\n"
"{\n"
"    background-color:  #313335;\n"
"}")
        self.SelectNumberAnimal.setDecimals(0)
        self.SelectNumberAnimal.setMinimum(1.0)
        self.SelectNumberAnimal.setMaximum(100000.0)
        self.SelectNumberAnimal.setObjectName("SelectNumberAnimal")
        self.horizontalLayout_2.addWidget(self.SelectNumberAnimal)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setMinimumSize(QtCore.QSize(150, 40))
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_2.addWidget(self.btn_add)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.btn_rm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rm.setMinimumSize(QtCore.QSize(150, 40))
        self.btn_rm.setObjectName("btn_rm")
        self.horizontalLayout_2.addWidget(self.btn_rm)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem14)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(650, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setStyleSheet("\n"
"QTableWidget{\n"
"    background-color:  #313335;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_6.addWidget(self.tableWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem15)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem16)
        self.btn_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_confirm.setMinimumSize(QtCore.QSize(200, 40))
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
        self.horizontalLayout_7.addWidget(self.btn_confirm)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem17)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem18)
        ApplicationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ApplicationWindow)
        QtCore.QMetaObject.connectSlotsByName(ApplicationWindow)

    def retranslateUi(self, ApplicationWindow):
        _translate = QtCore.QCoreApplication.translate
        ApplicationWindow.setWindowTitle(_translate("ApplicationWindow", "MainWindow"))
        self.label.setText(_translate("ApplicationWindow", "Тип заявки"))
        self.SelectTypeApp.setItemText(0, _translate("ApplicationWindow", "Заявка на списание"))
        self.SelectTypeApp.setItemText(1, _translate("ApplicationWindow", "Заявка на осмотр"))
        self.SelectTypeApp.setItemText(2, _translate("ApplicationWindow", "Заявка на изменение типа корма"))
        self.label_3.setText(_translate("ApplicationWindow", "Сотрудник"))
        self.label_2.setText(_translate("ApplicationWindow", "Номер животного"))
        self.btn_add.setText(_translate("ApplicationWindow", "Добавить"))
        self.btn_rm.setText(_translate("ApplicationWindow", "Удалить"))
        self.btn_confirm.setText(_translate("ApplicationWindow", "Подтвердить"))
        self.btn_confirm.setShortcut(_translate("ApplicationWindow", "Return"))