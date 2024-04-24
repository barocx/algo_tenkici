import pygame
from pygame.sprite import Sprite
import os
file_path = os.path.join(os.path.dirname(__file__), 'assets', 'wall.png')
img = pygame.image.load(file_path)
class Wall(Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = img
        #self.image = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32).convert_alpha()
        #self.image.fill(color)
