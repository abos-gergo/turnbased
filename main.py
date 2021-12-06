from map import Map, SCALE, enviroment_matrix, none_matrix
import hud
import camera
import mouse
import generate_map
import pygame
from player import Player
import render
import engine

WIN = pygame.display.set_mode((1920, 1080))
DISPLAY = pygame.Surface((1920, 1080))
CAM = camera.Camera(30, 10)

player0 = Player(0, SCALE)

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
    CAM.set_offset_to(player0, WIN)
    zoom_hud: hud.zoom = hud.zoom(CAM.zoom)
    clock = pygame.time.Clock() 
    run = True
    selected_tiles: list = [player0.getTileBelow()]
    select_tiles = False
    stopped = False
    click = False
    while run:
        pygame.mouse.set_visible(False)
        DISPLAY = pygame.Surface((1920 + CAM.zoom[0], 1080 + CAM.zoom[1]))
        DISPLAY.fill((76.4, 107.3, 121.7))
        collided_tile = engine.collide(player0, enviroment_matrix)
        map.tiles = []
        clock.tick(60)
        if select_tiles == False:
            if player0.move_on_selected_way(selected_tiles) or stopped:
                selected_tiles = [player0.getTileBelow()]
                player0.way_index = 0

        interactable = False
        if collided_tile is not None:
            interactable = True

        if CAM.lock:
            CAM.set_offset_to(player0, DISPLAY)

        if click and select_tiles:
            clicked_tile = mouse.click.getClickedTile(CAM.offset, CAM.zoom)
            if clicked_tile != None:
                if engine.tileDistance(selected_tiles[-1], clicked_tile) == 1 and clicked_tile not in selected_tiles:
                    selected_tiles.append(clicked_tile)

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
                    click = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    zoom_hud.m1_click = False
                    click = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    CAM.set_offset_to(player0, DISPLAY)

                if event.key == pygame.K_f:
                    if interactable:
                        enviroment_matrix[collided_tile[0]][collided_tile[1]] = None
                    player0.create_bridge()
                if event.key == pygame.K_z:
                    CAM.lock = CAM.lock * -1 + 1

                if event.key == pygame.K_LCTRL:
                    select_tiles = True

                if event.key == pygame.K_s:
                    stopped = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LCTRL:
                    select_tiles = False
                if event.key == pygame.K_s:
                    stopped = False

        render.renderTiles(CAM.move_camera(), DISPLAY, player0, selected_tiles, hud.Button(player0), collided_tile)
        WIN.blit(pygame.transform.scale(DISPLAY, (1920, 1080)), (0, 0))
        zoom_hud.draw(WIN, CAM)
        mouse.display_cursor(WIN)
        pygame.display.flip()


if __name__ == "__main__":
    main()
