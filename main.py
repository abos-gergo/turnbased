from map import Map, SCALE, enviroment_matrix, dirt_matrix
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
    # WINDOW SETUP ---------------------------------------------------------------------    WINDOW SETUP
    pygame.display.set_caption("rendkívül keratív név")
    icon = pygame.image.load('Assets/icon/icon.png')
    pygame.display.set_icon(icon)
    pygame.mouse.set_visible(False)
    # MAP GENERATION -------------------------------------------------------------------    MAP GENERATION
    mapgen = generate_map.generate_map(SCALE)
    mapgen.dirt_generation()
    map: Map = Map()
    map.read_tiles(player0)
    # RUN SETUP -------------------------------------------------------------------------  RUN SETUP
    CAM.set_offset_to(player0, WIN)
    clock = pygame.time.Clock() 
    run = True
    tile_in_focus = player0.getTileBelow()
    max_fps = 0
    min_fps = 60
    # LOOP ------------------------------------------------------------------------------  LOOP
    while run:
        #FPS counter
        clock.tick(60)
        fps = clock.get_fps()
        if fps > max_fps:
            max_fps = fps
        if fps < min_fps and fps != 0:
            min_fps = fps

        DISPLAY = pygame.Surface((1920 + CAM.zoom[0], 1080 + CAM.zoom[1]))
        DISPLAY.fill((76.4, 107.3, 121.7))
        collided_tile = engine.collide(player0, enviroment_matrix)
        player0.move()
        interactable = False
        if collided_tile is not None:
            tile_in_focus = dirt_matrix[collided_tile[0]][collided_tile[1]]
            interactable = True

        if CAM.lock:
            CAM.set_offset_to(player0, DISPLAY)
        
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # Mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    CAM.zoom_in()

                if event.button == 5:
                    CAM.zoom_out()

                if event.button == 1:
                    clicked_tile = mouse.click.getClickedTile(CAM.offset, CAM.zoom)
                    if clicked_tile != None:
                        player0.move_direction.y, player0.move_direction.y = 0,0
                        tile_in_focus = clicked_tile
            
            # Keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    CAM.set_offset_to(player0, DISPLAY)

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

                if event.key == pygame.K_z:
                    CAM.lock = CAM.lock * -1 + 1

                if event.key == pygame.K_f:
                    if interactable:
                        enviroment_matrix[collided_tile[0]][collided_tile[1]] = None
                    player0.create_bridge()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player0.move_direction.y = 0
                if event.key == pygame.K_s:
                    player0.move_direction.y = 0
                if event.key == pygame.K_a:
                    player0.move_direction.x = 0
                if event.key == pygame.K_d:
                    player0.move_direction.x = 0

        # Rendering
        render.renderTiles(CAM.move_camera(), DISPLAY, player0, tile_in_focus, hud.Button(player0), collided_tile)
        WIN.blit(pygame.transform.scale(DISPLAY, (1920, 1080)), (0, 0))
        mouse.display_cursor(WIN)
        pygame.display.flip()

    print(f'Max FPS: {max_fps}')
    print(f'Min FPS: {min_fps}')


if __name__ == "__main__":
    main()
