import m_click_det
from mapgen import *
import pygame
from m_click_det import *
from pygame import *
import engine

WIN = pygame.display.set_mode((1920, 1080))
WIN.fill((149, 149, 149))


def main() -> None:
    map: Map = Map(50, 400)

    clock = pygame.time.Clock()
    run = True
    pos: tuple(int) = (0, 0)
    while run:
        clock.tick(60)
        m_click_det.mouse_click.tile_detection(mouse_click())
        pos = engine.MoveTowards(pos, (1820, 980), 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()


if __name__ == "__main__":
    main()
