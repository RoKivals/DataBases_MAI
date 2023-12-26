# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\AuthGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.authWidget = QtWidgets.QWidget(self.centralwidget)
        self.authWidget.setEnabled(True)
        self.authWidget.setGeometry(QtCore.QRect(275, 200, 250, 200))
        self.authWidget.setObjectName("authWidget")
        self.LoginAuthLine = QtWidgets.QLineEdit(self.authWidget)
        self.LoginAuthLine.setGeometry(QtCore.QRect(0, 0, 250, 30))
        self.LoginAuthLine.setObjectName("LoginAuthLine")
        self.LoginAuthLine.setPlaceholderText("Логин")
        self.PasswordAuthLine = QtWidgets.QLineEdit(self.authWidget)
        self.PasswordAuthLine.setGeometry(QtCore.QRect(0, 40, 250, 30))
        self.PasswordAuthLine.setObjectName("PasswordAuthLine")
        self.PasswordAuthLine.setPlaceholderText("Пароль")
        self.PasswordAuthLine.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.AuthAuthButton = QtWidgets.QPushButton(self.authWidget)
        self.AuthAuthButton.setEnabled(True)
        self.AuthAuthButton.setGeometry(QtCore.QRect(0, 100, 250, 40))
        self.AuthAuthButton.setObjectName("AuthAuthButton")
        self.AuthRegButton = QtWidgets.QPushButton(self.authWidget)
        self.AuthRegButton.setEnabled(True)
        self.AuthRegButton.setGeometry(QtCore.QRect(0, 150, 250, 40))
        self.AuthRegButton.setObjectName("AuthRegButton")
        self.NotificationAuth = QtWidgets.QLabel(self.authWidget)
        self.NotificationAuth.setGeometry(QtCore.QRect(0, 80, 250, 20))
        self.NotificationAuth.setText("")
        self.NotificationAuth.setAlignment(QtCore.Qt.AlignCenter)
        self.NotificationAuth.setObjectName("NotificationAuth")
        self.regWidget = QtWidgets.QWidget(self.centralwidget)
        self.regWidget.setVisible(False)
        self.regWidget.setGeometry(QtCore.QRect(275, 200, 250, 200))
        self.regWidget.setObjectName("regWidget")
        self.LoginRegLine = QtWidgets.QLineEdit(self.regWidget)
        self.LoginRegLine.setGeometry(QtCore.QRect(0, 0, 250, 30))
        self.LoginRegLine.setObjectName("LoginRegLine")
        self.LoginRegLine.setPlaceholderText("Логин")
        self.PasswordRegLine = QtWidgets.QLineEdit(self.regWidget)
        self.PasswordRegLine.setGeometry(QtCore.QRect(0, 40, 250, 30))
        self.PasswordRegLine.setObjectName("PasswordRegLine")
        self.PasswordRegLine.setPlaceholderText("Пароль")
        self.PasswordRegLine.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.RegRegButton = QtWidgets.QPushButton(self.regWidget)
        self.RegRegButton.setGeometry(QtCore.QRect(0, 120, 250, 40))
        self.RegRegButton.setObjectName("RegRegButton")
        self.NotificationReg = QtWidgets.QLabel(self.regWidget)
        self.NotificationReg.setGeometry(QtCore.QRect(0, 80, 250, 20))
        self.NotificationReg.setText("")
        self.NotificationReg.setAlignment(QtCore.Qt.AlignCenter)
        self.NotificationReg.setObjectName("NotificationReg")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoginAuthLine.setText(_translate("MainWindow", ""))
        self.PasswordAuthLine.setText(_translate("MainWindow", ""))
        self.AuthAuthButton.setText(_translate("MainWindow", "Войти"))
        self.AuthRegButton.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.LoginRegLine.setText(_translate("MainWindow", ""))
        self.PasswordRegLine.setText(_translate("MainWindow", ""))
        self.RegRegButton.setText(_translate("MainWindow", "Зарегистрироваться"))
