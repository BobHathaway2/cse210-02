class Player:

    def __init__(self):
        self.hi_low_guess = ""
        self.score = 300
    
    def update_score(self, score):
        self.score += score