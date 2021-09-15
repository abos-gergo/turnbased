import main, mouse
from typing import List


class Camera():
    def __init__(self, camera_speed, display_offset):
        self.offset : List[int] = [0, 0]
        self.offset_change : int = 0
        self.camera_speed : int = camera_speed
        self.display_offset : int= display_offset

    def move_camera(self) -> None:
        if mouse.pos()[0] <= 0 + self.display_offset:
            self.offset[0] += self.camera_speed

        elif mouse.pos()[0] >= main.WIN.get_width() - self.display_offset:
            self.offset[0] -= self.camera_speed

        if mouse.pos()[1] <= 0 + self.display_offset:
            self.offset[1] += self.camera_speed

        elif mouse.pos()[1] >= main.WIN.get_height() - self.display_offset:
            self.offset[1] -= self.camera_speed

        return self.offset