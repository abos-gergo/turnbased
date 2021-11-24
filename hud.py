import pygame
import main
import mouse

class zoom:
    def __init__(self, zoom) -> None:
        self.zoom = zoom
        self.height = 300
        self.width = 12
        self.circle_r = self.width / 2
        self.size = pygame.math.Vector2(self.width, self.height)
        self.pos = pygame.math.Vector2(0, 0)
        self.hud_color_mid = (230, 230, 230)
        self.hud_color_bright = (255, 255, 255)
        self.hud_color_dark = (180, 180, 180)
        self.m1_click = False

    def calculate_pos(self, CAM):
        self.pos.x = main.WIN.get_width() - 50 - self.size.x
        self.pos.y = (main.WIN.get_height() + self.size.y)/4

        self.body_rect = pygame.Rect(
                    self.pos.x, self.pos.y, self.size.x, self.size.y)
        self.circle0_pos = pygame.math.Vector2(
            self.pos.x + self.circle_r, self.pos.y)
        self.circle1_pos = pygame.math.Vector2(
            self.pos.x + self.circle_r, self.pos.y + self.size.y)
        self.circle2_pos = pygame.math.Vector2(
            self.pos.x + self.circle_r, 0)

        self.circle2_pos.y = self.pos.y + \
            (self.size.y/(CAM.max_zoom[1]
             + abs(CAM.min_zoom[1])))*CAM.max_zoom[1] + (self.size.y/(CAM.max_zoom[1]
                                                                      + abs(CAM.min_zoom[1])))*self.zoom[1]

    def zoom_by_press(self, CAM):
        if mouse.pos()[0] > self.pos.x and mouse.pos()[0] < self.pos.x + self.size.x:
            if mouse.pos()[1] > self.pos.y and mouse.pos()[1] < self.pos.y + self.size.y:
                self.circle2_pos.y = mouse.pos()[1]
                self.convert_circle_pos_to_zoom(CAM)

    def convert_circle_pos_to_zoom(self, CAM):
        self.zoom[1] = ((1080 + CAM.max_zoom[1])
                        - (1080 + CAM.min_zoom[1]))/300*(self.circle2_pos.y - 325) - 1080 - 57

        self.zoom[0] = self.zoom[1] * 16 / 9

    def draw(self, display, CAM):
        self.calculate_pos(CAM)
        if self.m1_click:
            self.zoom_by_press(CAM)

        pygame.draw.rect(display, self.hud_color_mid, self.body_rect)
        pygame.draw.circle(display, self.hud_color_mid,
                           self.circle0_pos, self.size.x/2)
        pygame.draw.circle(display, self.hud_color_mid,
                           self.circle1_pos, self.size.x/2)
        pygame.draw.circle(display, self.hud_color_bright,
                           self.circle2_pos, self.size.x)

class Button:
    def __init__(self, player):
        self.pos = pygame.math.Vector3(player.x, player.y, player.z)
        self.buttons = {
            "F": pygame.image.load("Assets/buttons/F.png").convert()
        }
        self.buttons["F"].set_colorkey((0, 0,0))

    def display_button(self, display, Pos, collide, enviroment_matrix):
        pos = Pos
        if collide != None:
            display.blit(self.buttons["F"], (pos[0] + self.buttons["F"].get_width()/2, pos[1] - 32))

