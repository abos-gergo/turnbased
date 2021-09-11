from mapgen import *
import pygame
from pygame import *

WIN = pygame.display.set_mode((1920, 900))
WIN.fill((255, 255, 255))

def main() -> None:
    map : Map = Map(18, 100)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == "__main__":
    main()