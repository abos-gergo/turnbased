def Distance(tile1, tile2) -> int:
    distx = abs(tile1.x - tile2.x)
    disty = abs(tile1.y - tile2.y)
    return distx + disty