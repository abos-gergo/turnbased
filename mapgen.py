from typing import List
import engine
import random

class Tile:
    def __init__(self, x:int, y:int, z:int) -> None:
        self.x = x
        self.y = y
        self.z = z


class Map:
    tiles : List[Tile] = []
    maxsize : int
    tilecount : int

    def __init__(self, maxsize : int, tilecount: int) -> None:
        self.maxsize = maxsize
        self.tilecount = tilecount

    def generateTiles(map):
        tile = Tile(0, 0, 0)
        map.tiles.append(tile)
        freespaces : List[tuple] = []
        placedtiles : int = 0
        while placedtiles != map.tilecount - 1:
            # Get neighbours ---------------------------------
            for tile in map.tiles:
                fr : List[bool] = [0, 0, 0, 0]
                for neighbor in map.tiles:
                    if engine.Distance(tile, neighbor) == 1:
                        if neighbor.x < 0 or neighbor.x > map.maxsize / 2 or neighbor.y < 0 or neighbor.y > map.maxsize / 2:
                            if neighbor.y < tile.y: # NE
                                fr[0] = 1
                            elif neighbor.x > tile.x: #SE
                                fr[1] = 1
                            elif neighbor.y > tile.y: #SW
                                fr[2] = 1
                            elif neighbor.x < tile.x: #NW
                                fr[3] = 1
                for i, v in enumerate(fr):
                    if i == 0 and v == 0:
                        pos = (tile.x, tile.y - 1)
                        freespaces.append(pos)
                    elif i == 1 and v == 0:
                        pos = (tile.x + 1, tile.y)
                        freespaces.append(pos)
                    elif i == 2 and v == 0:
                        pos = (tile.x, tile.y + 1)
                        freespaces.append(pos)
                    elif i == 3 and v == 0:
                        pos = (tile.x  - 1, tile.y)
                        freespaces.append(pos)
            freespace = freespaces[random.randint(0, freespaces.__len__() - 1)]
            map.tiles.append(Tile(freespace[0], freespace[1], 0))
            placedtiles += 1



map : Map = Map(10, 1)
map.generateTiles()