import mapgen
import main



class Player:
    def __init__(self, teamNumber) -> None:
        self.x = main.SCALE / 2
        self.y = main.SCALE / 2
        self.z = 1
        self.teamNumber = teamNumber
        self.tileBelow = self.getTileBelow()

    def getTileBelow(self):
        for tile in mapgen.Map.tiles:
            if tile.x == self.x and tile.y == self.y:
                return tile
