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

    def initUI(self):
        self.setWindowTitle("Apex Converter")
        self.setFixedWidth(380)
        self.setMinimumHeight(480)
    

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(8)

        # Поле ввода
        layout.addWidget(QLabel("Сумма для обмена", objectName="title"))
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("0.00")
        self.amount_input.setValidator(QDoubleValidator(0.0, 10**12, 2))

        layout.addWidget(self.amount_input)

        # Направление
        layout.addWidget(QLabel("Направление", objectName="title"))
        
        combo_layout = QHBoxLayout()
        self.from_box = QComboBox()
        self.to_box = QComboBox()
        label_arrow = QLabel("→")
        
        combo_layout.addWidget(self.from_box)
        combo_layout.addWidget(label_arrow)
        combo_layout.addWidget(self.to_box)
        
        layout.addLayout(combo_layout)

    

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernLocalConverter()
    window.show()
    sys.exit(app.exec())
