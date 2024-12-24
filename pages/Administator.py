from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog, QTableWidgetItem
)
from PyQt5.uic import loadUi
import sqlite3

class Administator(QDialog):
    def __init__(self, table):
        super(Administator, self).__init__()
        self.tableWidget_Administator = table 
        self.vivod()
    
    def vivod(self):
        conn = sqlite3.connect("BD/Kargo_link.db") 
        cur = conn.cursor()
        
        zayavki = cur.execute(f'''SELECT
        t.ID as "Номер заказа",
        t.Date_zakaza as "Дата заказа", tov. Naimenovanie as "Наименование товара",
        t. Sum as "Сумма заказов",
        t.Code_polycheniya as "Код получения",
        ter.Adress as "Адрес терминала",
        k.FIO as "ФИО клиента",
        k.Phone as "Номер клиента"
        from Talon t
        LEFT JOIN
        Sostav_tovara s on t.id_Sostav_tovara= s.ID_code
        LEFT JOIN
        Tovar tov on s.id_tovara = tov.ID
        LEFT JOIN
        Terminal ter on t.Id_Terminal = ter. ID
        LEFT JOIN Klient k on t.id_Klient = k.ID
        LEFT JOIN
        Klient kl on t.id_Klient = kl.ID''')

        name_stolba = [xz[0] for xz in zayavki.description] 
        print(name_stolba)

        self.tableWidget_Administator.setColumnCount(len(name_stolba)) 
        self.tableWidget_Administator.setHorizontalHeaderLabels(name_stolba) 

        dan_table= cur.fetchall()
        
        self.tableWidget_Administator.setRowCount(0) 
        # row - строки
        for i, row in enumerate(dan_table): #цикл по строкам
            self.tableWidget_Administator.setRowCount(self.tableWidget_Administator.rowCount() + 1) 
            for l, cow in enumerate(row): #начинает по ячейке заносить данные
                self.tableWidget_Administator.setItem(i,l,QTableWidgetItem(str(cow))) 
        print(dan_table)

        self.tableWidget_Administator.resizeColumnsToContents() 
        conn.commit()
        conn.close()