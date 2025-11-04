from pico2d import *
import game_world
import game_framework

class Bird:
    image = None

    def __init__(self, x=400, y=300):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 182, 0, 182, 168, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 5
