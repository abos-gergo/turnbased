import random
import pygame
import generate_map


class Tree:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.tree0_img = pygame.image.load(
            "Assets/decorations/Tree01.png")
        self.tree1_img = pygame.image.load(
            "Assets/decorations/Tree02.png")
        self.imgx = self.tree0_img.get_width()
        self.imgy = self.tree0_img.get_height()
        self.z = 1
        self.tree_type = "Tree"

    def get_tree_type(self):
        return random.choice((pygame.image.load(
            "Assets/decorations/Tree02.png"), pygame.image.load(
                "Assets/decorations/Tree01.png"), pygame.image.load(
                    "Assets/decorations/Tree03.png")))


class Rock:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.img = pygame.image.load('Assets/decorations/rock01.png')
        self.imgx = self.img.get_width()
        self.imgy = self.img.get_height()
        self.z = 1
        self.rock_type = "Rock"

    def get_rock_type(self):
        return random.choice((pygame.image.load(
            "Assets/decorations/rock01.png"), pygame.image.load(
                "Assets/decorations/rock02.png")))
