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
            if engine.Distance(self, neighbor) <= 1:
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
        for tile in Map.tiles:
            string : str = ''
            spaces = 0
            for space in self.neighbors:
                if space == False:
                    spaces += 1
            if spaces == 1:
                pass

            elif spaces == 2:
                if tile.neighbors[0] == 0 and tile.neighbors[1] == 0:
                    string = 'W'
                elif tile.neighbors[0] == 0 and tile.neighbors[3] == 0:
                    string = 'S'
                elif tile.neighbors[2] == 0 and tile.neighbors[3] == 0:
                    string = 'E'
                elif tile.neighbors[2] == 0 and tile.neighbors[1] == 0:
                    string = 'N'

            elif spaces == 3:
                if tile.neighbors[0]  == 0 and tile.neighbors[1]  == 0 and tile.neighbors[2] == 0:
                    string = 'NW'
                elif tile.neighbors[1]  == 0 and tile.neighbors[2]  == 0 and tile.neighbors[3] == 0:
                    string = 'NE'
                elif tile.neighbors[2]  == 0 and tile.neighbors[3]  == 0 and tile.neighbors[0] == 0:
                    string = 'SE'
                elif tile.neighbors[3]  == 0 and tile.neighbors[0]  == 0 and tile.neighbors[1] == 0:
                    string = 'SW'

            elif spaces == 4:
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
        Map.tiles.append(Tile(0 + self.maxsize / 2, 0 + self.maxsize / 2, 0))
        freespaces : List[tuple] = []
        placedtiles : int = 1
        while placedtiles != self.tilecount:
            freespaces.clear()
            for tile in Map.tiles:
                tile.getNeighbors(self)
                for freespace in tile.neighbors:
                    freespaces.append(freespace)
            freespace = freespaces[random.randint(0, freespaces.__len__() - 1)]
            if freespace[0] <= 0 or freespace[0] > self.maxsize or freespace[1] <= 0 or freespace[1] > self.maxsize:
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
                    pos : tuple = (944 + (tile.x - 1) * 32 - (tile.y - 1) * 32, 529 + (tile.x - 1) * 16 + (tile.y - 1) * 16)
                    print(f'Image at: {(tile.x, tile.y)}')
                    main.WIN.blit(pygame.image.load('Assets/Map/Test.png'), pos)
                    pygame.display.update()
                    row.remove(tile)
                    temptiles.remove(tile)
            