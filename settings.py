import pygame

class Settings:

    def __init__(self):
        """Initialize the game static settings"""
        self.screen_height = 1920
        self.screen_width = 1024
        self.bg_color = (255,255,255)
        self.rectangle_speed = 1
        self.rectangle_direction = 1
        self.ship_speed = 10
        self.bullet_speed = 10
        self.bullets_allowed = 1
        self.target_misses_limit = 3
        self.initialize_dynamic_settings()
        self.speedup_scale = 1.1

    def initialize_dynamic_settings(self):
        self.bullet_speed = 10
        self.ship_speed = 10
        self.rectangle_speed = 1

    def increase_speed(self):

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.rectangle_speed *= self.speedup_scale




