from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QTextEdit, QLineEdit, 
                             QPushButton, QHBoxLayout)
from PyQt5.QtCore import Qt, pyqtSignal

class GCodeConsole(QWidget):
    command_sent = pyqtSignal(str)
    
    def __init__(self, serial_connection, parent=None):
        super().__init__(parent)
        self.serial = serial_connection
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Kimeneti konzol
        self.output_console = QTextEdit()
        self.output_console.setReadOnly(True)
        layout.addWidget(self.output_console)
        
        # Bemeneti sor
        input_layout = QHBoxLayout()
        self.input_line = QLineEdit()
        self.input_line.returnPressed.connect(self.send_command)
        input_layout.addWidget(self.input_line)
        
        self.send_btn = QPushButton("Küldés")
        self.send_btn.clicked.connect(self.send_command)
        input_layout.addWidget(self.send_btn)
        
        layout.addLayout(input_layout)
        self.setLayout(layout)
        
        # Soros kapcsolat eseményeinek figyelése
        self.serial.data_received.connect(self.append_output)
    
    def send_command(self):
        command = self.input_line.text()
        if command:
            self.serial.send_command(command)
            self.append_output(f"> {command}")
            self.input_line.clear()
    
    def append_output(self, text):
        self.output_console.append(text)
        self.output_console.ensureCursorVisible()
