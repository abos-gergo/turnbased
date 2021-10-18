from map import Map
import hud
import camera
import mouse
import generate_map
import pygame
import render

WIN = pygame.display.set_mode((1920, 1080))
DISPLAY = pygame.Surface((1920, 1080))
CAM = camera.Camera(30, 10)
SCALE = 60


def main() -> None:
    # WINDOW SETUP ------------------------------------------------------------ WINDOW SETUP
    pygame.display.set_caption("rendkívül keratív név")
    icon = pygame.image.load('Assets/icon/icon.png')
    pygame.display.set_icon(icon)
    # MAP GENERATION -------------------------------------------------------- MAP GENERATION
    generate_map.generate_map(SCALE).dirt_generation()
    map: Map = Map()
    map.read_dirt()
    CAM.set_offset_to_middle()
    zoom_hud: hud.zoom = hud.zoom(CAM.zoom)
    zoom_in = False
    zoom_out = False
    clock = pygame.time.Clock()
    run = True
    while run:
        DISPLAY = pygame.Surface((1920 + CAM.zoom[0], 1080 + CAM.zoom[1]))
        DISPLAY.fill((76.4, 107.3, 121.7))
        render.renderTiles(CAM.move_camera(), DISPLAY)
        map.tiles = []
        clock.tick(60)

        if zoom_in:
            CAM.zoom_in()

        if zoom_out:
            CAM.zoom_out()

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
                    tile = mouse.click.getClickedTile(CAM.offset, CAM.zoom)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    zoom_hud.m1_click = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    CAM.set_offset_to_middle()
                if event.key == pygame.K_DOWN:
                    zoom_out = True
                elif event.key == pygame.K_UP:
                    zoom_in = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    zoom_out = False
                elif event.key == pygame.K_UP:
                    zoom_in = False

        WIN.blit(pygame.transform.scale(DISPLAY, (1920, 1080)), (0, 0))
        zoom_hud.draw(WIN, CAM)
        pygame.display.flip()


if __name__ == "__main__":
    main()
