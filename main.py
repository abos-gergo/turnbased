import pygame
WIN = pygame.display.set_mode((1920, 1000), pygame.FULLSCREEN)

import mouse
import mapgen
import engine
import noise
import camera

CAM = camera.Camera(25, 40)

def main() -> None:
    scale = 10
    print(noise.createNoise(scale, 3))
    map: mapgen.Map = mapgen.Map(300, 1)
    #player1 = player.Player((1, 4, 1), 1)
    clock = pygame.time.Clock()
    map.generateTiles(scale)
    run = True
    pos: tuple(int) = (0, 0)
    while run:
        WIN.fill((149, 149, 149))
        mapgen.Map.renderTiles(CAM.move_camera())
        map.tiles = []
        clock.tick(60)
        pos = engine.MoveTowards(pos, (1820, 980), 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3):
                    tile = mouse.click.getClickedTile(CAM.offset)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        pygame.display.update()


if __name__ == "__main__":
    main()
