from tank import Tank
from enemy_tank import Enemy_Tank
import pygame

class Sprite_Manager:
    def __init__(self, game):
        self.game = game
        self.allsprites = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()

        self._initialize_player_tank()
        self._initialize_enemy_tanks()

    def _initialize_player_tank(self):
        self.tank = Tank(2, 2, self.game)
        self.allsprites.add(self.tank)
        self.player_group.add(self.tank)

    def _initialize_enemy_tanks(self):
        enemy_positions = [(55, 37), (10, 12)]
        for position in enemy_positions:
            enemy_tank = Enemy_Tank(position[0], position[1], self.game)
            self.allsprites.add(enemy_tank)
            self.enemy_group.add(enemy_tank)

    def update(self):
        self.allsprites.update(self.game.wall_manager.allwalls)

    def draw(self, screen):
        self.allsprites.draw(screen)
