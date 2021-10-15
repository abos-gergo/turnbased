import pygame
import tiles
import player
from mapgen import Map
from typing import List

def renderTiles(offset, Display):
        for tile in Map.tiles:
            pos: List = [
                (tile.x) * 32 - (tile.y) * 32 + offset[0],
                (tile.x) * 16 + (tile.y) * 16 - tile.z * 32 + offset[1],
            ]

            if pos[0] > -64 and pos[0] < Display.get_width() and pos[1] > -64 and pos[1] < Display.get_height():
                if isinstance(tile, tiles.Rock):
                    Display.blit(tile.tile_type.convert_alpha(), pos)

                elif isinstance(tile, tiles.Tree):
                    pos[1] -= 64
                    Display.blit(tile.tile_type.convert_alpha(), pos)

                elif isinstance(tile, tiles.Dirt):
                    Display.blit(tile.tile_type.convert(), pos)

                elif isinstance(tile, player.Player):
                    pos[1] -= tile.imgy / 4
                    pos[0] += tile.imgx / 2
                    img = pygame.transform.scale(pygame.image.load(
                        "Assets/Player/Melee/Character01/character01-front-left.png"), (32, 64))
                    Display.blit(img, pos)