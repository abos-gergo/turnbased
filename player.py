class Player:
    def __init__(self, pos : tuple, teamNumber) -> None:
        self.x, self.y, self.z = pos
        self.teamNumber = teamNumber
        