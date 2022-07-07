# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphs.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow):
        GraphWindow.setObjectName("GraphWindow")
        GraphWindow.resize(1545, 817)
        self.centralwidget = QtWidgets.QWidget(GraphWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background-color: #242424;\n"
"    font-family: Roboto;\n"
"    color: white;\n"
"    font-size: 20px;\n"
"    font-weight: 100px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.ChooseGraph = QtWidgets.QComboBox(self.centralwidget)
        self.ChooseGraph.setMinimumSize(QtCore.QSize(300, 40))
        self.ChooseGraph.setStyleSheet("QComboBox{\n"
"    background-color:  #313335;\n"
"}")
        self.ChooseGraph.setObjectName("ChooseGraph")
        self.ChooseGraph.addItem("")
        self.ChooseGraph.addItem("")
        self.ChooseGraph.addItem("")
        self.ChooseGraph.addItem("")
        self.horizontalLayout_2.addWidget(self.ChooseGraph)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.typeAnimal = QtWidgets.QComboBox(self.centralwidget)
        self.typeAnimal.setMinimumSize(QtCore.QSize(300, 40))
        self.typeAnimal.setStyleSheet("QComboBox{\n"
"    background-color:  #313335;\n"
"}")
        self.typeAnimal.setObjectName("typeAnimal")
        self.typeAnimal.addItem("")
        self.typeAnimal.addItem("")
        self.typeAnimal.addItem("")
        self.typeAnimal.addItem("")
        self.typeAnimal.addItem("")
        self.typeAnimal.addItem("")
        self.typeAnimal.addItem("")
        self.horizontalLayout_4.addWidget(self.typeAnimal)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.numberAnimal = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.numberAnimal.setMinimumSize(QtCore.QSize(300, 40))
        self.numberAnimal.setStyleSheet("QDoubleSpinBox\n"
"{\n"
"    background-color:  #313335;\n"
"}")
        self.numberAnimal.setDecimals(0)
        self.numberAnimal.setMinimum(1.0)
        self.numberAnimal.setMaximum(100000.0)
        self.numberAnimal.setObjectName("numberAnimal")
        self.horizontalLayout_5.addWidget(self.numberAnimal)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem12)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.horizontalLayoutForGraph = QtWidgets.QHBoxLayout()
        self.horizontalLayoutForGraph.setObjectName("horizontalLayoutForGraph")
        self.horizontalLayout_3.addLayout(self.horizontalLayoutForGraph)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem15)
        GraphWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GraphWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)

    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", "MainWindow"))
        self.label.setText(_translate("GraphWindow", "График"))
        self.ChooseGraph.setItemText(0, _translate("GraphWindow", "Смертность от возраста"))
        self.ChooseGraph.setItemText(1, _translate("GraphWindow", "Смертность от типа корма"))
        self.ChooseGraph.setItemText(2, _translate("GraphWindow", "Темп роста"))
        self.ChooseGraph.setItemText(3, _translate("GraphWindow", "Зависимость веса от типа корма"))
        self.label_2.setText(_translate("GraphWindow", "Тип животного"))
        self.typeAnimal.setItemText(0, _translate("GraphWindow", "Все животные"))
        self.typeAnimal.setItemText(1, _translate("GraphWindow", "Хрюша"))
        self.typeAnimal.setItemText(2, _translate("GraphWindow", "Корова"))
        self.typeAnimal.setItemText(3, _translate("GraphWindow", "Страус"))
        self.typeAnimal.setItemText(4, _translate("GraphWindow", "Курица"))
        self.typeAnimal.setItemText(5, _translate("GraphWindow", "Кролик"))
        self.typeAnimal.setItemText(6, _translate("GraphWindow", "Индейка"))
        self.label_3.setText(_translate("GraphWindow", "Номер животного"))
