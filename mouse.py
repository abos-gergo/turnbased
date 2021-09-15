import main
import pygame.mouse
import mapgen
import engine

class click:
    def __init__(self) -> None:
        self.button: int

    def getClickedTile(offset: tuple[int, int]) -> mapgen.Tile:
        clickpos = pos()
        lowest_dist = engine.pixelDistance(engine.convertTileToScreenPos(mapgen.Map.tiles[0], offset), clickpos)
        closest_tile = mapgen.Map.tiles[0]
        for tile in mapgen.Map.tiles[1: ]:
            dist = engine.pixelDistance(engine.convertTileToScreenPos(tile, offset), clickpos)
            if dist < lowest_dist:
                lowest_dist = dist
                closest_tile = tile
        print(closest_tile.x, closest_tile.y)
        return closest_tile

def pos() -> tuple[int, int]:
    return pygame.mouse.get_pos()