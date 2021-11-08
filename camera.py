import main
import mouse
from typing import List


class Camera():
    def __init__(self, camera_speed, display_offset):
        self.offset: List[int] = [0, 0]
        self.camera_speed: int = camera_speed
        self.display_offset: int = display_offset
        self.zoom: List[int] = [0, 0]
        self.zoom_size = 8
        self.max_zoom = (1920 - 16 * self.zoom_size, 1080 - 9 * self.zoom_size)
        self.min_zoom = (-1920 + 16 * self.zoom_size,
                         - 1080 + 9 * self.zoom_size)

    def move_camera(self) -> List[int]:
        if mouse.pos()[0] <= 0 + self.display_offset:
            self.offset[0] += self.camera_speed/(1920/(1920 + self.zoom[0]))

        elif mouse.pos()[0] >= main.WIN.get_width() - self.display_offset:
            self.offset[0] -= self.camera_speed/(1920/(1920 + self.zoom[0]))

        if mouse.pos()[1] <= 0 + self.display_offset:
            self.offset[1] += self.camera_speed/(1080/(1080 + self.zoom[1]))

        elif mouse.pos()[1] >= main.WIN.get_height() - self.display_offset:
            self.offset[1] -= self.camera_speed/(1080/(1080 + self.zoom[1]))

        return self.offset

    def set_offset_to_middle(self):
        self.offset = [(main.WIN.get_width()-main.SCALE + self.zoom[0])/2,
                       (main.WIN.get_height()-main.SCALE*32 + self.zoom[1])/2]

    def set_offset_to_player(self, player):
        self.offset = [(main.WIN.get_width()- (player.x * 32 - player.y * 32)+ self.zoom[0])/2,
                       (main.WIN.get_height()- (player.x * 16 + player.y * 16 - player.z * 32) + self.zoom[1])/2]

    def zoom_in(self):
        if self.zoom[0] > self.min_zoom[0] or self.zoom[1] > self.min_zoom[1]:
            self.zoom[0] -= 16 * self.zoom_size
            self.zoom[1] -= 9 * self.zoom_size

    def zoom_out(self):
        if self.zoom[0] < self.max_zoom[0] or self.zoom[1] < self.max_zoom[1]:
            self.zoom[0] += 16 * self.zoom_size
            self.zoom[1] += 9 * self.zoom_size
