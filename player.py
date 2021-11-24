import pygame
import map
import engine
import tiles

class Player:
    def __init__(self, teamNumber, SCALE) -> None:
        self.x = SCALE / 2
        self.y = SCALE / 2
        self.z = 1
        self.tile_type = ''
        self.anchor_y = 0
        self.move_direction = pygame.math.Vector3(0, 0, 0)
        self.render_dir = pygame.math.Vector3(0, 0, 0)
        self.move_speed: float = 0.07
        self.player_types = (pygame.image.load('Assets/Player/Melee/Character01/character01-front-left.png'), pygame.image.load('Assets/Player/Melee/Character01/character01-front-right.png'), pygame.image.load('Assets/Player/Melee/Character01/character01-back-left.png'), pygame.image.load('Assets/Player/Melee/Character01/character01-back-right.png'))
        self.teamNumber = teamNumber
        self.middle_offset = 1/self.player_types[0].get_width()*2
        self.prev_player_type = self.player_types[0]
        self.look_dir = pygame.math.Vector2(0, 1)

    def getTileBelow(self):
        return map.none_matrix[round(self.y)][round(self.x)]
    
    def get_tile_type(self):
        if self.move_direction.x == 1:
            self.prev_player_type = self.player_types[1]
            self.look_dir.x, self.look_dir.y = 1, 0
            return self.player_types[1]
        
        elif self.move_direction.x == -1:
            self.prev_player_type = self.player_types[2]
            self.look_dir.x, self.look_dir.y = -1, 0
            return self.player_types[2]
        
        elif self.move_direction.y == 1:
            self.prev_player_type = self.player_types[0]
            self.look_dir.x, self.look_dir.y = 0, 1
            return self.player_types[0]
        
        elif self.move_direction.y == -1:
            self.prev_player_type = self.player_types[3]
            self.look_dir.x, self.look_dir.y = 0, -1
            return self.player_types[3]
        else:
            return self.prev_player_type
    
    def move(self):
        if round(self.x + 5*self.move_direction.x*self.move_speed) != self.getTileBelow().x or round(self.y + 5*self.move_direction.y*self.move_speed) != self.getTileBelow().y:
            if map.none_matrix[round(self.y) + int(self.move_direction.y)][round(self.x) + int(self.move_direction.x)] == None or map.enviroment_matrix[round(self.y) + int(self.move_direction.y)][round(self.x) + int(self.move_direction.x)] != None:
                self.x -= self.move_direction.x*self.move_speed
                self.y -= self.move_direction.y*self.move_speed

        self.x += self.move_direction.x*self.move_speed
        self.y += self.move_direction.y*self.move_speed

    def create_bridge(self):
        if engine.collide(self, map.none_matrix) == None and self.getTileBelow().x + int(self.look_dir.x) < len(map.none_matrix) and self.getTileBelow().y + int(self.look_dir.y) < len(map.none_matrix):
            map.none_matrix[self.getTileBelow().y + int(self.look_dir.y)][self.getTileBelow().x + int(self.look_dir.x)] = tiles.Bridge((self.getTileBelow().x + int(self.look_dir.x), self.getTileBelow().y + int(self.look_dir.y), 1))
            map.dirt_matrix.append(tiles.Bridge((self.getTileBelow().x + int(self.look_dir.x), self.getTileBelow().y + int(self.look_dir.y), 1)))