# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import os
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 211)
        MainWindow.setStyleSheet("background: black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 86, 481, 35))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: white;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 150, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: white;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Particle")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.click()
    def click(self):
    	self.pushButton.clicked.connect(self.open)
    def open(self):
    	if self.lineEdit.text() == "Your password": # Add your password
    		os.system("start programm.exe") # Add a programm or link to programm 
    		exit()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password - Defender"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.label.setText(_translate("MainWindow", "Password Defender"))
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
