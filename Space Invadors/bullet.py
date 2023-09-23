import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullet fired from the ship."""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ships current position"""
        super(Bullet, self).__init__()
        self.screen = screen
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet.heigt)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

