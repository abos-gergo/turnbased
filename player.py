import pygame
import mapgen

class Player:
    def __init__(self, pos: tuple, teamNumber) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.teamNumber = teamNumber
        self.imgx, self.imgy = (32, 64)
        self.imgoffsetx, self.imgoffsety = (self.imgx / 2, self.imgy / 4)
        mapgen.Map.tiles.append(self)
        self.tileBelow = self.getTileBelow()
        print(self.tileBelow.x, self.tileBelow.y)

    def getTileBelow(self):
        for tile in mapgen.Map.tiles:
            if tile.x == self.x and tile.y == self.y:
                return tile
    '''
    def onClick(self):
        self.tileBelow.getNeighbors()
        print(self.tileBelow.neighbors)
        for neighbor in self.tileBelow.neighbors:
            pygame.diplay.blit("Assets/Map/MoveTo.png", (0, 0))'''