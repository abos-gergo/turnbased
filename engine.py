from typing import Any, List
import pygame


def Distance(tile1: Any, tile2: Any) -> int:
    distx = abs(tile1.x - tile2.x)
    disty = abs(tile1.y - tile2.y)
    return distx + disty


def MoveTowards(
    start: tuple[int, int], target: tuple[int, int], speed: float
) -> tuple[int, int]:  # Returns x and y value, both are whole numbers
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
    returned: tuple[int, int] = (dest[0], dest[1])
    return returned
