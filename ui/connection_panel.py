from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                             QComboBox, QPushButton, QSpinBox)
from PyQt5.QtCore import Qt
from core.serial_connection import SerialConnection  # Új import

class ConnectionPanel(QWidget):
    def __init__(self, serial_connection, parent=None):  # Módosított paraméter
        super().__init__(parent)
        self.connection = serial_connection  # SerialConnection példányt vár
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Port választó
        port_layout = QHBoxLayout()
        port_layout.addWidget(QLabel("Port:"))
        self.port_combo = QComboBox()
        self.refresh_ports()
        port_layout.addWidget(self.port_combo)
        
        # Frissítés gomb
        self.refresh_btn = QPushButton("Frissítés")
        self.refresh_btn.clicked.connect(self.refresh_ports)
        port_layout.addWidget(self.refresh_btn)
        layout.addLayout(port_layout)
        
        # Baudrate
        baud_layout = QHBoxLayout()
        baud_layout.addWidget(QLabel("Baudrate:"))
        self.baud_spin = QSpinBox()
        self.baud_spin.setRange(9600, 115200)
        self.baud_spin.setValue(115200)
        baud_layout.addWidget(self.baud_spin)
        layout.addLayout(baud_layout)
        
        # Kapcsolódás gomb
        self.connect_btn = QPushButton("Kapcsolódás")
        self.connect_btn.clicked.connect(self.toggle_connection)
        layout.addWidget(self.connect_btn)
        
        self.setLayout(layout)
    
    def refresh_ports(self):
        self.port_combo.clear()
        ports = self.connection.list_ports()
        self.port_combo.addItems(ports)
        
    def toggle_connection(self):
        if self.connection.connected:
            self.connection.disconnect()
            self.connect_btn.setText("Kapcsolódás")
        else:
            port = self.port_combo.currentText()
            baudrate = self.baud_spin.value()
            self.connection.connect(port, baudrate)
            self.connect_btn.setText("Kapcsolat bontása")
