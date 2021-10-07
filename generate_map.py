import random
import numpy
import os


class generate_map:
    def __init__(self, scale) -> None:
        self.scale: int = scale
        self.random_gen = {
            'wallCountdown': self.scale * self.scale/2,
            'padding': 3,
            'x': int(self.scale / 2),
            'y': int(self.scale / 2)
            }

        self.neighborscount: int = 0

    def getLevelRow(self):
        return [0] * self.scale

    def generation(self):
        level = [self.getLevelRow() for _ in range(self.scale)]

        while self.random_gen['wallCountdown'] >= 0:
            x = self.random_gen['x']
            y = self.random_gen['y']

            if level[y][x] == 0:
                level[y][x] = 1
                self.random_gen['wallCountdown'] -= 1

            roll = random.randint(1, 4)

            if roll == 1 and x > self.random_gen['padding']:
                self.random_gen['x'] -= 1

            if roll == 2 and x < self.scale - 1 - self.random_gen['padding']:
                self.random_gen['x'] += 1

            if roll == 3 and y > self.random_gen['padding']:
                self.random_gen['y'] -= 1

            if roll == 4 and y < self.scale - 1 - self.random_gen['padding']:
                self.random_gen['y'] += 1

        for i in range(2):
            for y in range(len(level)):
                for x in range(len(level[y])):
                    self.neighborscount = 0
                    if level[y][x] == 0:
                        if y > 1 and y < len(level) - 1 and x > 1 and x < len(level[y]) - 1:
                            if level[y-1][x] == 1:
                                self.neighborscount += 1
                            if level[y+1][x] == 1:
                                self.neighborscount += 1
                            if level[y][x+1] == 1:
                                self.neighborscount += 1
                            if level[y][x-1] == 1:
                                self.neighborscount += 1

                        if self.neighborscount == 4 or self.neighborscount == 3:
                            level[y][x] = 1

        os.remove("map.npy")
        numpy.save("map", level)
