import pygame.mouse

import mapgen
import engine

class click:
    def __init__(self) -> None:
        self.button: int

    def clickedOnTile(self):
        lowestDist = engine.pixelDistance(mapgen.Map.tile_matrix[0], self.mousepos)
        for tile in mapgen.Map.tile_matrix[1, ]:
            pass


def pos() -> tuple[int, int]:
    return pygame.mouse.get_pos()