from typing import List
import numpy
import tiles

tile_matrix: List = []
none_matrix: List[None] = []
dirt_matrix: List[tiles.Dirt] = []
enviroment_matrix: List[List] = [[None]*70 for i in range(70)]

class Map:
    def read_tiles(self, player0):
        for z in range(2):
            map_file = numpy.load(f"Game Files/layer_{z}.npy", 'r', 'bytes')
            for y, row in enumerate(map_file):
                for x, tile in enumerate(row):
                    if tile == 1:
                        generated_tile = tiles.Dirt((int(round(float(x))), int(round(float(y))), z))
                        tile_matrix.append(generated_tile)
                        dirt_matrix.append(generated_tile)
                    elif y == player0.y and x == player0.x and z == player0.z:
                        generated_tile = player0
                        tile_matrix.append(generated_tile)
                        enviroment_matrix[y][x] = generated_tile
                    elif tile == 2:
                        generated_tile = tiles.Tree((x, y, z))
                        tile_matrix.append(generated_tile)
                        enviroment_matrix[y][x] = generated_tile
                    elif tile == 3:
                        generated_tile = tiles.Rock((x, y, z))
                        tile_matrix.append(generated_tile)
                        enviroment_matrix[y][x] = generated_tile                        
                    else:
                        none_matrix.append((None, (x, y, z)))

        for tile in tile_matrix:
            if isinstance(tile, tiles.Dirt):
                tile.neighbors = tile.get_neighbors()
                tile.tile_type = tile.get_tile_type().convert()
                tile.tile_type.set_colorkey((0, 0, 0))
            elif tile:
                tile.tile_type = tile.get_tile_type().convert()
                tile.tile_type.set_colorkey((0, 0, 0))
