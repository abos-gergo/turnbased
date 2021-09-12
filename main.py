import m_click_det
from mapgen import *
import pygame
from m_click_det import *
from pygame import *
import engine
import player

WIN = pygame.display.set_mode((1920, 1000))
WIN.fill((149, 149, 149))


def main() -> None:
    map: Map = Map(50, 300)
    player1 = player.Player((1, 4, 1), 1)
    Map.renderTiles()
    clock = pygame.time.Clock()
    run = True
    pos: tuple(int) = (0, 0)
    while run:
        clock.tick(60)
        pos = engine.MoveTowards(pos, (1820, 980), 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3):
                    m_click_det.mouse_click.tile_detection(mouse_click())
        pygame.display.update()


if __name__ == "__main__":
    main()
