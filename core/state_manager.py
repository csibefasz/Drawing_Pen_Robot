import json
from pathlib import Path

class StateManager:
    def __init__(self):
        self.config_path = Path("config.json")
        self.settings = {
            "connection": {
                "port": None,
                "baudrate": 115200
            },
            "calibration": {
                "x_offset": 0,
                "y_offset": 0,
                "pen_up": 250,
                "pen_down": 0
            }
        }
        self.load_settings()
        
    def load_settings(self):
        if self.config_path.exists():
            with open(self.config_path, 'r') as f:
                self.settings = json.load(f)
                
    def save_settings(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.settings, f, indent=4)
