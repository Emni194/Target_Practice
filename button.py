import pygame
import pygame.font

class Button:
    """Create a button to start game"""

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()
        self.color = (50,50,50)
        self.height = 100
        self.width = 200
        self.rect = self.screen.get_rect()
        self.font = pygame.font.SysFont(None, 32)
        self.font_color = (200, 250, 150)
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.font_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

