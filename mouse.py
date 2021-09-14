from _typeshed import Self
import mapgen
import engine

class click:
    def __init__(self) -> None:
        self.button: int
        self.mousepos: tuple[int, int]

    def clickedOnTile(self):
        lowestDist = engine.pixelDistance(mapgen.Map.tiles[0], self.mousepos)
        for tile in mapgen.Map.tiles[1, ]:
            pass
