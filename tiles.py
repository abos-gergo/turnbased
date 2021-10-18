import map
import random
from typing import List
import pygame


class TileTypes:
    S_NE_Dirt = pygame.image.load("Assets/Map/S_NE_Tile.png")
    W_SE_Dirt = pygame.image.load("Assets/Map/W_SE_Tile.png")
    E_SW_Dirt = pygame.image.load("Assets/Map/E_SW_Tile.png")
    S_NW_Dirt = pygame.image.load("Assets/Map/S_NW_Tile.png")

    N_Dirt = pygame.image.load("Assets/Map/N_Tile.png")
    E_Dirt = pygame.image.load("Assets/Map/E_Tile.png")
    S_Dirt = pygame.image.load("Assets/Map/S_Tile.png")
    W_Dirt = pygame.image.load("Assets/Map/W_Tile.png")

    NE_SW_Dirt = pygame.image.load("Assets/Map/NE_SW_Tile.png")
    SE_NW_Dirt = pygame.image.load("Assets/Map/SE_NW_Tile.png")

    NE_Dirt = pygame.image.load("Assets/Map/NE_Tile.png")
    SE_Dirt = pygame.image.load("Assets/Map/SE_Tile.png")
    SW_Dirt = pygame.image.load("Assets/Map/SW_Tile.png")
    NW_Dirt = pygame.image.load("Assets/Map/NW_Tile.png")

    M_Dirt = pygame.image.load("Assets/Map/M_Tile.png")


class Tile:
    def __init__(self, pos) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.tile_type = ''
        self.anchor_y: int = 0

    def get_tile_type(self):
        pass


class Dirt(Tile):
    def __init__(self, pos: tuple) -> None:
        super().__init__(pos)

        self.neighbors: List[tuple] = [0, 0, 0, 0]
        self.imgx, self.imgy = (64, 32)
        self.tile_type = ''
        self.tile_above = None

    def get_neighbors(self) -> List[bool]:
        """
        Returns a list of bools, true meaning there is a neighbor, false meaning there isn't one.
        """

        neighbors: List[bool] = [0, 0, 0, 0]
        for row in map.tile_matrix:
            for dirt in row:
                if dirt:
                    if dirt.y == self.y - 1 and dirt.x == self.x:
                        neighbors[0] = 1
                    elif dirt.y == self.y and dirt.x == self.x + 1:
                        neighbors[1] = 1
                    elif dirt.y == self.y + 1 and dirt.x == self.x:
                        neighbors[2] = 1
                    elif dirt.y == self.y and dirt.x == self.x - 1:
                        neighbors[3] = 1
        return neighbors

    def get_tile_type(self) -> str:
        """
        Returns a string representing the tile type based on the dirt's neighbors
        """

        neighborscount = 0
        for neighbor in self.neighbors:
            if neighbor:
                neighborscount += 1

        if neighborscount == 1:
            if self.neighbors[0] == 1:
                return TileTypes.S_NE_Dirt
            if self.neighbors[1] == 1:
                return TileTypes.W_SE_Dirt
            if self.neighbors[2] == 1:
                return TileTypes.E_SW_Dirt
            if self.neighbors[3] == 1:
                return TileTypes.S_NW_Dirt

        elif neighborscount == 2:
            if self.neighbors[0] == 0 and self.neighbors[1] == 0:
                return TileTypes.E_Dirt
            elif self.neighbors[0] == 0 and self.neighbors[3] == 0:
                return TileTypes.N_Dirt
            elif self.neighbors[2] == 0 and self.neighbors[3] == 0:
                return TileTypes.W_Dirt
            elif self.neighbors[2] == 0 and self.neighbors[1] == 0:
                return TileTypes.S_Dirt
            elif self.neighbors[0] == 0 and self.neighbors[2] == 0:
                return TileTypes.SE_NW_Dirt
            elif self.neighbors[1] == 0 and self.neighbors[3] == 0:
                return TileTypes.NE_SW_Dirt

        elif neighborscount == 3:
            if self.neighbors[0] == 1 and self.neighbors[1] == 1 and self.neighbors[2] == 1:
                return TileTypes.NW_Dirt
            elif self.neighbors[1] == 1 and self.neighbors[2] == 1 and self.neighbors[3] == 1:
                return TileTypes.NE_Dirt
            elif self.neighbors[2] == 1 and self.neighbors[3] == 1 and self.neighbors[0] == 1:
                return TileTypes.SE_Dirt
            elif self.neighbors[3] == 1 and self.neighbors[0] == 1 and self.neighbors[1] == 1:
                return TileTypes.SW_Dirt

        elif neighborscount == 4:
            return TileTypes.M_Dirt

        return TileTypes.M_Dirt

    def set_tile_above(self, tile: Tile) -> None:
        """
        Sets the dirt's tile_above variable to the given tile
        """

        self.tile_above = tile


class Tree(Tile):
    def __init__(self, pos) -> None:
        super().__init__(pos)
        self.imgx = 64
        self.imgy = 64
        self.tile_type = ''
        self.anchor_y: int = 64

    def get_tile_type(self):
        """
        Returns the type of the tree, chosen on random
        """

        tree_1 = pygame.image.load("Assets/decorations/Tree01.png")
        tree_2 = pygame.image.load("Assets/decorations/Tree02.png")
        tree_3 = pygame.image.load("Assets/decorations/Tree03.png")
        return random.choice((tree_1, tree_2, tree_3))


class Rock(Tile):
    def __init__(self, pos):
        super().__init__(pos)
        self.imgx = 64
        self.imgy = 64
        self.tile_type = ''

    def get_tile_type(self):
        """
        Returns the type of the rock, chosen on random
        """

        rock_1 = pygame.image.load("Assets/decorations/rock01.png")
        rock_2 = pygame.image.load("Assets/decorations/rock02.png")
        return random.choice((rock_1, rock_2))
