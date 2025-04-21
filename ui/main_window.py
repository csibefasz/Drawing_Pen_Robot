from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QSplitter, QStatusBar, QLabel)
from PyQt5.QtCore import Qt
from .connection_panel import ConnectionPanel
from .control_panel import ControlPanel  # ÚJ IMPORT
from .drawing_canvas import DrawingCanvas
from .gcode_console import GCodeConsole
from core.machine import Machine
from core.state_manager import StateManager
from core.serial_connection import SerialConnection

class MainWindow(QMainWindow):
    def __init__(self, machine, state_manager, parent=None):
        super().__init__(parent)
        self.machine = machine
        self.state_manager = state_manager
        self.serial_connection = SerialConnection()
        
        self.setWindowTitle("Rajzoló Robot Vezérlő")
        self.setGeometry(100, 100, 1200, 800)
        
        # Fő widget és layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        
        # Bal oldali panel (kapcsolati panel + vezérlőpult)
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        self.connection_panel = ConnectionPanel(self.serial_connection)
        left_layout.addWidget(self.connection_panel)
        
        # Vezérlőpult hozzáadása
        self.control_panel = ControlPanel(self.machine, self.serial_connection)
        left_layout.addWidget(self.control_panel)
        left_layout.addStretch()
        
        # Jobb oldali panel (rajzfelület + konzol)
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        self.drawing_canvas = DrawingCanvas(self.machine, self.serial_connection)
        right_layout.addWidget(self.drawing_canvas)
        self.gcode_console = GCodeConsole(self.serial_connection)
        right_layout.addWidget(self.gcode_console)
        
        # Splitter a reszponzív elrendezéshez
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([300, 700])
        main_layout.addWidget(splitter)
        
        # Állapotsor
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Kész a használatra")
