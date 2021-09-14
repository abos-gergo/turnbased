from mapgen import *
import pygame
from pygame import *
import engine
import player
import noise

WIN = pygame.display.set_mode((1920, 1000))
WIN.fill((149, 149, 149))


def main() -> None:
    print(noise.createNoise(100, 1))
    map: Map = Map(300, 1)
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
                    pass
        pygame.display.update()


if __name__ == "__main__":
    main()
