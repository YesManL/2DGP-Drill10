from pico2d import *
import game_world
import game_framework

class Bird:
    image = None

    def __init__(self, x=400, y=300, velocity=2.0):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0
        self.velocity = velocity
        self.dir = 1

        self.size_x = 1.2
        self.size_y = 1.2
        self.width = int(182 * self.size_x)
        self.height = int(168 * self.size_y)

        self.flap_speed = 0.15
        self.frame_float = 0.0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 182, 0, 182, 168, self.x, self.y, self.width, self.height)
        else:
            self.image.clip_composite_draw(int(self.frame) * 182, 0, 182, 168, 0, 'h', self.x, self.y, self.width, self.height)

    def update(self):
        self.frame_float += self.flap_speed
        self.frame = int(self.frame_float) % 5

        self.x += self.velocity * self.dir

        if self.x < 100 or self.x > 1500:
            self.dir *= -1

# 2023182044 게임공학과 임호권
