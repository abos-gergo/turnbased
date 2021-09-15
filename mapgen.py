from player import Player
from typing import List
import numpy
import engine
import main
import pygame


class TileTypes:
    S_NE_Tile = pygame.image.load("Assets/Map/S_NE_Tile.png").convert_alpha()
    W_SE_Tile = pygame.image.load("Assets/Map/W_SE_Tile.png").convert_alpha()
    E_SW_Tile = pygame.image.load("Assets/Map/E_SW_Tile.png").convert_alpha()
    S_NW_Tile = pygame.image.load("Assets/Map/S_NW_Tile.png").convert_alpha()

    N_Tile = pygame.image.load("Assets/Map/N_Tile.png").convert_alpha()
    E_Tile = pygame.image.load("Assets/Map/E_Tile.png").convert_alpha()
    S_Tile = pygame.image.load("Assets/Map/S_Tile.png").convert_alpha()
    W_Tile = pygame.image.load("Assets/Map/W_Tile.png").convert_alpha()

    NE_SW_Tile = pygame.image.load("Assets/Map/NE_SW_Tile.png").convert_alpha()
    SE_NW_Tile = pygame.image.load("Assets/Map/SE_NW_Tile.png").convert_alpha()

    NE_Tile = pygame.image.load("Assets/Map/NE_Tile.png").convert_alpha()
    SE_Tile = pygame.image.load("Assets/Map/SE_Tile.png").convert_alpha()
    SW_Tile = pygame.image.load("Assets/Map/SW_Tile.png").convert_alpha()
    NW_Tile = pygame.image.load("Assets/Map/NW_Tile.png").convert_alpha()

    M_Tile = pygame.image.load("Assets/Map/M_Tile.png").convert_alpha()

class Tile:


    def __init__(self, pos: tuple) -> None:
        self.x, self.y, self.z = pos
        self.neighbors: List[tuple] = []
        self.imgx, self.imgy = (64, 32)
        self.tile_type = "M"

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
                return TileTypes.S_NE_Tile
            if neighbors[1] == 1:
                return TileTypes.W_SE_Tile
            if neighbors[2] == 1:
                return TileTypes.E_SW_Tile
            if neighbors[3] == 1:
                return TileTypes.S_NW_Tile

        elif neighborscount == 2:
            if neighbors[0] == 0 and neighbors[1] == 0:
                return TileTypes.E_Tile
            elif neighbors[0] == 0 and neighbors[3] == 0:
                return TileTypes.N_Tile
            elif neighbors[2] == 0 and neighbors[3] == 0:
                return TileTypes.W_Tile
            elif neighbors[2] == 0 and neighbors[1] == 0:
                return TileTypes.S_Tile
            elif neighbors[0] == 0 and neighbors[2] == 0:
                return TileTypes.SE_NW_Tile
            elif neighbors[1] == 0 and neighbors[3] == 0:
                return TileTypes.NE_SW_Tile

        elif neighborscount == 3:
            if neighbors[0] == 1 and neighbors[1] == 1 and neighbors[2] == 1:
                return TileTypes.NW_Tile
            elif neighbors[1] == 1 and neighbors[2] == 1 and neighbors[3] == 1:
                return TileTypes.NE_Tile
            elif neighbors[2] == 1 and neighbors[3] == 1 and neighbors[0] == 1:
                return TileTypes.SE_Tile
            elif neighbors[3] == 1 and neighbors[0] == 1 and neighbors[1] == 1:
                return TileTypes.SW_Tile

        elif neighborscount == 4:
            return TileTypes.M_Tile

        return TileTypes.M_Tile


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
        for tile in Map.tiles:
            tile.tile_type = tile.getTileType()

    def renderTiles(offset):
        for tile in Map.tiles:
            pos: List = [
                (main.WIN.get_width()+32)/2 + (tile.x) * 32 - (tile.y) * 32 + offset[0],
                -(main.WIN.get_height()+16)/2 + (tile.x) * 16 + (tile.y) * 16 - tile.z * 32 + offset[1],
            ]

            if pos[0] > -64 and pos[0] < main.WIN.get_width() and pos[1] > -64 and pos[1] < main.WIN.get_height():
                if type(tile) == Tile:
                    main.WIN.blit(tile.tile_type, pos)

                elif type(tile) == Player:
                    pos[1] -= tile.imgy / 4
                    pos[0] += tile.imgx / 2
                    img = pygame.transform.scale(pygame.image.load("Assets/Player/Melee/Character01/character01-front-left.png").convert_alpha(),(32, 64))
                    main.WIN.blit(img, pos)
