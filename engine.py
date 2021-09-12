import math
from typing import List
import numpy as np
import pygame



def Distance(tile1, tile2) -> int:
    distx = abs(tile1.x - tile2.x)
    disty = abs(tile1.y - tile2.y)
    return distx + disty


def MoveTowards(start: tuple, target: tuple, speed: float) -> tuple: # Returns x and y value, both are whole numbers
    dest : List = []
    if start != target:
        startvector = pygame.Vector2(start)
        targetvector = pygame.Vector2(target)
        towards = (targetvector - startvector).normalize() * speed
        dest = [round(start[0] + towards[0]), round(start[1] + towards[1])]
        if dest[0] > target[0]:
            dest[0] = target[0]
        if dest[1] > target[1]:
            dest[1] = target[1]
    else:
        dest = target
    return tuple(dest)
