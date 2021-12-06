from map import dirt_matrix, enviroment_matrix
from typing import List
import tiles

def renderTiles(offset, Display, player, selected_tiles, Button, collide):
    for tile in dirt_matrix:
        pos: List = [
            (tile.x) * 32 - (tile.y) * 32 + offset[0],
            (tile.x) * 16 + (tile.y) * 16 - tile.z * 32 + offset[1] - tile.anchor_y]
        
        if pos[0] > -64 and pos[0] < Display.get_width() + 64 and pos[1] > -64 and pos[1] < Display.get_height() + 64:
            Display.blit(tile.tile_type, pos)
    
    for tile in selected_tiles:
        Display.blit(tiles.TileTypes.outline.convert_alpha(), (
            (tile.x) * 32 - (tile.y) * 32 + offset[0],
            (tile.x) * 16 + (tile.y) * 16 - tile.z * 32 + offset[1] - tile.anchor_y))

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
                        
                if pos[0] > -64*2 and pos[0] < Display.get_width() + 64*2 and pos[1] > -64*2 and pos[1] < Display.get_height() + 64*2:
                    if tile != player:
                        if tile == tiles.Tree:
                            pos[0] += 64
                            pos[1] += 64

                        Display.blit(tile.tile_type, pos)
                    else:
                        Display.blit(tile.get_tile_type(), pos)

    Button.display_button(Display, [
                    (player.x) * 32 - (player.y) * 32 + offset[0],
                    (player.x) * 16 + (player.y) * 16 - player.z * 32 + offset[1] - player.anchor_y
                    ], collide, enviroment_matrix)