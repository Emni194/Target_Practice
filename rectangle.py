import pygame
from pygame.locals import *

class Rectangle:
    """Overall class to manage rectangle object"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()
        self.rectangle_width, self.rectangle_height = 100, 100
        self.rectangle_color = (0, 0, 255)
        self.rect = pygame.Rect(0, 0, self.rectangle_width,
                                self.rectangle_height)
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        self.y += self.settings.rectangle_speed * self.settings.rectangle_direction
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.rectangle_color, self.rect)



