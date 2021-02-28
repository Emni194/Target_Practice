from time import sleep

import pygame
import sys
from rectangle import Rectangle
from settings import Settings
from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from button import Button


class TargetPractice:
    """Overall class to manage simple game"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        self.caption = pygame.display.set_caption("Target Practice")
        self.rectangle = Rectangle(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.button = Button(self, "Play")

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self._update_rectangle()
                self._update_bullet()
                self.ship.update()
            self._update_screen()

    def _check_rectangle_edges(self):
        if self.rectangle.check_edges():
            self._change_rectangle_direction()

    def _change_rectangle_direction(self):
        self.settings.rectangle_direction *= -1

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rectangle.draw()
        if not self.stats.game_active:
            self.button.draw_button()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _update_rectangle(self):
        self.rectangle.update()
        self._check_rectangle_edges()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            self._check_bullet_rectangle_collision()
        for bullet in self.bullets:
            if bullet.rect.right >= self.settings.screen_height:
                self.bullets.remove(bullet)
                self.stats.target_misses_left -= 1
            if self.stats.target_misses_left == 0:
                self.stats.game_active = False
                pygame.mouse.set_visible(True)

    def _check_bullet_rectangle_collision(self):
        if pygame.sprite.spritecollideany(self.rectangle, self.bullets):
            self.bullets.empty()
            self.settings.increase_speed()
            sleep(0.2)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_button(mouse_pos)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _check_button(self, mouse_pos):
        if self.button.rect.collidepoint(mouse_pos):
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self._start_game()
            pygame.mouse.set_visible(False)

    def _start_game(self):
        self.stats.reset_stats()
        self.bullets.empty()
        self.rectangle.draw()
        self.ship.center_ship()


if __name__ == '__main__':
    ai = TargetPractice()
    ai.run_game()
