class GCodeEngine:
    def __init__(self, machine_params):
        self.machine_params = machine_params
        self.pen_up_pos = 250
        self.pen_down_pos = 0
        self.current_pos = (0, 0)
        self.pen_state = 'up'
        
    def generate_from_path(self, path, feed_rate=8000):
        """Generál G-code-ot vektoros útvonalból"""
        commands = []
        commands.append("G21")  # Millimeter mode
        commands.append("G90")  # Absolute positioning
        commands.append(f"G1 F{feed_rate}")
        
        for point in path:
            if len(point) == 3:  # X, Y, pen state
                x, y, pen = point
            else:  # X, Y
                x, y = point
                pen = None
                
            if pen is not None and pen != self.pen_state:
                if pen == 'down':
                    commands.append(f"M3 S{self.pen_down_pos}")
                    self.pen_state = 'down'
                else:
                    commands.append(f"M3 S{self.pen_up_pos}")
                    self.pen_state = 'up'
                    
            commands.append(f"G1 X{x:.2f} Y{y:.2f}")
            self.current_pos = (x, y)
            
        return "\n".join(commands)
    
    def optimize_path(self, paths, method='nearest_neighbor'):
        """Optimalizálja az útvonalat a rajzolási idő csökkentésére"""
        # Implementálhatsz különböző optimalizálási algoritmusokat
        if method == 'nearest_neighbor':
            return self._nearest_neighbor(paths)
        # Egyéb módszerek...
        
    def _nearest_neighbor(self, paths):
        """Legközelebbi szomszéd algoritmus"""
        if not paths:
            return []
            
        optimized = [paths[0]]
        remaining = paths[1:]
        
        while remaining:
            last_point = optimized[-1][-1] if isinstance(optimized[-1], list) else optimized[-1]
            last_x, last_y = last_point[:2]
            
            # Keresés a legközelebbi pontra
            closest_idx = 0
            closest_dist = float('inf')
            
            for i, path in enumerate(remaining):
                first_point = path[0] if isinstance(path, list) else path
                first_x, first_y = first_point[:2]
                dist = ((first_x - last_x)**2 + (first_y - last_y)**2)**0.5
                
                if dist < closest_dist:
                    closest_dist = dist
                    closest_idx = i
            
            optimized.append(remaining.pop(closest_idx))
            
        return optimized
