class Machine:
    def __init__(self):
        self.x_offset = 0
        self.y_offset = 0
        self.pen_up_pos = 250
        self.pen_down_pos = 0
        self.max_x = 290  # mm
        self.max_y = 248  # mm
        self.current_pos = (0, 0)
        
    def update_calibration(self, x_offset, y_offset, pen_up_pos, pen_down_pos):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.pen_up_pos = pen_up_pos
        self.pen_down_pos = pen_down_pos
        
    def validate_position(self, x, y):
        """Ellenőrzi, hogy a pozíció a munkaterületen belül van-e"""
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y
