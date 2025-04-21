from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QPushButton, QDoubleSpinBox, QGroupBox)

class CalibrationDialog(QDialog):
    def __init__(self, machine, parent=None):
        super().__init__(parent)
        self.machine = machine
        self.setWindowTitle("Robot Kalibrálása")
        self.setModal(True)
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Pozíció kalibrálás
        pos_group = QGroupBox("Pozíció Kalibrálás")
        pos_layout = QVBoxLayout()
        
        # X tengely
        x_layout = QHBoxLayout()
        x_layout.addWidget(QLabel("X Offset:"))
        self.x_spin = QDoubleSpinBox()
        self.x_spin.setRange(-50, 50)
        self.x_spin.setSingleStep(0.1)
        x_layout.addWidget(self.x_spin)
        pos_layout.addLayout(x_layout)
        
        # Y tengely
        y_layout = QHBoxLayout()
        y_layout.addWidget(QLabel("Y Offset:"))
        self.y_spin = QDoubleSpinBox()
        self.y_spin.setRange(-50, 50)
        self.y_spin.setSingleStep(0.1)
        y_layout.addWidget(self.y_spin)
        pos_layout.addLayout(y_layout)
        
        pos_group.setLayout(pos_layout)
        layout.addWidget(pos_group)
        
        # Toll kalibrálás
        pen_group = QGroupBox("Toll Kalibrálás")
        pen_layout = QVBoxLayout()
        
        # Toll fel/le pozíciók
        up_down_layout = QHBoxLayout()
        up_down_layout.addWidget(QLabel("Toll fel pozíció:"))
        self.pen_up_spin = QDoubleSpinBox()
        self.pen_up_spin.setRange(0, 300)
        up_down_layout.addWidget(self.pen_up_spin)
        
        up_down_layout.addWidget(QLabel("Toll le pozíció:"))
        self.pen_down_spin = QDoubleSpinBox()
        self.pen_down_spin.setRange(0, 300)
        up_down_layout.addWidget(self.pen_down_spin)
        
        pen_layout.addLayout(up_down_layout)
        pen_group.setLayout(pen_layout)
        layout.addWidget(pen_group)
        
        # Gombok
        btn_layout = QHBoxLayout()
        self.save_btn = QPushButton("Mentés")
        self.save_btn.clicked.connect(self.save_calibration)
        btn_layout.addWidget(self.save_btn)
        
        self.cancel_btn = QPushButton("Mégse")
        self.cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(self.cancel_btn)
        
        layout.addLayout(btn_layout)
        self.setLayout(layout)
        
        # Betöltjük a jelenlegi beállításokat
        self.load_current_settings()
    
    def load_current_settings(self):
        # Betöltjük a gép jelenlegi kalibrációs értékeit
        # (Ezt a machine osztályból kell lekérni)
        self.x_spin.setValue(self.machine.x_offset)
        self.y_spin.setValue(self.machine.y_offset)
        self.pen_up_spin.setValue(self.machine.pen_up_pos)
        self.pen_down_spin.setValue(self.machine.pen_down_pos)
    
    def save_calibration(self):
        # Mentjük az új kalibrációs értékeket
        self.machine.update_calibration(
            x_offset=self.x_spin.value(),
            y_offset=self.y_spin.value(),
            pen_up_pos=self.pen_up_spin.value(),
            pen_down_pos=self.pen_down_spin.value()
        )
        self.accept()
