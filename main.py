import pygame
from pygame import display
WIN = pygame.display.set_mode((1920, 1000), pygame.FULLSCREEN)

import mouse
import mapgen
import engine
import noise
import camera

CAM = camera.Camera(25, 40)
SCALE = 60

def main() -> None:
    key_up = False
    noise.createNoise(SCALE)
    map: mapgen.Map = mapgen.Map(300, 1)
    #player1 = player.Player((1, 4, 1), 1)
    clock = pygame.time.Clock()
    map.generateTiles(SCALE)
    CAM.set_offset_to_middle()
    run = True
    pos: tuple(int) = (0, 0)
    while run:
        DISPLAY = pygame.Surface((1920 + CAM.zoom[0], 1080 + CAM.zoom[1]))
        DISPLAY.fill((147, 147, 147))
        mapgen.Map.renderTiles(CAM.move_camera(), DISPLAY)
        map.tiles = []
        clock.tick(60)
        pos = engine.MoveTowards(pos, (1820, 980), 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 4:
                    CAM.zoom_in()
                if event.button == 5:
                    CAM.zoom_out()

                if event.button == 1:
                    tile = mouse.click.getClickedTile(CAM.offset, CAM.zoom)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                
                if event.key == pygame.K_SPACE:
                    CAM.set_offset_to_middle()
                

        WIN.blit(pygame.transform.scale(DISPLAY, (1920, 1080)), (0,0))
        pygame.display.update()


if __name__ == "__main__":
    main()
