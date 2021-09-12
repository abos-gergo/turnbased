import mapgen


class Player:
    def __init__(self, pos: tuple, teamNumber) -> None:
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.teamNumber = teamNumber
        self.imgx, self.imgy = (29, 64)
        mapgen.Map.tiles.append(Player)
