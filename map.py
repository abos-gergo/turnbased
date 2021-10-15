from typing import List
import numpy
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
            if isinstance(tile, tiles.Dirt):
                tile.neighbors = tile.get_neighbors()
                tile.tile_type = tile.get_tile_type().convert()
            if isinstance(tile, tiles.Tree):
                tile.tile_type = tile.get_tile_type().convert_alpha()
            if isinstance(tile, tiles.Rock):
                tile.tile_type = tile.get_tile_type().convert_alpha()

    def tile_set_colorkey(self):
        for tile in Map.tiles:
            if isinstance(tile, tiles.Dirt):
                tile.tile_type.set_colorkey((0, 0, 0))
