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

        for i in range(3):
            x_cut_size = 2
            y_cut_size = 2

            for y in range(len(level)):
                if random.randint(0, 1):
                    if x_cut_size > 0:
                        x_cut_size -= 1
                else:
                    if x_cut_size < 6:
                        x_cut_size += 1

                if random.randint(0, 1):
                    if y_cut_size > 0:
                        y_cut_size -= 1
                else:
                    if y_cut_size < 6:
                        y_cut_size += 1

                for x in range(len(level[y])):
                    self.neighborscount = 0
                    if y > 1 and y < len(level) - 1 and x > 1 and x < len(level[y]) - 1:
                        if level[y-1][x] == 1:
                            self.neighborscount += 1
                        if level[y+1][x] == 1:
                            self.neighborscount += 1
                        if level[y][x+1] == 1:
                            self.neighborscount += 1
                        if level[y][x-1] == 1:
                            self.neighborscount += 1

                    if not(level[y][x]):
                        if self.neighborscount >= 3:
                            level[y][x] = 1

                    else:
                        if self.neighborscount < 1:
                            level[y][x] = 0

                    if not(i):
                        if x < x_cut_size + self.random_gen['padding']:
                            level[y][x] = 0

                        if x > len(level[y]) - x_cut_size - 1 - self.random_gen['padding']:
                            level[y][x] = 0

                        if x < y_cut_size + self.random_gen['padding']:
                            level[x][y] = 0

                        if x > len(level) - y_cut_size - 1 - self.random_gen['padding']:
                            level[x][y] = 0

        os.remove("map.npy")
        numpy.save("map", level)
