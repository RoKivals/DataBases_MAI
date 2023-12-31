# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ModelInfoGui.ui'
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
        self.centralwidget.setObjectName("centralwidget")
        self.BrandNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.BrandNameLabel.setGeometry(QtCore.QRect(30, 30, 100, 20))
        self.BrandNameLabel.setScaledContents(False)
        self.BrandNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BrandNameLabel.setObjectName("BrandNameLabel")
        self.BrandPicLabel = QtWidgets.QLabel(self.centralwidget)
        self.BrandPicLabel.setGeometry(QtCore.QRect(30, 50, 100, 100))
        self.BrandPicLabel.setText("")
        self.BrandPicLabel.setPixmap(QtGui.QPixmap("C:/Users/T/Pictures/O1gerKj--dGl_k0PXyL-sY4GprPziWVlILIwqPOblsUgcskhjU9JfRi9_R-qjJz2PvZhT4WiPANHNoHSeijslYd3.jpg"))
        self.BrandPicLabel.setScaledContents(True)
        self.BrandPicLabel.setObjectName("BrandPicLabel")
        self.BrandInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.BrandInfoButton.setGeometry(QtCore.QRect(30, 150, 100, 30))
        self.BrandInfoButton.setObjectName("BrandInfoButton")
        self.ModelNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.ModelNameLabel.setGeometry(QtCore.QRect(320, 30, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ModelNameLabel.setFont(font)
        self.ModelNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ModelNameLabel.setObjectName("ModelNameLabel")
        self.SpecTable = QtWidgets.QTableWidget(self.centralwidget)
        self.SpecTable.setGeometry(QtCore.QRect(320, 100, 400, 350))
        self.SpecTable.setObjectName("SpecTable")
        self.SpecTable.setColumnCount(0)
        self.SpecTable.setRowCount(0)
        self.BackButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackButton.setGeometry(QtCore.QRect(30, 460, 135, 60))
        self.BackButton.setObjectName("BackButton")
        self.EditButton = QtWidgets.QPushButton(self.centralwidget)
        self.EditButton.setGeometry(QtCore.QRect(320, 460, 150, 60))
        self.EditButton.setObjectName("EditButton")
        self.DeletButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeletButton.setGeometry(QtCore.QRect(570, 460, 150, 60))
        self.DeletButton.setObjectName("DeletButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BrandNameLabel.setText(_translate("MainWindow", "Имя Бренда"))
        self.BrandInfoButton.setText(_translate("MainWindow", "Информация"))
        self.ModelNameLabel.setText(_translate("MainWindow", "Имя модели"))
        self.BackButton.setText(_translate("MainWindow", "Назад"))
        self.EditButton.setText(_translate("MainWindow", "Изменить"))
        self.DeletButton.setText(_translate("MainWindow", "Удалить"))
