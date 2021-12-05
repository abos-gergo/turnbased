from typing import Any, List
import pygame
import map
import math


def tileDistance(tile1: Any, tile2: Any) -> int:
    distx = abs(tile1.x - tile2.x)
    disty = abs(tile1.y - tile2.y)
    return distx + disty

def pixelDistance(pos1: tuple, pos2: tuple) -> int:
    distx = abs(pos1[0] - pos2[0])
    disty = abs(pos1[1] - pos2[1])
    #dist = math.sqrt(distx ** 2 + disty ** 2)
    return (distx, disty)

def MoveTowards(start: tuple, target: tuple, speed: float) -> tuple:
    # Returns x and y value, both are whole numbers
    dest: List[int] = []
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
        dest = list(target)
    returned: tuple = (dest[0], dest[1])
    return returned

def collide(tile, matrix):

    # returns with the coillided tile -> the location of the obj (based on the enviroment_matrix)

    if matrix[tile.getTileBelow().y + int(tile.look_dir.y)][tile.getTileBelow().x + int(tile.look_dir.x)] != None:
        return tile.getTileBelow().y + int(tile.look_dir.y), tile.getTileBelow().x + int(tile.look_dir.x)
    return None

def convertTileToScreenPos(tile, offset: tuple, zoom : List[int]) -> tuple:
    screen_pos = ((tile.x) * 32 - (tile.y) * 32 + offset[0] + 32)*(1920/(1920 + zoom[0])), ((tile.x) * 16 + (tile.y) * 16 - tile.z * 32 + offset[1] + 16)*(1080/(1080 + zoom[1]))
    return screen_pos
            

