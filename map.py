from typing import List
import numpy
import random
import tiles

tile_matrix: List[List] = []

class Map:

    def generateTiles(self):
        map_file = numpy.load("Game Files/map.npy", 'r', 'bytes')

        for y, row in enumerate(map_file):
            temp_row: List[List] = []
            for x, tile in enumerate(row):
                if tile:
                    generated_tile = tiles.Dirt((int(round(float(x))), int(round(float(y))), 0))
                    temp_row.append(generated_tile)
                    '''
                        if not(random.randint(0, 14)):
                        generated_tree = tiles.Tree([int(round(float(x))), int(round(float(y))), 1])
                        Map.tiles.append(generated_tree)
                        generated_tile.set_tile_above(generated_tree)
                        generated_tree.tile_type = generated_tree.get_tile_type().convert_alpha()
                    elif not(random.randint(0, 60)):
                        generated_rock = tiles.Rock([int(round(float(x))), int(round(float(y))), 1])
                        Map.tiles.append(generated_rock)
                        generated_tile.set_tile_above(generated_rock)
                        generated_rock.tile_type = generated_rock.get_tile_type().convert_alpha()
                    '''
                else:
                    temp_row.append(None)
            tile_matrix.append(list(temp_row))

        for row in tile_matrix:
            for tile in row:
                if tile:
                    tile.neighbors = tile.get_neighbors()
                    tile.tile_type = tile.get_tile_type().convert()
                    tile.tile_type.set_colorkey((0, 0, 0))