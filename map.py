from typing import List
import numpy
import tiles

SCALE = 80

all_tile_list: List = []
dirt_matrix: List[List] = [[None]*SCALE for i in range(SCALE)]
dirt_list: List[tiles.Dirt] = []
enviroment_matrix: List[List] = [[None]*SCALE for i in range(SCALE)]

class Map:
    def read_tiles(self, player0):
        for z in range(2):
            map_file = numpy.load(f"Game Files/test_layer_{z}.npy", 'r', 'bytes')
            for y, row in enumerate(map_file):
                for x, tile in enumerate(row):
                    if tile == 1:
                        generated_tile = tiles.Dirt((int(round(float(x))), int(round(float(y))), z))
                        all_tile_list.append(generated_tile)
                        dirt_list.append(generated_tile)
                        dirt_matrix[y][x] = generated_tile
                    elif y == player0.y and x == player0.x and z == player0.z:
                        generated_tile = player0
                        all_tile_list.append(generated_tile)
                        enviroment_matrix[y][x] = generated_tile
                        generated_tile.tile_type = generated_tile.get_tile_type().convert()
                        generated_tile.tile_type.set_colorkey((0, 0, 0))
                    elif tile == 2:
                        generated_tile = tiles.Tree((x, y, z))
                        all_tile_list.append(generated_tile)
                        enviroment_matrix[y][x] = generated_tile
                        generated_tile.tile_type = generated_tile.get_tile_type().convert()
                        generated_tile.tile_type.set_colorkey((0, 0, 0))
                    elif tile == 3:
                        generated_tile = tiles.Rock((x, y, z))
                        all_tile_list.append(generated_tile)
                        enviroment_matrix[y][x] = generated_tile
                        generated_tile.tile_type = generated_tile.get_tile_type().convert()
                        generated_tile.tile_type.set_colorkey((0, 0, 0))
                    elif tile == 4:
                        generated_tile = tiles.Boss_shard((x, y, z))
                        all_tile_list.append(generated_tile)
                        enviroment_matrix[y][x] = generated_tile
                        generated_tile.tile_type = generated_tile.get_tile_type().convert()
                        generated_tile.tile_type.set_colorkey((0, 0, 0))
                        
        for tile in dirt_list:
            if isinstance(tile, tiles.Dirt):
                tile.neighbors = tile.get_neighbors()
                tile.tile_type = tile.get_tile_type().convert()
                tile.tile_type.set_colorkey((0, 0, 0))