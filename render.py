from map import dirt_matrix, enviroment_matrix
from typing import List
import tiles

def renderTiles(offset, Display, player, clicked_tile):
    for tile in dirt_matrix:
        pos: List = [
            (tile.x) * 32 - (tile.y) * 32 + offset[0],
            (tile.x) * 16 + (tile.y) * 16 - tile.z * 32 + offset[1] - tile.anchor_y]
        
        if pos[0] > -64 and pos[0] < Display.get_width() + 64 and pos[1] > -64 and pos[1] < Display.get_height() + 64:
            Display.blit(tile.tile_type, pos)
    
    Display.blit(tiles.TileTypes.outline.convert_alpha(), ((clicked_tile.x) * 32 - (clicked_tile.y) * 32 + offset[0], (clicked_tile.x) * 16 + (clicked_tile.y) * 16 - clicked_tile.z * 32 + offset[1] - clicked_tile.anchor_y))


    for y, row in enumerate(enviroment_matrix):
        for x, tile in enumerate(row):
            if tile != None:
                pos: List = [
                    (tile.x) * 32 - (tile.y) * 32 + offset[0],
                    (tile.x) * 16 + (tile.y) * 16 - tile.z * 32 + offset[1] - tile.anchor_y
                    ]
                
                if tile == player:
                    if enviroment_matrix[tile.getTileBelow().y][tile.getTileBelow().x] == None:
                        enviroment_matrix[y][x] = None
                        enviroment_matrix[tile.getTileBelow().y][tile.getTileBelow().x] = tile
                        
                if pos[0] > -64 and pos[0] < Display.get_width() + 64 and pos[1] > -64 and pos[1] < Display.get_height() + 64:
                    if tile != player:
                        Display.blit(tile.tile_type, pos)
                    else:
                        pos[0] += 0
                        pos[1] -= 10
                        Display.blit(tile.get_tile_type(), pos)
