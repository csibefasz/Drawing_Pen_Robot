import serial
import serial.tools.list_ports
from PyQt5.QtCore import QObject, pyqtSignal

class SerialConnection(QObject):
    connection_changed = pyqtSignal(bool)
    data_received = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.serial = None
        self.port = None
        self.baudrate = 115200
        self.connected = False
        
    def list_ports(self):
        return [port.device for port in serial.tools.list_ports.comports()]
    
    def connect(self, port, baudrate):
        try:
            self.serial = serial.Serial(port, baudrate, timeout=1)
            self.connected = True
            self.port = port
            self.baudrate = baudrate
            self.connection_changed.emit(True)
            return True
        except Exception as e:
            print(f"Connection error: {e}")
            return False
    
    def disconnect(self):
        if self.serial and self.serial.is_open:
            self.serial.close()
        self.connected = False
        self.connection_changed.emit(False)
    
    def send_command(self, command):
        if self.connected:
            self.serial.write(f"{command}\n".encode())
    
    def read_response(self):
        if self.connected:
            return self.serial.readline().decode().strip()
        return ""
