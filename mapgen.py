from typing import List
import engine
import random
from assets import Sprites
import main
import pygame

class Tile:
    def __init__(self, x:int, y:int, z:int) -> None:
        self.x : int = x
        self.y : int = y
        self.z : int = z
        self.neighbors : List[tuple] = []

    def getNeighbors(self, map):
        neighborspos : List[tuple] = []
        neighbors : List[bool] = [0, 0, 0, 0]
        for neighbor in Map.tiles:
            if engine.Distance(self, neighbor) == 1:
                if neighbor.y < self.y: # NE
                    neighbors[0] = 1
                elif neighbor.x > self.x: #SE
                    neighbors[1] = 1
                elif neighbor.y > self.y: #SW
                    neighbors[2] = 1
                elif neighbor.x < self.x: #NW
                    neighbors[3] = 1
        for i, v in enumerate(neighbors):
            if i == 0 and v == 0:
                pos = (self.x, self.y - 1)
                neighborspos.append(pos)
            if i == 1 and v == 0:
                pos = (self.x + 1, self.y)
                neighborspos.append(pos)
            if i == 2 and v == 0:
                pos = (self.x, self.y + 1)
                neighborspos.append(pos)
            if i == 3 and v == 0:
                pos = (self.x  - 1, self.y)
                neighborspos.append(pos)
        self.neighbors = neighborspos

    def getTileType(self) -> str:
        string : str = ''
        neighborscount = 0
        neighbors : List[bool] = [0, 0, 0, 0]
        for neighbor in Map.tiles:
            if engine.Distance(self, neighbor) == 1:
                if neighbor.y < self.y: # NE
                    neighbors[0] = 1
                elif neighbor.x > self.x: #SE
                    neighbors[1] = 1
                elif neighbor.y > self.y: #SW
                    neighbors[2] = 1
                elif neighbor.x < self.x: #NW
                    neighbors[3] = 1
        for neighbor in neighbors:
            if neighbor == 1:
                neighborscount += 1
        if neighborscount == 1:
            if neighbors[0] == 1:
                string = 'S_NE'
            if neighbors[1] == 1:
                string = 'W_SE'
            if neighbors[2] == 1:
                string = 'E_SW'
            if neighbors[3] == 1:
                string = 'S_NW'

        elif neighborscount == 2:
            if neighbors[0] == 0 and neighbors[1] == 0:
                string = 'E'
            elif neighbors[0] == 0 and neighbors[3] == 0:
                string = 'N'
            elif neighbors[2] == 0 and neighbors[3] == 0:
                string = 'W'
            elif neighbors[2] == 0 and neighbors[1] == 0:
                string = 'S'
            elif neighbors[0] == 0 and neighbors[2] == 0:
                string = 'SE_NW'
            elif neighbors[1] == 0 and neighbors[3] == 0:
                string = 'NE_SW'

        elif neighborscount == 3:
            if neighbors[0]  == 1 and neighbors[1]  == 1 and neighbors[2] == 1:
                string = 'NW'
            elif neighbors[1]  == 1 and neighbors[2]  == 1 and neighbors[3] == 1:
                string = 'NE'
            elif neighbors[2]  == 1 and neighbors[3]  == 1 and neighbors[0] == 1:
                string = 'SE'
            elif neighbors[3]  == 1 and neighbors[0]  == 1 and neighbors[1] == 1:
                string = 'SW'

        elif neighborscount == 4:
            string = 'M'

        return string

class Map:
    tiles : List[Tile] = []
    maxsize : int
    tilecount : int

    def __init__(self, maxsize : int, tilecount: int) -> None:
        self.maxsize = maxsize
        self.tilecount = tilecount
        Map.generateTiles(self)

    def generateTiles(self):
        Map.tiles.append(Tile(0, 0, 0))
        freespaces : List[tuple] = []
        placedtiles : int = 1
        while placedtiles != self.tilecount:
            freespaces.clear()
            for tile in Map.tiles:
                tile.getNeighbors(self)
                for freespace in tile.neighbors:
                    freespaces.append(freespace)
            freespace = freespaces[random.randint(0, freespaces.__len__() - 1)]
            if freespace[0] < -self.maxsize / 2 or freespace[0] >= self.maxsize / 2 or freespace[1] < -self.maxsize / 2 or freespace[1] >= self.maxsize / 2:
                continue
            Map.tiles.append(Tile(freespace[0], freespace[1], 0))
            placedtiles += 1

        temptiles : List[Tile] = list(Map.tiles)
        row : List[Tile] = []
        lowx = temptiles[0].x
        lowy = temptiles[0].y
        highx = temptiles[0].x
        highy = temptiles[0].y
        for tile in temptiles:
            if tile.x < lowx:
                    lowx = tile.x
            elif tile.x > highx:
                highx = tile.x
            if tile.y < lowy:
                lowy = tile.y
            elif tile.y > highy:
                highy = tile.y
        
        while temptiles.__len__() != 0:
            row.clear()
            lowx = temptiles[0].x
            lowy = temptiles[0].y
            highx = temptiles[0].x
            highy = temptiles[0].y

            for tile in temptiles:
                if tile.x < lowx:
                    lowx = tile.x
                elif tile.x > highx:
                    highx = tile.x
            origin = ()
            for tile in temptiles:
                if tile.x == lowx:
                    row.append(tile)

            lowy : int = row[0].y
            for tile in row:
                if tile.y < lowy:
                    lowy = tile.y
                elif tile.y > highy:
                    highy = tile.y

            for tile in row:
                if tile.y == lowy:
                    pos : tuple = (944 + (tile.x) * 32 - (tile.y) * 32, 529 + (tile.x) * 16 + (tile.y) * 16)
                    tiletype : str = tile.getTileType()
                    if (tile.x, tile.y) == (0, 0):
                        main.WIN.blit(pygame.image.load('Assets/Map/Test.png'), pos)
                    elif tiletype.__len__() != 0:
                        main.WIN.blit(pygame.image.load('Assets/Map/' + tiletype + '_Tile.png'), pos)
                    else:
                        main.WIN.blit(pygame.image.load('Assets/Map/Test.png'), pos)
                    pygame.display.update()
                    row.remove(tile)
                    temptiles.remove(tile)