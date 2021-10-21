import main
import pygame
from map import tile_matrix
import engine
from typing import List
import tiles


class click:
    def __init__(self) -> None:
        self.button: int

    def getClickedTile(offset: tuple, zoom: List[int]):
        click_pos = pos()
        highest_z = -1
        clicked_tile: tiles.Dirt = None
        for tile in tile_matrix:
            dist = engine.pixelDistance(
                engine.convertTileToScreenPos(tile, offset, zoom), click_pos)
            if dist <= 32:
                if highest_z < tile[1][2]:
                    clicked_tile = tile[0]
        if clicked_tile:
            if type(clicked_tile) == tiles.Dirt:
                if clicked_tile.tile_above:
                    return clicked_tile.tile_above
            return clicked_tile
        return None


def pos() -> tuple:
    return pygame.mouse.get_pos()
