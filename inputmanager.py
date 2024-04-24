import pygame

class Input_Manager:
    def __init__(self, game):
        self.game = game

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.sprite_manager.tank.shoot()
                elif event.key == pygame.K_KP_5:
                    self.game.sprite_manager.enemy_tank.shoot()
