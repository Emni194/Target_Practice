import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manage bullets"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.width = 10
        self.height = 10
        self.color = (60,60,60)
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.midright = ai_game.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
