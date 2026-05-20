import sys
import sqlite3
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox, QListWidget)


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Вход в приложение.')
        self.resize(300, 150)
        
        layout = QVBoxLayout()
        
        self.login_input = QLineEdit(placeholderText='Login')
        self.password_input = QLineEdit(placeholderText='Password', echoMode=QLineEdit.EchoMode.Password)

        self.button_login = QPushButton('Ok')
        self.button_login.clicked.connect(self.check_login)
         
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.button_login)
        
        self.setLayout(layout)
    
    def check_login(self):
        login = self.login_input.text()
        password = self.password_input.text()
        if login == "1" and password == "1":
            self.manager = PasswordManager()
            self.manager.show()
            self.close()
        else:
            QMessageBox.critical(self, "Error", "Bad login or password")
            
class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()
        self.init_database()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('My superb password manager!')
        self.setMinimumWidth(400)
        self.setMinimumHeight(400)
        layout = QVBoxLayout()
        
        self.login_input = QLineEdit(placeholderText='Login')
        self.password_input = QLineEdit(placeholderText='Password', echoMode=QLineEdit.EchoMode.Password)
        
        self.addButton = QPushButton('Save')
        self.addButton.clicked.connect(self.add_password)
        self.list_widget = QListWidget()
        
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.addButton)
        layout.addWidget(self.list_widget)
        self.load_data_from_database()
        self.setLayout(layout)
        
    def add_password(self):
        login = self.login_input.text()
        password = self.password_input.text()
        if login != '' and password != '':
            self.cursor.execute("INSERT INTO accounts VALUES (?, ?)", (login, password))
            self.conn.commit()
            self.load_data_from_database()
    
    def load_data_from_database(self):
        self.list_widget.clear()
        self.cursor.execute("SELECT login_name FROM accounts")
        for row in self.cursor.fetchall():
            self.list_widget.addItem(row[0])

    def init_database(self):
        self.conn = sqlite3.connect('passwords.db') 
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS accounts (login_name TEXT, password TEXT)")
        self.conn.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec())