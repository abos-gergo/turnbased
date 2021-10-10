import main
import pygame
import mapgen
import engine
from typing import List


class click:
    def __init__(self) -> None:
        self.button: int

    def getClickedTile(offset: tuple, zoom: List[int]) -> mapgen.Tile:
        clickpos = pos()
        lowest_dist = engine.pixelDistance(engine.convertTileToScreenPos(
            mapgen.Map.tiles[0], offset, zoom), clickpos)
        closest_tile = mapgen.Map.tiles[0]
        for tile in mapgen.Map.tiles[1:]:
            dist = engine.pixelDistance(
                engine.convertTileToScreenPos(tile, offset, zoom), clickpos)
            if dist < lowest_dist:
                lowest_dist = dist
                closest_tile = tile
        print(closest_tile.x, closest_tile.y)
        if lowest_dist <= 32:
            return closest_tile
        else:
            return None


def pos() -> tuple:
    return pygame.mouse.get_pos()
