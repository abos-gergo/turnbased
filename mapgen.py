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

    def getNeighbors(self):
        neighborspos: List[tuple] = []
        neighbors: List[bool] = [0, 0, 0, 0]
        if Map.tile_matrix[self.y - 1][self.x]:
            neighbors[0] = 1
        if Map.tile_matrix[self.y][self.x + 1]:
            neighbors[1] = 1
        if Map.tile_matrix[self.y + 1][self.x]:
            neighbors[2] = 1
        if Map.tile_matrix[self.y][self.x - 1]:
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
        neighborscount = 0
        neighbors: List[bool] = [0, 0, 0, 0]
        if Map.tile_matrix[self.y - 1][self.x]:
            neighbors[0] = 1
            neighborscount += 1
        if Map.tile_matrix[self.y][self.x + 1]:
            neighbors[1] = 1
            neighborscount += 1
        if Map.tile_matrix[self.y + 1][self.x]:
            neighbors[2] = 1
            neighborscount += 1
        if Map.tile_matrix[self.y][self.x - 1]:
            neighbors[3] = 1
            neighborscount += 1


        if neighborscount == 1:
            if neighbors[0] == 1:
                return "S_NE"
            if neighbors[1] == 1:
                return "W_SE"
            if neighbors[2] == 1:
                return "E_SW"
            if neighbors[3] == 1:
                return "S_NW"

        elif neighborscount == 2:
            if neighbors[0] == 0 and neighbors[1] == 0:
                return "E"
            elif neighbors[0] == 0 and neighbors[3] == 0:
                return "N"
            elif neighbors[2] == 0 and neighbors[3] == 0:
                return "W"
            elif neighbors[2] == 0 and neighbors[1] == 0:
                return "S"
            elif neighbors[0] == 0 and neighbors[2] == 0:
                return "SE_NW"
            elif neighbors[1] == 0 and neighbors[3] == 0:
                return "NE_SW"

        elif neighborscount == 3:
            if neighbors[0] == 1 and neighbors[1] == 1 and neighbors[2] == 1:
                return "NW"
            elif neighbors[1] == 1 and neighbors[2] == 1 and neighbors[3] == 1:
                return "NE"
            elif neighbors[2] == 1 and neighbors[3] == 1 and neighbors[0] == 1:
                return "SE"
            elif neighbors[3] == 1 and neighbors[0] == 1 and neighbors[1] == 1:
                return "SW"

        elif neighborscount == 4:
            return "M"

        return "M"


class Map:
    tiles: List = []
    tile_matrix: List[List] = []
    maxsize: int
    tilecount: int

    def __init__(self, maxsize: int, tilecount: int) -> None:
        self.maxsize = maxsize
        self.tilecount = tilecount

    def generateTiles(self, scale):
        file = numpy.load("map.npy", 'r', 'bytes')
        matrix_row: List[List] = []
        for y, row in enumerate(file):
            matrix_row.clear()
            for x, tile in enumerate(row):
                tile = round(float(tile))
                if tile:
                    Map.tiles.append(Tile((int(round(float(x))), int(round(float(y))), 0)))
                matrix_row.append(tile)
            Map.tile_matrix.append(list(matrix_row))
        print(Map.tile_matrix)

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

