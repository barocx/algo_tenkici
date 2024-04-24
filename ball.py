import pygame
import math
import os
from random import randint
file_path = os.path.join(os.path.dirname(__file__), 'assets', 'ball.png')
img = pygame.image.load(file_path)

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, direction,game,team=0, speed=5):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect(center=(x, y))
        self.direction=direction
        self.speed = speed
        self.x = x
        self.y = y
        self.bounce_count = 10
        self.team = team
        self.game = game
        self.enemy_group = self.game.enemy_group
        self.player_group = self.game.player_group
    def update(self, walls):
        dx=self.speed * math.cos(math.radians(self.direction))
        self.x += dx
        tempx = self.rect.centerx
        self.rect.centerx = self.x
        switch1 = False
        switch2 = False
        destroyer = False
        if randint(1,100)==5:
            destroyer = True
        else:
            destroyer = False
        if pygame.sprite.spritecollide(self,walls,destroyer):
            self.rect.centerx = tempx
            self.x -= dx
            self.speed = -self.speed
            switch1 = True
        dy = self.speed * math.sin(math.radians(self.direction))
        self.y -= dy
        tempy = self.rect.centery
        self.rect.centery = self.y
        if pygame.sprite.spritecollide(self,walls,destroyer):
            self.rect.centery = tempy
            self.y += dy
            switch2 = True
        if switch2:
            self.direction = -self.direction
        if switch1:
            self.direction = -self.direction
        if self.bounce_count <= 0:
            self.kill()
        if switch1 or switch2:
            self.bounce_count -=1
        self.rect.center = (self.x, self.y)
        if self.team == 1:
            if pygame.sprite.spritecollide(self,self.enemy_group,True):
                pass
        if self.team == 2:
            if pygame.sprite.spritecollide(self,self.player_group,True):
                pass





