import pygame
import math
import os
from ball import Ball

TILE_SIZE = 24
file_path = os.path.join(os.path.dirname(__file__), 'assets', 'tenk.png')
img = pygame.image.load(file_path)
class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y,game, direction=0):
        super().__init__()
        self.original_image = pygame.transform.rotate(img,90)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x*TILE_SIZE, y*TILE_SIZE))
        #self.mask = pygame.mask.from_surface(self.image)
        self.x = x*TILE_SIZE
        self.y = y*TILE_SIZE
        self.direction = direction
        self.speed=3
        self.rotation_speed=3
        self.game = game


    def move(self,walls):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
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
        if keys[pygame.K_s]:
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
        
        if keys[pygame.K_d]:
            self.rotate(self.rotation_speed)
            if pygame.sprite.spritecollide(self,walls,False):
                self.rotate(-self.rotation_speed)
        if keys[pygame.K_a]:
            self.rotate(-self.rotation_speed)
            if pygame.sprite.spritecollide(self,walls,False):
                self.rotate(self.rotation_speed)
                
    def shoot(self):
        self.game.sprite_manager.allsprites.add(Ball(self.x,self.y,self.direction,self.game.sprite_manager,team=1))

    def rotate(self, angle):
        self.direction -= angle % 360
        self.image = pygame.transform.rotate(self.original_image, self.direction)

    def update(self,walls):
        self.move(walls)
        

        