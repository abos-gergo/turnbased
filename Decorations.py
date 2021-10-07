import random
import pygame


class Tree:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.tree_img = pygame.image.load(
            "Assets/decorations/Tree01.png")
        self.imgx = self.tree_img.get_width()
        self.imgy = self.tree_img.get_height()
        self.z = 1
