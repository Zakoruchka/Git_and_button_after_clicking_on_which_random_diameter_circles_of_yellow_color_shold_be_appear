from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 460)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_after_clicking_on_which_random_diameter_circles_of_yellow_color_shold_be_appear_on_the_form = QtWidgets.QPushButton(self.centralwidget)
        self.button_after_clicking_on_which_random_diameter_circles_of_yellow_color_shold_be_appear_on_the_form.setGeometry(QtCore.QRect(10, 10, 400, 40))
        self.button_after_clicking_on_which_random_diameter_circles_of_yellow_color_shold_be_appear_on_the_form.setObjectName("button_after_clicking_on_which_random_diameter_circles_of_yellow_color_shold_be_appear_on_the_form")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 420, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_after_clicking_on_which_random_diameter_circles_of_yellow_color_shold_be_appear_on_the_form.setText(_translate("MainWindow", "Кнопка, после нажатия на которую на форме должны появляться\n"
"окружности желтого цвета и случайного диаметра"))
