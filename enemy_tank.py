import pygame
import math
import os
from ball import Ball
from random import randint
TILE_SIZE = 16
file_path = os.path.join(os.path.dirname(__file__), 'assets', 'enemy_tenk.png')
img = pygame.image.load(file_path)
class Enemy_Tank(pygame.sprite.Sprite):
    def __init__(self, x, y,game, direction=0):
        super().__init__()
        self.original_image = pygame.transform.rotate(img,90)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x*TILE_SIZE, y*TILE_SIZE))
        #self.mask = pygame.mask.from_surface(self.image)
        self.x = x*TILE_SIZE
        self.y = y*TILE_SIZE
        self.direction = direction
        self.speed=1.2
        self.rotation_speed=1
        self.game = game
        self.forward_dir = True
        self.right_dir = True

    def forward(self,walls):
        dx=self.speed * math.cos(math.radians(self.direction))
        self.x += dx
        tempx = self.rect.centerx
        self.rect.centerx = self.x
        if pygame.sprite.spritecollide(self,walls,False):
            self.rect.centerx = tempx
            self.x -= dx

        dy = self.speed * math.sin(math.radians(self.direction))
        self.y -= dy
        tempy = self.rect.centery
        self.rect.centery = self.y
        if pygame.sprite.spritecollide(self,walls,False):
            self.rect.centery = tempy
            self.y += dy
        self.rect.center = (self.x, self.y)
    def backward(self,walls):
        dx=self.speed * math.cos(math.radians(self.direction))
        self.x -= dx
        tempx = self.rect.centerx
        self.rect.centerx = self.x
        if pygame.sprite.spritecollide(self,walls,False):
            self.rect.centerx = tempx
            self.x += dx

        dy = self.speed * math.sin(math.radians(self.direction))
        self.y += dy
        tempy = self.rect.centery
        self.rect.centery = self.y
        if pygame.sprite.spritecollide(self,walls,False):
            self.rect.centery = tempy
            self.y -= dy

        self.rect.center = (self.x, self.y)

    def rotate_right(self,walls):
        self.rotate(self.rotation_speed)
        if pygame.sprite.spritecollide(self,walls,False):
            self.rotate(-self.rotation_speed)

    def rotate_left(self,walls):
        self.rotate(-self.rotation_speed)
        if pygame.sprite.spritecollide(self,walls,False):
            self.rotate(self.rotation_speed)
    def move(self,walls):
        self.direction = self.calculate_angle((self.x,self.y),
                                              (self.game.sprite_manager.tank.x,
                                               self.game.sprite_manager.tank.y))
        self.rotate_right(walls)
        self.forward(walls)
        
        #if randint(1,40)== 3:
            #self.shoot()
    def calculate_angle(self,player_pos, target_pos):
        dx = target_pos[0] - player_pos[0]
        dy = target_pos[1] - player_pos[1]
        return math.degrees(math.atan2(-dy, dx))
                
    def shoot(self):
        self.game.allsprites.add(Ball(self.x,self.y,self.direction,self.game,team = 2))

    def rotate(self, angle):
        self.direction -= angle
        self.image = pygame.transform.rotate(self.original_image, self.direction)
        #self.mask = pygame.mask.from_surface(self.image)

    def update(self,walls):
        self.move(walls)
        

        