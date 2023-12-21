import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QTableWidgetItem
import Gui
import ModelInfoGui
import BrandInfoGui
from config import *
import psycopg2
import datetime
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import AuthGui


try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(dbname=DBNAME, user=USER,
                                  # пароль, который указали при установке PostgreSQL
                                  password=PASSWORD,
                                  host=HOST,
                                  port=PORT)
    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    record = cursor.fetchall()
    print("Вы подключены к - ", record, "\n")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)


class BrandWindow(QtWidgets.QMainWindow, Gui.Ui_MainWindow):
    def __init__(self, cursor):
        super().__init__()
        self.cur = cursor
        self.setupUi(self)
        self.setFixedSize(800, 600)
        self.NextButton.clicked.connect(self.next_window)
        self.set_brands_list()
        self.ListWidget.clicked.connect(self.get_brand)
        self.InfoButton.clicked.connect(self.info_window)

    def info_window(self):
        global window

        window = BrandInfoWindow(self.cur, self.NameLabel.text())
        window.show()

    def next_window(self):
        global window
        window = ModelWindow(self.cur, self.NameLabel.text())
        window.show()

    def set_brands_list(self):
        self.cur.execute("SELECT name FROM companies;")
        res = [i[0] for i in self.cur.fetchall()]
        res.sort()
        for i in res:
            item = QListWidgetItem(i)
            self.ListWidget.addItem(item)

        self.set_brand(res[0])

    def set_brand(self, brand):
        self.NameLabel.setText(brand)
        # todo добавить Лого

    def get_brand(self):
        brand = self.ListWidget.currentItem().text()
        self.set_brand(brand)


class ModelWindow(QtWidgets.QMainWindow, Gui.Ui_MainWindow):
    def __init__(self, cursor, brand):
        super().__init__()
        self.brand = brand
        self.cur = cursor
        self.setupUi(self)
        self.setFixedSize(800, 600)
        self.NextButton.setVisible(False)
        self.InfoButton.setGeometry(110, 380, 135, 60)
        self.BackButton.clicked.connect(self.back_window)
        self.NameLabel.setText("Название Модели")
        self.set_models_list()
        self.ListWidget.clicked.connect(self.get_model)
        self.InfoButton.clicked.connect(self.info_window)

    def info_window(self):
        global window

        window = ModelInfoWindow(self.cur, self.brand, self.NameLabel.text())
        window.show()

    def get_model(self):
        model = self.ListWidget.currentItem().text()
        self.set_model(model)

    def back_window(self):
        global window

        window = BrandWindow(self.cur)
        window.show()

    def set_models_list(self):
        # todo обработка ситуации, когда нет моделей
        self.cur.execute(f'select model_name from models_range where company_id = (select id from companies where name = \'{self.brand}\')')
        res = [i[0] for i in self.cur.fetchall()]
        res.sort()
        for i in res:
            item = QListWidgetItem(i)
            self.ListWidget.addItem(item)

        self.set_model(res[0])

    def set_model(self, model):
        self.NameLabel.setText(model)
        # todo добавить Лого


class ModelInfoWindow(QtWidgets.QMainWindow, ModelInfoGui.Ui_MainWindow):
    def __init__(self, cursor, brand, model):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800, 600)
        self.cur = cursor
        self.BrandNameLabel.setText(brand)
        self.ModelNameLabel.setText(model)
        self.BackButton.clicked.connect(self.back_window)
        self.BrandInfoButton.clicked.connect(self.brand_info_window)
        self.set_info_table()

    def back_window(self):
        global window

        window = ModelWindow(self.cur, self.BrandNameLabel.text())
        window.show()

    def brand_info_window(self):
        global window

        window = BrandInfoWindow(self.cur, self.BrandNameLabel.text())
        window.show()

    def set_info_table(self):
        self.cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'models';")
        res = [i[0] for i in self.cur.fetchall()]
        self.cur.execute(f'SELECT * FROM models where name = \'{self.ModelNameLabel.text()}\';')
        res2 = list(self.cur.fetchall()[0])
        for i in range(len(res2)):
            res2[i] = str(res2[i])
        print(res2)
        self.SpecTable.setColumnCount(2)
        self.SpecTable.setRowCount(len(res))
        self.SpecTable.setHorizontalHeaderLabels(['Параметры', 'Значения'])
        for i in range(len(res)):
            self.SpecTable.setItem(i, 0, QTableWidgetItem(res[i]))

            self.SpecTable.setItem(i, 1, QTableWidgetItem(res2[i]))


class BrandInfoWindow(QtWidgets.QMainWindow, BrandInfoGui.Ui_MainWindow):
    def __init__(self, cursor, brand):
        super().__init__()
        self.cur = cursor
        self.setupUi(self)
        self.setFixedSize(800, 600)
        self.BrandNameLabel.setText(brand)
        self.BackButton.clicked.connect(self.back_window)
        self.NextButton.clicked.connect(self.next_window)
        self.set_info_table()

    def back_window(self):
        global window

        window = BrandWindow(self.cur)
        window.show()

    def next_window(self):
        global window

        window = ModelWindow(self.cur, self.BrandNameLabel.text())
        window.show()

    def set_info_table(self):
        self.cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'companies';")
        res = [i[0] for i in self.cur.fetchall()]
        self.cur.execute(f'SELECT * FROM companies where name = \'{self.BrandNameLabel.text()}\';')
        res2 = list(self.cur.fetchall()[0])
        for i in range(len(res2)):
            res2[i] = str(res2[i])
        self.InfoTable.setColumnCount(2)
        self.InfoTable.setRowCount(len(res))
        self.InfoTable.setHorizontalHeaderLabels(['Параметры', 'Значения'])
        for i in range(len(res)):
            self.InfoTable.setItem(i, 0, QTableWidgetItem(res[i]))
            self.InfoTable.setItem(i, 1, QTableWidgetItem(res2[i]))


class AuthWindow(QtWidgets.QMainWindow, AuthGui.Ui_MainWindow):
    def __init__(self, cursor):
        super().__init__()
        self.setupUi(self)
        self.cur = cursor
        self.AuthRegButton.clicked.connect(self.reg_window)
        self.AuthAuthButton.clicked.connect(self.auth_handle)
        self.RegRegButton(self.reg_handle)

    def auth_handle(self):
        pass

    def reg_handle(self):
        pass

    def reg_window(self):
        self.regWidget.setVisible(True)
        self.authWidget.setVisible(False)


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    #window = BrandWindow(cursor)  # Создаём объект класса ExampleApp
    window = AuthWindow(cursor)
    window.show()  # Показываем окно
    app.exec_()