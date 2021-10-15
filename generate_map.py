import random
import numpy
import os


class generate_map:
    def __init__(self, scale) -> None:
        self.scale: int = scale
        self.generation_specs = {
            # How many dirt tile going to be in the first part of the generation (the dirt count could change later)
            'dirt_count': self.scale * self.scale/2,
            #the offset from the side of the map. It is important at the get_tile_type() part
            'padding': 3,
            #set x to the middle of the map
            'x': int(self.scale / 2),
            #set y to the middle of the map
            'y': int(self.scale / 2)
            }

        self.neighborscount: int = 0

    def get_level_row(self) -> list:
        '''
        Generetes a row, with a length of the given scale, and returns it as a list
        '''

        return [0] * self.scale

    def generation(self) -> None:
        '''
        Generates the map to Gamefiles\map.npy
        '''
        #make the level list according to the scales
        level = [self.get_level_row() for _ in range(self.scale)]

        while self.generation_specs['dirt_count'] >= 0:
            x = self.generation_specs['x']
            y = self.generation_specs['y']

            #dirt count decreases by 1 if the chosen tile type is 0 (none), and sets it to 1 (dirt tile)
            if level[y][x] == 0:
                level[y][x] = 1
                self.generation_specs['dirt_count'] -= 1

            #choose a direction (top, left, bottom, right)
            roll = random.randint(1, 4)

            #step 1 unit to the chosen direction
            if roll == 1 and x > self.generation_specs['padding']:
                self.generation_specs['x'] -= 1

            if roll == 2 and x < self.scale - 1 - self.generation_specs['padding']:
                self.generation_specs['x'] += 1

            if roll == 3 and y > self.generation_specs['padding']:
                self.generation_specs['y'] -= 1

            if roll == 4 and y < self.scale - 1 - self.generation_specs['padding']:
                self.generation_specs['y'] += 1

        for i in range(2):
            x_cut_size = 2
            y_cut_size = 2

            for y in range(len(level)):

                #set the cut sizes, based on randomness,
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
                    #get the neighbors of a dirt tile
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

                    #if tile is 0 (none) the count of the neighbors are more than 2, it will set the 0 (none) to 1 (dirt tile)
                    if not(level[y][x]):
                        if self.neighborscount >= 3:
                            level[y][x] = 1

                    #if the tile is 1 (dirt tile), but doesn't have any neighbors, the 1 (dirt tile) will set to 0 (none)
                    else:
                        if self.neighborscount < 1:
                            level[y][x] = 0

                    #it runs only once (if not(i))
                    if not(i):
                        #deletes all the tiles, which are closer to the left side than the cutsize
                        if x < x_cut_size + self.generation_specs['padding']:
                            level[y][x] = 0

                        #deletes all the tiles, which are closer to the right side than the cutsize
                        if x > len(level[y]) - x_cut_size - 1 - self.generation_specs['padding']:
                            level[y][x] = 0

                        #deletes all the tiles, which are closer to the top side than the cutsize
                        if x < y_cut_size + self.generation_specs['padding']:
                            level[x][y] = 0

                        #deletes all the tiles, which are closer to the bottom side than the cutsize
                        if x > len(level) - y_cut_size - 1 - self.generation_specs['padding']:
                            level[x][y] = 0

        #manage files
        if os.path.isfile("Game Files/map.npy"):
            os.remove("Game Files/map.npy")
        if not os.path.isdir("Game Files"):
            os.mkdir("Game Files")
        numpy.save("Game Files/map", level)
