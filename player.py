### player.py
### Player class for tictactoe

# -----

class Player:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.score = 0
    
    def __repr__(self):
        return str(f"{self.name} {self.pos} {self.score}")
        
    def update_score(self):
        self.score += 1
    
    def get_name(self):
        return self.name
    
    def get_pos(self):
        return self.pos
    
    def get_score(self):
        return self.score
    