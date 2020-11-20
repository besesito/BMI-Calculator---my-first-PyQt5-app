from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 331)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.waga_label = QtWidgets.QLabel(self.centralwidget)
        self.waga_label.setGeometry(QtCore.QRect(120, 20, 141, 70))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.waga_label.setFont(font)
        self.waga_label.setObjectName("waga_label")
        self.spinBoxWaga = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxWaga.setGeometry(QtCore.QRect(160, 110, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.spinBoxWaga.setFont(font)
        self.spinBoxWaga.setMinimum(0)
        self.spinBoxWaga.setMaximum(120)
        self.spinBoxWaga.setObjectName("spinBoxWaga")



        self.wzrost_label = QtWidgets.QLabel(self.centralwidget)
        self.wzrost_label.setGeometry(QtCore.QRect(350, 20, 191, 70))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.wzrost_label.setFont(font)
        self.wzrost_label.setObjectName("wzrost_label")
        self.spinBoxWzrost = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxWzrost.setGeometry(QtCore.QRect(390, 110, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.spinBoxWzrost.setFont(font)
        self.spinBoxWzrost.setMinimum(100)
        self.spinBoxWzrost.setMaximum(200)
        self.spinBoxWzrost.setProperty("value", 100)
        self.spinBoxWzrost.setObjectName("spinBoxWzrost")



        self.bmi_display = QtWidgets.QLCDNumber(self.centralwidget)
        self.bmi_display.setGeometry(QtCore.QRect(220, 200, 171, 81))
        font = QtGui.QFont()
        font.setKerning(False)
        self.bmi_display.setFont(font)
        self.bmi_display.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bmi_display.setObjectName("bmi_display")
        self.obliczButton = QtWidgets.QPushButton(self.centralwidget)
        self.obliczButton.setGeometry(QtCore.QRect(250, 150, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.obliczButton.setFont(font)
        self.obliczButton.setObjectName("obliczButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.obliczButton.clicked.connect(self.oblicz)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BMI Calculator"))
        self.waga_label.setText(_translate("MainWindow", "Twoja waga:"))
        self.wzrost_label.setText(_translate("MainWindow", "Twój wzrost:"))
        self.obliczButton.setText(_translate("MainWindow", "Oblicz"))

    def oblicz(self):
        self.wzrost = self.spinBoxWzrost.value()
        self.waga = self.spinBoxWaga.value()

        return self.bmi_display.display(self.waga / ((self.wzrost / 100) ** 2))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
