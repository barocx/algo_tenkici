import pygame
from wallmanager import Wall_Manager
from spritemanager import Sprite_Manager
from inputmanager import Input_Manager
from settings import *
class Game:
    def __init__(self, grid_size, tile_size):
        self.grid_size = grid_size
        self.tile_size = tile_size
        self.width = grid_size[0] * tile_size
        self.height = grid_size[1] * tile_size
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.wall_manager = Wall_Manager(self.grid_size,self.tile_size)
        self.sprite_manager = Sprite_Manager(self)
        self.input_manager = Input_Manager(self)
        print("Game started")
        self.running = True
    def run(self):
        
        while self.running:
            self.input_manager.handle_input()
            self.screen.fill(DARK_CYAN)  
            self.wall_manager.draw_walls(self.screen)
            self.sprite_manager.update()
            self.sprite_manager.draw(self.screen)
            pygame.display.update() 
            self.clock.tick(FPS)  

        pygame.quit()

if __name__ == "__main__":
    pygame.init()
    game = Game((TILES_X, TILES_Y), TILE_SIZE)
    game.run()

