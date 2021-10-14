from pygame import display
import player
from typing import List
import numpy
import pygame
import random
import tiles

class Map:
    tiles: List = []
    tile_matrix: List[List] = []
    maxsize: int
    tilecount: int

    def __init__(self, maxsize: int, tilecount: int) -> None:
        self.maxsize = maxsize
        self.tilecount = tilecount

    def generateTiles(self, scale):
        map_file = numpy.load("Game Files/map.npy", 'r', 'bytes')
        matrix_row: List[List] = []
        for y, row in enumerate(map_file):
            matrix_row.clear()
            for x, tile in enumerate(row):
                if tile:
                    generated_tile = tiles.Dirt((int(round(float(x))), int(round(float(y))), 0))
                    Map.tiles.append(generated_tile)
                    if not(random.randint(0, 14)):
                        generated_tree = tiles.Tree([int(round(float(x))), int(round(float(y))), 1])
                        Map.tiles.append(generated_tree)
                        generated_tile.set_tile_above(generated_tree)
                    else:
                        if not(random.randint(0, 60)):
                            generated_rock = tiles.Rock([int(round(float(x))), int(round(float(y))), 1])
                            Map.tiles.append(generated_rock)
                            generated_tile.set_tile_above(generated_rock)

                matrix_row.append(tile)
            Map.tile_matrix.append(list(matrix_row))
        for tile in Map.tiles:
            if type(tile) == tiles.Dirt:
                tile.neighbors = generated_tile.get_neighbors()
                tile.tile_type = tile.get_tile_type()
            if type(tile) == tiles.Tree:
                tile.tile_type = tile.get_tile_type()
            if type(tile) == tiles.Rock:
                tile.tile_type = tile.get_tile_type()

    def tile_set_colorkey(self):
        for tile in Map.tiles:
            if type(tile) == tiles.Dirt:
                tile.tile_type.set_colorkey((0, 0, 0))

    def renderTiles(offset, Display):
        for tile in Map.tiles:
            pos: List = [
                (tile.x) * 32 - (tile.y) * 32 + offset[0],
                (tile.x) * 16 + (tile.y) * 16 - tile.z * 32 + offset[1],
            ]

            if pos[0] > -64 and pos[0] < Display.get_width() and pos[1] > -64 and pos[1] < Display.get_height():
                if type(tile) == tiles.Rock:
                    Display.blit(tile.tile_type.convert_alpha(), pos)

                elif type(tile) == tiles.Tree:
                    pos[1] -= 64
                    Display.blit(tile.tile_type.convert_alpha(), pos)

                elif type(tile) == tiles.Dirt:
                    Display.blit(tile.tile_type.convert(), pos)

                elif type(tile) == player.Player:
                    pos[1] -= tile.imgy / 4
                    pos[0] += tile.imgx / 2
                    img = pygame.transform.scale(pygame.image.load(
                        "Assets/Player/Melee/Character01/character01-front-left.png"), (32, 64))
                    Display.blit(img, pos)
