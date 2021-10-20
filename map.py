from typing import List
import numpy
import tiles

tile_matrix: List[List] = []


class Map:

    def read_tiles(self):
        for z in range(2):
            map_file = numpy.load(f"Game Files/layer_{z}.npy", 'r', 'bytes')
            temp_layer: List[List] = []
            for y, row in enumerate(map_file):
                temp_row: List[List] = []
                for x, tile in enumerate(row):
                    if tile == 1:
                        generated_tile = tiles.Dirt((int(round(float(x))), int(round(float(y))), z))
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
                    elif tile == 2:
                        generated_tree = tiles.Tree((x, y, z))
                        temp_row.append(generated_tree)
                    else:
                        temp_row.append(None)
                temp_layer.append(list(temp_row))
            tile_matrix.append(temp_layer)
        for layer in tile_matrix:
            for row in layer:
                for tile in row:
                    if isinstance(tile, tiles.Dirt):
                        tile.neighbors = tile.get_neighbors()
                        tile.tile_type = tile.get_tile_type().convert()
                        tile.tile_type.set_colorkey((0, 0, 0))
                    elif tile:
                        tile.tile_type = tile.get_tile_type().convert_alpha()
                        tile.tile_type.set_colorkey((0, 0, 0))