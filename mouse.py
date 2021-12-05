import main
import pygame
from map import dirt_list
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
        for tile in dirt_list:
            distx, disty = engine.pixelDistance(
                engine.convertTileToScreenPos(tile, offset, zoom), click_pos)
            if distx <= 16 * main.WIN.get_width()/(main.WIN.get_width() + zoom[0]) and disty <= 16 * main.WIN.get_width()/(main.WIN.get_width() + zoom[0]):
                if highest_z < tile.z:
                    clicked_tile = tile

        if clicked_tile:
            if type(clicked_tile) == tiles.Dirt:
                if clicked_tile.tile_above:
                    return clicked_tile.tile_above
            
            return clicked_tile
        return None


def pos() -> tuple:
    return pygame.mouse.get_pos()

def display_cursor(display):
    pygame.draw.circle(display, (255,255,255), pos(), 5, 2) 
