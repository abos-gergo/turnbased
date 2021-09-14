from typing import List
from opensimplex import *
import random
import numpy
import engine


def createNoise(scale, precision = 10):
    midpoint = (scale / 2, scale / 2)
    matrix: List[List] = []
    seed: int = random.randint(1, 99999)
    tmp = OpenSimplex(seed)
    row: List = []
    row.append(0)
    row.append(0)
    for x in range(scale):
        row.append(0)
    matrix.append(row)

    for y in range(scale):
        row: List = [0]
        for x in range(scale):
            z = (tmp.noise2d(x, y) + 1) / 2
            threshold = engine.pixelDistance(midpoint, (x, y)) / scale + 0.1
            z = 1 if z > threshold else 0
            row.append(z)
        row.append(0)
        matrix.append(row)

    row.clear()
    row.append(0)
    row.append(0)
    for x in range(scale):
        row.append(0)
    matrix.append(row)

    for _ in range(precision):
        for y in range(scale):
            y += 1
            for x in range(scale):
                x += 1
                neighborscount = 0
                if matrix[x][y - 1]: neighborscount += 1
                if matrix[x + 1][y]: neighborscount += 1
                if matrix[x][y + 1]: neighborscount += 1
                if matrix[x - 1][y]: neighborscount += 1
                
                if neighborscount == 0 :
                    matrix[x][y] = 0
                elif neighborscount == 4 or neighborscount == 3:
                    matrix[x][y] = 1

    numpy.savetxt("map.csv", matrix)  
