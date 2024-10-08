from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    def update(self): pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball41x41.png')
        self.image2 = load_image('ball21x21.png')
        self.size = random.randint(1,2)
        self.speed = random.randint(3,10)
    def update(self):
        if self.y > 41 / 2 + 55 and self.size == 1:
            self.y -= self.speed
        if self.y > 21 / 2 + 55 and self.size == 2:
            self.y -= self.speed
    def draw(self):
        if self.size==1:
            self.image.draw(self.x,self.y)
        if self.size==2:
            self.image2.draw(self.x,self.y)

def reset_world():
    global running
    global grass
    global team
    global balls
    global world
    running = True
    world = []
    balls = [ball() for i in range(20)]
    world += balls
    grass = Grass()
    world.append(grass)
    team = [Boy() for i in range(10)]
    world += team


def update_world():
    grass.update()
    for o in world:
        o.update()
    for ball in balls:
        ball.update()
    for boy in team:
        boy.update()

    pass
def render_world():
    clear_canvas()
    grass.draw()
    for o in world:
        o.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()

    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

# initialization code

# game main loop code
reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
