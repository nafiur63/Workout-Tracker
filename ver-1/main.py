from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QScrollArea,
                             QLineEdit, QHBoxLayout, QFrame, QPushButton, QLabel, QWidget)

from PyQt5.QtCore import Qt
from datetime import datetime
from db import(create_table, get_all_workouts, insert_workout, update_workout)

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        create_table()

def main():
    app = QApplication([])
    app.setStyle('fusion')
    win = Main()
    win.show()
    app.exec_()

if __name__ == '__main__':
    main()