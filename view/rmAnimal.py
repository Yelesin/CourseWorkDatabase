# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rmAnimal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 471)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        spacerItem = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.numberAnimal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.numberAnimal.setMinimumSize(QtCore.QSize(250, 40))
        self.numberAnimal.setStyleSheet("QDoubleSpinBox\n"
"{\n"
"    background-color:  #313335;\n"
"}")
        self.numberAnimal.setDecimals(0)
        self.numberAnimal.setMinimum(1.0)
        self.numberAnimal.setMaximum(10000.0)
        self.numberAnimal.setObjectName("numberAnimal")
        self.horizontalLayout_5.addWidget(self.numberAnimal)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.infoAnimal = QtWidgets.QLabel(self.centralwidget)
        self.infoAnimal.setStyleSheet("color: #B15B2E")
        self.infoAnimal.setObjectName("infoAnimal")
        self.horizontalLayout_3.addWidget(self.infoAnimal)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.img_animal = QtWidgets.QLabel(self.centralwidget)
        self.img_animal.setMinimumSize(QtCore.QSize(150, 150))
        self.img_animal.setText("")
        self.img_animal.setObjectName("img_animal")
        self.horizontalLayout.addWidget(self.img_animal)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem9)
        self.img_feed = QtWidgets.QLabel(self.centralwidget)
        self.img_feed.setMinimumSize(QtCore.QSize(150, 150))
        self.img_feed.setText("")
        self.img_feed.setObjectName("img_feed")
        self.horizontalLayout.addWidget(self.img_feed)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.img_gender = QtWidgets.QLabel(self.centralwidget)
        self.img_gender.setMinimumSize(QtCore.QSize(150, 150))
        self.img_gender.setText("")
        self.img_gender.setObjectName("img_gender")
        self.horizontalLayout.addWidget(self.img_gender)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem12 = QtWidgets.QSpacerItem(20, 32, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem12)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.btn_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_confirm.setMinimumSize(QtCore.QSize(200, 40))
        self.btn_confirm.setMaximumSize(QtCore.QSize(200, 40))
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
"}\n"
"\n"
"QTableWidget{\n"
"    background-color:  #313335;\n"
"}")
        self.btn_confirm.setObjectName("btn_confirm")
        self.horizontalLayout_2.addWidget(self.btn_confirm)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Номер животного"))
        self.infoAnimal.setText(_translate("MainWindow", "Инфа о животном"))
        self.btn_confirm.setText(_translate("MainWindow", "Подтвердить"))
