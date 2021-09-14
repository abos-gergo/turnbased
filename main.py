from mapgen import *
import pygame
import player
import noise

WIN = pygame.display.set_mode((1920, 1000))
WIN.fill((149, 149, 149))


def main() -> None:
    scale = 30 #Defines max widht of the map
    noise.createNoise(scale, 3)
    map: Map = Map(300, 1)
    map.generateTiles(scale)
    player1 = player.Player((1, 4, 1), 1)
    Map.renderTiles()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3):
                    pass
        pygame.display.update()


if __name__ == "__main__":
    main()
