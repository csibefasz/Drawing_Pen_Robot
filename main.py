import sys
from PyQt5.QtWidgets import QApplication
from core.machine import Machine
from core.state_manager import StateManager
from ui.main_window import MainWindow

def main():
    # Alkalmazás inicializálása
    app = QApplication(sys.argv)
    
    # Függőségek létrehozása
    machine = Machine()
    state_manager = StateManager()
    
    # Főablak létrehozása
    window = MainWindow(machine, state_manager)
    window.show()
    
    # Alkalmazás indítása
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
