# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DeleteGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 165)
        self.NoButton = QtWidgets.QPushButton(Dialog)
        self.NoButton.setGeometry(QtCore.QRect(30, 80, 150, 60))
        self.NoButton.setObjectName("NoButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.YesButton = QtWidgets.QPushButton(Dialog)
        self.YesButton.setGeometry(QtCore.QRect(220, 80, 150, 60))
        self.YesButton.setObjectName("YesButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.NoButton.setText(_translate("Dialog", "Нет"))
        self.label.setText(_translate("Dialog", "Вы уверены?"))
        self.YesButton.setText(_translate("Dialog", "Да"))