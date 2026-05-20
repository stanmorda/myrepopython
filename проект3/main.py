import sys
import sqlite3
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QComboBox, 
                             QPushButton, QTableWidget, QTableWidgetItem, QMessageBox)
from PyQt6.QtCore import Qt


# 1. Добавление записи (заработок(карманные деньги, работа по дому, помощь другу), трата(еда, развлечение, подарки)). 

class FinanceManager(QMainWindow):
    def __init__(self):
        self.categoies = {
            "Расход":["еда", "развлечения", "подарки"],
            "Доход":["зарплата", "подарки"]
        }
        
        super().__init__()
        self.resize(650, 450)
        self.setWindowTitle('FinanceManager')
        
        self.init_db()
        self.init_ui()
        
        self.update_categories()
        self.load_data()
        
    def init_db(self):
        self.conn = sqlite3.connect('finance.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS transactions (
                                type TEXT,
                                amount REAL,
                                category TEXT,
                                description TEXT
                            )
        ''')
        self.conn.commit()
        pass
    
    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        
        input_layout = QHBoxLayout()
        self.type_cb = QComboBox()
        self.type_cb.addItems(['Расход', 'Доход'])
        self.type_cb.currentTextChanged.connect(self.update_categories)
        
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText('Amount')
        
        self.categoies_cb = QComboBox()
        
        self.desc_input = QLineEdit()
        self.desc_input.setPlaceholderText('Description')
        
        self.add_btn = QPushButton('+')
        self.add_btn.clicked.connect(self.add_transaction)
        
        input_layout.addWidget(self.type_cb)
        input_layout.addWidget(self.amount_input)
        input_layout.addWidget(self.categoies_cb)
        input_layout.addWidget(self.desc_input)
        input_layout.addWidget(self.add_btn)
        
        main_layout.addLayout(input_layout)
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['Type', 'Amount', 'Category', 'Description'])
        self.table.horizontalHeader().setStretchLastSection(True)
        main_layout.addWidget(self.table)
        
        self.balance_label = QLabel('Balance: 0')
        self.balance_label.setStyleSheet('font-size: 18px; font-weight: bold;')
        main_layout.addWidget(self.balance_label)
    
    def update_categories(self):
        current = self.type_cb.currentText()
        self.categoies_cb.clear()
        self.categoies_cb.addItems(self.categoies[current])
    
    def add_transaction(self):
        operation_type = self.type_cb.currentText()
        amount = self.amount_input.text()
        category = self.categoies_cb.currentText()
        desc = self.desc_input.text()
        
        if not amount or int(amount)<=0:
            QMessageBox.warning(self, 'Error', 'Enter amount please!')
            return

        self.cursor.execute('''
                            INSERT INTO transactions (
                                type,
                                amount,
                                category,
                                description)
                            VALUES (?,?,?,?)
                            ''', (operation_type, amount,category,desc))
        self.conn.commit()
        
        self.amount_input.clear()
        self.desc_input.clear()
        self.load_data()

    def load_data(self):
        self.table.setRowCount(0)
        self.cursor.execute('''
                            SELECT type,
                                amount,
                                category,
                                description
                            FROM transactions
                            ''')
        balance = 0
        rows = self.cursor.fetchall()
        
        for number, data in enumerate(rows):
            self.table.insertRow(number)
            
            type = data[0]
            amount = data[1]
            
            if type == 'Доход':
                balance += amount
            else:
                balance -= amount
            
            for c_number, c_data in enumerate(data):
                item = QTableWidgetItem(str(c_data))
                self.table.setItem(number, c_number, item)
        
        self.balance_label.setText(f'Balance: {balance} руб.')
            
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FinanceManager()
    window.show()
    sys.exit(app.exec())