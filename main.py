from map import Map
import hud
import camera
import mouse
import generate_map
import pygame
from player import Player
import render

WIN = pygame.display.set_mode((1920, 1080))
DISPLAY = pygame.Surface((1920, 1080))
CAM = camera.Camera(30, 10)
SCALE = 70

player0 = Player(0, 70)

def main() -> None:
    # WINDOW SETUP ------------------------------------------------------------ WINDOW SETUP
    pygame.display.set_caption("rendkívül keratív név")
    icon = pygame.image.load('Assets/icon/icon.png')
    pygame.display.set_icon(icon)
    # MAP GENERATION -------------------------------------------------------- MAP GENERATION
    mapgen = generate_map.generate_map(SCALE)
    mapgen.dirt_generation()
    map: Map = Map()
    map.read_tiles(player0)
    CAM.set_offset_to_middle()
    zoom_hud: hud.zoom = hud.zoom(CAM.zoom)
    clock = pygame.time.Clock() 
    run = True
    tile = player0.getTileBelow()
    while run:
        pygame.mouse.set_visible(False)
        DISPLAY = pygame.Surface((1920 + CAM.zoom[0], 1080 + CAM.zoom[1]))
        DISPLAY.fill((76.4, 107.3, 121.7))
        render.renderTiles(CAM.move_camera(), DISPLAY, player0, tile)
        map.tiles = []
        clock.tick(60)
        player0.move()
        tile = player0.getTileBelow()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    CAM.zoom_in()
                if event.button == 5:
                    CAM.zoom_out()
                if event.button == 1:
                    zoom_hud.m1_click = True
                    clicked_tile = mouse.click.getClickedTile(CAM.offset, CAM.zoom)
                    if clicked_tile != None:
                        player0aa.move_direction.y, player0.move_direction.y = 0,0
                        tile = clicked_tile

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    zoom_hud.m1_click = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    CAM.set_offset_to_middle()

                if event.key == pygame.K_w:
                    player0.move_direction.y = -1
                    player0.move_direction.x = 0

                if event.key == pygame.K_s:
                    player0.move_direction.y = 1
                    player0.move_direction.x = 0

                if event.key == pygame.K_a:
                    player0.move_direction.x = -1
                    player0.move_direction.y = 0

                if event.key == pygame.K_d:
                    player0.move_direction.x = 1
                    player0.move_direction.y = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player0.move_direction.y = 0
                if event.key == pygame.K_s:
                    player0.move_direction.y = 0
                if event.key == pygame.K_a:
                    player0.move_direction.x = 0
                if event.key == pygame.K_d:
                    player0.move_direction.x = 0

        WIN.blit(pygame.transform.scale(DISPLAY, (1920, 1080)), (0, 0))
        zoom_hud.draw(WIN, CAM)
        mouse.display_cursor(WIN)
        pygame.display.flip()


if __name__ == "__main__":
    main()
