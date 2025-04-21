import sys
from PyQt5.QtWidgets import QApplication
from core.machine import Machine
from core.state_manager import StateManager
from ui.main_window import MainWindow

def test_integration():
    app = QApplication(sys.argv)
    
    # Függőségek létrehozása
    machine = Machine()
    state_manager = StateManager()
    
    # Főablak létrehozása
    window = MainWindow(machine, state_manager)
    window.show()
    
    # Teszteljük a kapcsolódást
    connection_panel = window.findChild(QWidget, "connection_panel")
    if connection_panel:
        print("Kapcsolati panel megtalálva")
        
    # Alkalmazás futtatása
    sys.exit(app.exec_())

if __name__ == "__main__":
    test_integration()

