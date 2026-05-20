import sys
import json
import os
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QComboBox, QLabel, QPushButton, QFrame)
from PyQt6.QtGui import QDoubleValidator, QFont
from PyQt6.QtCore import Qt

class ModernLocalConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.rates = {}
        self.file_path = "rates.json"
        self.initUI()
        self.load_from_file()

    def initUI(self):
        self.setWindowTitle("Apex Converter")
        self.setFixedWidth(380)
        self.setMinimumHeight(480)
        
        # Стилизация в стиле Modern Dark (неоновый фиолетовый акцент)
        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: #f8fafc;
                font-family: 'Segoe UI', sans-serif;
            }
            QLabel#title {
                color: #94a3b8;
                font-size: 11px;
                font-weight: bold;
                text-transform: uppercase;
                letter-spacing: 1px;
                margin-top: 10px;
            }
            QLineEdit {
                background-color: #1e293b;
                border: 2px solid #334155;
                border-radius: 8px;
                padding: 12px;
                color: #ffffff;
                font-size: 18px;
                font-weight: bold;
            }
            QLineEdit:focus {
                border: 2px solid #8b5cf6;
            }
            QComboBox {
                background-color: #1e293b;
                border: 2px solid #334155;
                border-radius: 8px;
                padding: 10px;
                color: #f8fafc;
                font-weight: bold;
            }
            QComboBox::drop-down {
                border: 0px;
            }
            QPushButton {
                background-color: #8b5cf6;
                color: white;
                border-radius: 8px;
                padding: 14px;
                font-weight: bold;
                font-size: 13px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #a78bfa;
            }
            QPushButton#refresh {
                background-color: transparent;
                border: 1px solid #334155;
                color: #94a3b8;
            }
            QPushButton#refresh:hover {
                border: 1px solid #8b5cf6;
                color: #f8fafc;
            }
            QLabel#result {
                font-size: 42px;
                font-weight: 800;
                color: #22c55e;
                margin: 10px 0;
            }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(8)

        # Поле ввода
        layout.addWidget(QLabel("Сумма для обмена", objectName="title"))
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("0.00")
        self.amount_input.setValidator(QDoubleValidator(0.0, 10**12, 2))
        self.amount_input.textChanged.connect(self.convert)
        layout.addWidget(self.amount_input)

        # Направление
        layout.addWidget(QLabel("Направление", objectName="title"))
        combo_layout = QHBoxLayout()
        self.from_box = QComboBox()
        self.to_box = QComboBox()
        
        self.from_box.currentTextChanged.connect(self.convert)
        self.to_box.currentTextChanged.connect(self.convert)
        
        combo_layout.addWidget(self.from_box)
        label_arrow = QLabel("→")
        label_arrow.setStyleSheet("font-size: 20px; color: #475569;")
        combo_layout.addWidget(label_arrow)
        combo_layout.addWidget(self.to_box)
        layout.addLayout(combo_layout)

        # Результат
        layout.addSpacing(20)
        self.result_label = QLabel("0.00")
        self.result_label.setObjectName("result")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result_label)

        # Декоративная линия
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet("background-color: #334155; max-height: 1px;")
        layout.addWidget(line)

        # Кнопка обновления
        self.refresh_btn = QPushButton("Обновить данные из файла")
        self.refresh_btn.setObjectName("refresh")
        self.refresh_btn.clicked.connect(self.load_from_file)
        layout.addWidget(self.refresh_btn)

        # Статус
        self.status_label = QLabel("Rates ready")
        self.status_label.setStyleSheet("color: #475569; font-size: 10px;")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def load_from_file(self):
        if not os.path.exists(self.file_path):
            self.status_label.setText("JSON NOT FOUND")
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.rates = json.load(f)
            
            cur_f, cur_t = self.from_box.currentText(), self.to_box.currentText()
            self.from_box.clear()
            self.to_box.clear()
            self.from_box.addItems(self.rates.keys())
            self.to_box.addItems(self.rates.keys())
            
            if cur_f in self.rates: self.from_box.setCurrentText(cur_f)
            if cur_t in self.rates: self.to_box.setCurrentText(cur_t)

            self.status_label.setText(f"DATABASE UPDATED")
            self.convert()
        except:
            self.status_label.setText("JSON ERROR")

    def convert(self):
        text = self.amount_input.text().replace(",", ".")
        if not text or not self.rates:
            self.result_label.setText("0.00")
            return
        try:
            val = float(text)
            res = (val * self.rates[self.from_box.currentText()]) / self.rates[self.to_box.currentText()]
            self.result_label.setText(f"{res:,.2f}".replace(",", " "))
        except:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernLocalConverter()
    window.show()
    sys.exit(app.exec())
