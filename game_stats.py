

class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.read_high_score()

    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def read_high_score(self):
        with open('high_score.txt') as file:
            high_score = file.read()
        self.high_score = int(high_score)
