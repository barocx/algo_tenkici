from wall import Wall
import os
import json
import pygame
#Used for making, drawing and loading walls structure
class Wall_Manager():
    def __init__(self,grid_size,tile_size):
        self.tile_size = tile_size
        self.allwalls = pygame.sprite.Group()
        self.grid_size = grid_size
        self.load_walls()
    def create_wall(self, x, y, width=1, height=1, color=(0,0,0)):
        wall = Wall(x * self.tile_size, 
                    y * self.tile_size, 
                    width * self.tile_size, 
                    height * self.tile_size, 
                    color)
        self.allwalls.add(wall)
    def load_walls(self,mapjson = 'purple_map.json'):
        file_path = os.path.join(os.path.dirname(__file__), 'tiled_info', mapjson)
        with open(file_path, 'r') as f:
            json_data = json.load(f)
        layer_data = list(json_data.get("layers", [])[0].get("data", []))
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                if layer_data[i+self.grid_size[0]*j]==1:
                    self.create_wall(i,j)
    def draw_walls(self,screen):
        self.allwalls.draw(screen)