import mapgen
from mapgen import *
import pygame
from pygame import *
import engine
import player
import noise
import camera

WIN = pygame.display.set_mode((1920, 1000), pygame.FULLSCREEN)
CAM = camera.Camera(25, 40)

def main() -> None:
    scale = 20
    print(noise.createNoise(scale, 3))
    map: Map = Map(300, 1)
    player1 = player.Player((1, 4, 1), 1)
    clock = pygame.time.Clock()
    map.generateTiles(scale)
    run = True
    pos: tuple(int) = (0, 0)
    while run:
        WIN.fill((149, 149, 149))
        Map.renderTiles(CAM.move_camera())
        map.tiles = []
        clock.tick(60)
        pos = engine.MoveTowards(pos, (1820, 980), 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3):
                    pass
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        pygame.display.update()


if __name__ == "__main__":
    main()
