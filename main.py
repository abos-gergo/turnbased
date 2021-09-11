from mapgen import *
import pygame
from pygame import *

WIN = pygame.display.set_mode((1920, 1080))
WIN.fill((149, 149, 149))

def main() -> None:
    map : Map = Map(50, 400)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == "__main__":
    main()