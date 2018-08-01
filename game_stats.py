import json
class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        try:
            with open(r"data\data.json") as data:
                self.high_score = json.load(data)
        except FileNotFoundError:
            self.high_score = 0
        print(self.high_score)
        self.level = 1
        #self.score = 0
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
