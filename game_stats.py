class GameStats:

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        self.target_misses_left = self.settings.target_misses_limit



