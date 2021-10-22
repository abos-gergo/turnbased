from typing import List
import numpy
import tiles

tile_matrix: List[List] = []
none_matrix: List[List] = []


class Map:

    def read_tiles(self):
        for z in range(2):
            map_file = numpy.load(f"Game Files/layer_{z}.npy", 'r', 'bytes')
            temp_layer: List[List] = []
            none_layer: List[List] = []
            for y, row in enumerate(map_file):
                for x, tile in enumerate(row):
                    if tile == 1:
                        generated_tile = tiles.Dirt((int(round(float(x))), int(round(float(y))), z))
                        tile_matrix.append(generated_tile)
                    elif tile == 2:
                        generated_tree = tiles.Tree((x, y, z))
                        tile_matrix.append(generated_tree)
                    else:
                        none_matrix.append((None, (x, y, z)))

        for tile in tile_matrix:
            if isinstance(tile, tiles.Dirt):
                tile.neighbors = tile.get_neighbors()
                tile.tile_type = tile.get_tile_type().convert()
                tile.tile_type.set_colorkey((0, 0, 0))
            elif tile:
                tile.tile_type = tile.get_tile_type().convert_alpha()
                tile.tile_type.set_colorkey((0, 0, 0))
