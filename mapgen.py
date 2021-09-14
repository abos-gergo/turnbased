from player import Player
from typing import List
import numpy
import engine
import main
import pygame
import camera


class Tile:
    def __init__(self, pos: tuple) -> None:
        self.x, self.y, self.z = pos
        self.neighbors: List[tuple] = []
        self.imgx, self.imgy = (64, 32)

    def getNeighbors(self, map):
        neighborspos: List[tuple] = []
        neighbors: List[bool] = [0, 0, 0, 0]
        for neighbor in Map.tiles:
            if engine.tileDistance(self, neighbor) == 1:
                if neighbor.y < self.y:  # NE
                    neighbors[0] = 1
                elif neighbor.x > self.x:  # SE
                    neighbors[1] = 1
                elif neighbor.y > self.y:  # SW
                    neighbors[2] = 1
                elif neighbor.x < self.x:  # NW
                    neighbors[3] = 1

        for i, v in enumerate(neighbors):
            if i == 0 and v == 0:
                pos = (self.x, self.y - 1)
                neighborspos.append(pos)
            if i == 1 and v == 0:
                pos = (self.x + 1, self.y)
                neighborspos.append(pos)
            if i == 2 and v == 0:
                pos = (self.x, self.y + 1)
                neighborspos.append(pos)
            if i == 3 and v == 0:
                pos = (self.x - 1, self.y)
                neighborspos.append(pos)

        self.neighbors = neighborspos

    def getTileType(self) -> str:
        string: str = ""
        neighborscount = 0
        neighbors: List[bool] = [0, 0, 0, 0]
        for neighbor in Map.tiles:
            if engine.tileDistance(self, neighbor) == 1:
                if neighbor.y < self.y:  # NE
                    neighbors[0] = 1
                elif neighbor.x > self.x:  # SE
                    neighbors[1] = 1
                elif neighbor.y > self.y:  # SW
                    neighbors[2] = 1
                elif neighbor.x < self.x:  # NW
                    neighbors[3] = 1
        for neighbor in neighbors:
            if neighbor == 1:
                neighborscount += 1
        if neighborscount == 1:
            if neighbors[0] == 1:
                string = "S_NE"
            if neighbors[1] == 1:
                string = "W_SE"
            if neighbors[2] == 1:
                string = "E_SW"
            if neighbors[3] == 1:
                string = "S_NW"

        elif neighborscount == 2:
            if neighbors[0] == 0 and neighbors[1] == 0:
                string = "E"
            elif neighbors[0] == 0 and neighbors[3] == 0:
                string = "N"
            elif neighbors[2] == 0 and neighbors[3] == 0:
                string = "W"
            elif neighbors[2] == 0 and neighbors[1] == 0:
                string = "S"
            elif neighbors[0] == 0 and neighbors[2] == 0:
                string = "SE_NW"
            elif neighbors[1] == 0 and neighbors[3] == 0:
                string = "NE_SW"

        elif neighborscount == 3:
            if neighbors[0] == 1 and neighbors[1] == 1 and neighbors[2] == 1:
                string = "NW"
            elif neighbors[1] == 1 and neighbors[2] == 1 and neighbors[3] == 1:
                string = "NE"
            elif neighbors[2] == 1 and neighbors[3] == 1 and neighbors[0] == 1:
                string = "SE"
            elif neighbors[3] == 1 and neighbors[0] == 1 and neighbors[1] == 1:
                string = "SW"

        elif neighborscount == 4:
            string = "M"

        return string


class Map:
    tiles: List = []
    maxsize: int
    tilecount: int

    def __init__(self, maxsize: int, tilecount: int) -> None:
        self.maxsize = maxsize
        self.tilecount = tilecount

    def generateTiles(self, scale):
        file = numpy.load("map.npy", 'r', 'bytes')
        for y, row in enumerate(file):
            for x, tile in enumerate(row):
                tile = round(float(tile))
                if tile:
                    Map.tiles.append(Tile((round(float(x)) - scale / 2,round(float(y)) - scale / 2, 0)))

    def renderTiles(offset):
        for tile in Map.tiles:
            pos: List = [
                (main.WIN.get_width()+32)/2 + (tile.x) * 32 - (tile.y) * 32 + offset[0],
                (main.WIN.get_height()+16)/2 + (tile.x) * 16 + (tile.y) * 16 - tile.z * 32 + offset[1],
            ]

            if type(tile) == Tile:
                tiletype: str = tile.getTileType()
                main.WIN.blit(pygame.image.load("Assets/Map/" + tiletype + "_Tile.png").convert_alpha(), pos)

            elif type(tile) == Player:
                pos[1] -= tile.imgy / 4
                pos[0] += tile.imgx / 2
                img = pygame.transform.scale(pygame.image.load("Assets/Player/Melee/Character01/character01-front-left.png").convert_alpha(),(32, 64))
                main.WIN.blit(img, pos)

