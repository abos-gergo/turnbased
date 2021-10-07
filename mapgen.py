from pygame import display
import player
from typing import List
import numpy
import pygame
import random
import Decorations


class TileTypes:
    S_NE_Tile = pygame.image.load("Assets/Map/S_NE_Tile.png")
    W_SE_Tile = pygame.image.load("Assets/Map/W_SE_Tile.png")
    E_SW_Tile = pygame.image.load("Assets/Map/E_SW_Tile.png")
    S_NW_Tile = pygame.image.load("Assets/Map/S_NW_Tile.png")

    N_Tile = pygame.image.load("Assets/Map/N_Tile.png")
    E_Tile = pygame.image.load("Assets/Map/E_Tile.png")
    S_Tile = pygame.image.load("Assets/Map/S_Tile.png")
    W_Tile = pygame.image.load("Assets/Map/W_Tile.png")

    NE_SW_Tile = pygame.image.load("Assets/Map/NE_SW_Tile.png")
    SE_NW_Tile = pygame.image.load("Assets/Map/SE_NW_Tile.png")

    NE_Tile = pygame.image.load("Assets/Map/NE_Tile.png")
    SE_Tile = pygame.image.load("Assets/Map/SE_Tile.png")
    SW_Tile = pygame.image.load("Assets/Map/SW_Tile.png")
    NW_Tile = pygame.image.load("Assets/Map/NW_Tile.png")

    M_Tile = pygame.image.load("Assets/Map/M_Tile.png")


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
        if self.y > 1 and self.y < len(Map.tile_matrix) - 1 and self.x > 1 and self.x < len(Map.tile_matrix[self.y]) - 1:
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
                    Map.tiles.append(
                        Tile((int(round(float(x))), int(round(float(y))), 0)))
                    if not(random.randint(0, 20)):
                        Map.tiles.append(Decorations.Tree(
                            [int(round(float(x))), int(round(float(y)))]))

                matrix_row.append(tile)
            Map.tile_matrix.append(list(matrix_row))
        for tile in Map.tiles:
            if type(tile) == Tile:
                tile.tile_type = tile.getTileType()

    def tile_set_colorkey(self):
        for tile in Map.tiles:
            if type(tile) == Tile:
                tile.tile_type.set_colorkey((0, 0, 0))

    def renderTiles(offset, Display):
        for tile in Map.tiles:
            pos: List = [
                (tile.x) * 32 - (tile.y) * 32 + offset[0],
                (tile.x) * 16 + (tile.y) * 16 - tile.z * 32 + offset[1],
            ]

            if pos[0] > -64 and pos[0] < Display.get_width() and pos[1] > -64 and pos[1] < Display.get_height():
                if type(tile) == Decorations.Tree:
                    pos[0] -= 10
                    pos[1] -= tile.imgy/2
                    Display.blit(
                                        Decorations.Tree(pos).tree_img.convert_alpha(), pos)
                elif type(tile) == Tile:
                    Display.blit(tile.tile_type.convert(), pos)

                elif type(tile) == player.Player:
                    pos[1] -= tile.imgy / 4
                    pos[0] += tile.imgx / 2
                    img = pygame.transform.scale(pygame.image.load(
                        "Assets/Player/Melee/Character01/character01-front-left.png"), (32, 64))
                    Display.blit(img, pos)
