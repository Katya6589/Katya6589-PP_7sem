
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QDialog, QTableWidgetItem
)
from PyQt5.uic import loadUi
import sqlite3

class AddStoki(QDialog):
    def __init__(self):
        super(AddStoki, self).__init__()