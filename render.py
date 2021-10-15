from mapgen import Map
from typing import List


def renderTiles(offset, Display):
    for tile in Map.tiles:
        pos: List = [
            (tile.x) * 32 - (tile.y) * 32 + offset[0],
            (tile.x) * 16 + (tile.y) * 16 - tile.z * 32 + offset[1] - tile.anchor_y
        ]

        if pos[0] > -64 and pos[0] < Display.get_width() + 64 and pos[1] > -64 and pos[1] < Display.get_height() + 64:

            Display.blit(tile.tile_type, pos)
