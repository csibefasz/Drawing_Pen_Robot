from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, 
                             QPushButton, QLabel, QSpinBox)
from PyQt5.QtCore import Qt

class ControlPanel(QWidget):
    def __init__(self, machine, serial_connection, parent=None):
        super().__init__(parent)
        self.machine = machine
        self.serial = serial_connection
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Mozgató gombok
        move_group = QGroupBox("Kézi vezérlés")
        move_layout = QVBoxLayout()
        
        # X tengely
        x_layout = QHBoxLayout()
        self.x_minus_btn = QPushButton("X-")
        self.x_minus_btn.clicked.connect(lambda: self.move_relative(-10, 0))
        x_layout.addWidget(self.x_minus_btn)
        
        self.x_plus_btn = QPushButton("X+")
        self.x_plus_btn.clicked.connect(lambda: self.move_relative(10, 0))
        x_layout.addWidget(self.x_plus_btn)
        move_layout.addLayout(x_layout)
        
        # Y tengely
        y_layout = QHBoxLayout()
        self.y_minus_btn = QPushButton("Y-")
        self.y_minus_btn.clicked.connect(lambda: self.move_relative(0, -10))
        y_layout.addWidget(self.y_minus_btn)
        
        self.y_plus_btn = QPushButton("Y+")
        self.y_plus_btn.clicked.connect(lambda: self.move_relative(0, 10))
        y_layout.addWidget(self.y_plus_btn)
        move_layout.addLayout(y_layout)
        
        move_group.setLayout(move_layout)
        layout.addWidget(move_group)
        
        # Toll vezérlés
        pen_group = QGroupBox("Toll vezérlés")
        pen_layout = QHBoxLayout()
        
        self.pen_up_btn = QPushButton("Toll fel")
        self.pen_up_btn.clicked.connect(self.pen_up)
        pen_layout.addWidget(self.pen_up_btn)
        
        self.pen_down_btn = QPushButton("Toll le")
        self.pen_down_btn.clicked.connect(self.pen_down)
        pen_layout.addWidget(self.pen_down_btn)
        
        pen_group.setLayout(pen_layout)
        layout.addWidget(pen_group)
        
        # Kezdőpozíció
        home_group = QGroupBox("Pozíciók")
        home_layout = QHBoxLayout()
        
        self.home_btn = QPushButton("Kezdőpozíció")
        self.home_btn.clicked.connect(self.go_home)
        home_layout.addWidget(self.home_btn)
        
        self.stop_btn = QPushButton("STOP")
        self.stop_btn.setStyleSheet("background-color: red; color: white;")
        self.stop_btn.clicked.connect(self.emergency_stop)
        home_layout.addWidget(self.stop_btn)
        
        home_group.setLayout(home_layout)
        layout.addWidget(home_group)
        
        self.setLayout(layout)
    
    def move_relative(self, dx, dy):
        """Relatív mozgatás"""
        cmd = f"G91\nG0 X{dx} Y{dy}\nG90"
        self.serial.send_command(cmd)
    
    def pen_up(self):
        self.serial.send_command("M3 S250")
    
    def pen_down(self):
        self.serial.send_command("M3 S0")
    
    def go_home(self):
        self.serial.send_command("G0 X0 Y0")
    
    def emergency_stop(self):
        self.serial.send_command("M112")
