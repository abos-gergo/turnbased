import pygame, mapgen, main
from pygame import *


class mouse_click:
    def __init__(self):
        self.mouse_pos_ = []
        self.tile_pos = []
        self.chosen_tile_pos = []
        self.rect_offset = 5
        self.tile = mapgen.Map.tiles[0]


    def mouse_pos(self):
        self.mouse_pos_ = pygame.mouse.get_pos()
        return self.mouse_pos_

    def tile_detection(self):
        for tile in mapgen.Map.tiles:
            tile_posX = 944 + (tile.x - 1) * 32 - (tile.y - 1) * 32
            tile_posY = 529 + (tile.x - 1) * 16 + (tile.y - 1) * 16
            self.tile_pos = [
                tile_posX,
                tile_posY,
            ]  # [(main.WIN.get_width()-64)/2 + (tile.x - 1) * 32 - (tile.y - 1) * 32, (main.WIN.get_height()-32)/2 + (tile.x - 1) * 16 + (tile.y - 1) * 16)]

            if (
                self.tile_pos[0] + 64 - self.rect_offset > self.mouse_pos()[0]
                and self.tile_pos[0] + self.rect_offset < self.mouse_pos()[0]
                and self.tile_pos[1] + 32 - self.rect_offset > self.mouse_pos()[1]
                and self.tile_pos[1] + self.rect_offset < self.mouse_pos()[1]
            ):  # mivel nem négyzet hanem rombusz, nem tudtam tökéletesen megírni, hogy pontosan érzékelje  aszéleket, így a rombuszok legszélén nem érzékeli a kattintást. Minden tileon egy (64-offset*2) * (32-offset*2) téglalapon érzékel csak
                self.chosen_tile_pos = list(self.tile_pos)
                self.tile = tile
        print(self.tile)
        return self.tile
