import pygame.mouse

import mapgen
import engine

class click:
    def __init__(self) -> None:
        self.button: int

    def pos(self) -> tuple[int, int]:
        return pygame.mouse.get_pos()

    def clickedOnTile(self):
        lowestDist = engine.pixelDistance(mapgen.Map.tiles[0], self.mousepos)
        for tile in mapgen.Map.tiles[1, ]:
            pass
