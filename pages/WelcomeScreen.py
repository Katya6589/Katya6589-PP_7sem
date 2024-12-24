from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog, QTableWidget
)
from PyQt5.uic import loadUi
import sqlite3

from pages.Operator import Operator
from pages.Administator import Administator
from pages.Manager import Manager
from pages.AddStoki import AddStoki

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi ("views/welcomeScreen.ui", self)
        self.Password_q.setEchoMode(QtWidgets.QLineEdit.Password) 
        self.Vxod_q.clicked.connect(self.registaciya) 
        self.back_q.clicked.connect(self.back) 
        self.back_q.hide()
        self.Add_q.clicked.connect(self.add) 
        self.Add_q.hide()
        self.save_q.hide()
        self.save_q.clicked.connect(self.save_func)

        self.stackedWidget.currentChanged.connect(self.hiddenButton)

    def save_func(self):
        ID = self.ID.text()
        print(ID)
        Date_zakaza = self.Date_zakaza.text()
        print(Date_zakaza)
        id_Sostav_tovara = self.id_Sostav_tovara.text()
        print(id_Sostav_tovara)
        Sum = self.Sum.text()
        print(Sum)
        Code_polycheniya = self.Code_polycheniya.text()
        print(Code_polycheniya)
        Id_Terminal = self.Id_Terminal.text()
        print(Id_Terminal)
        id_Klient = self.id_Klient.text()
        print(id_Klient)
       

        conn = sqlite3.connect("BD/Kargo_link.db") #подключение к бд
        cur = conn.cursor() #создаем переменную для хранения запросов
       
        cur.execute(f'''INSERT INTO Talon (ID, Date_zakaza, id_Sostav_tovara, Sum, Code_polycheniya, Id_Terminal, id_Klient) VALUES ({ID}, "{Date_zakaza}", {id_Sostav_tovara}, {Sum}, {Code_polycheniya}, {Id_Terminal}, {id_Klient}) ''') #получаем тип пользователя, логин и пароль которого был введен
        conn.commit() #сохраняет в подключении запросы
        conn.close() #закрывает подключение


    def registaciya(self):
        login = self.Login_q.text()
        password = self.Password_q.text()
        print(login, password)
        if len(login) == 0 or len(password) == 0:
            self.Error_q.setText("Поля должны быть заполнены")
        else:
            self.Error_q.setText(" ")
            conn = sqlite3.connect("BD/Kargo_link.db")
            cur = conn.cursor()
            cur.execute(f'SELECT IDavtorizovan FROM Klient where Login = "{login}" and Password = "{password}"')
            typeUser = cur.fetchone()
            if typeUser == None:
                self.Error_q.setText("Такого пользователя нет")
            elif typeUser[0] == 1:
                self.tableWidget_Klient = self.findChild(QTableWidget, "tableWidget_Operator")
                self.stackedWidget.setCurrentWidget(self.Operator_q)
                self.lybaya = Operator(self.tableWidget_Operator)
            elif typeUser[0] == 2:
                self.tableWidget_Klient = self.findChild(QTableWidget, "tableWidget_Manager")
                self.stackedWidget.setCurrentWidget(self.Manager_q)
                self.lybaya = Manager(self.tableWidget_Manager)
            elif typeUser[0] == 3:
                self.tableWidget_Klient = self.findChild(QTableWidget, "tableWidget_Administator")
                self.stackedWidget.setCurrentWidget(self.Administator_q)
                self.lybaya = Administator(self.tableWidget_Administator)

    def back(self):
        self.stackedWidget.setCurrentWidget(self.Avtorizaciya_q)
        self.lybaya = WelcomeScreen()
    
    def add(self):
        self.stackedWidget.setCurrentWidget(self.AddStoki_q)
        self.lybaya = AddStoki()

    def hiddenButton(self):
        if self.stackedWidget.currentWidget() == self.Avtorizaciya_q:
            self.back_q.hide()
            self.Add_q.hide()
        else:
            self.back_q.show()
            self.Add_q.show()
        if self.stackedWidget.currentWidget() != self.AddStoki_q:
            self.save_q.hide()
        else:
            self.save_q.show()
     