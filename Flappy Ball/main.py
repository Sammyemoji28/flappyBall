
import pgzrun

HEIGHT = 800
WIDTH = 800
TITLE = "flappy ball"

GRAVITY = 2000 #pixels per second

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 200
        self.vel_y = 0
        self.radius = 40
    def drawBall(self):
        screen.draw.filled_circle((self.x, self.y), self.radius, "white")

ball = Ball(100,50)

def draw():
    screen.clear() 
    ball.drawBall()

def update(c):
    # applying constent accelertion
    initalY = ball.vel_y
    ball.vel_y += GRAVITY * c
    ball.y += (initalY + ball.vel_y) * 0.5 * c

    #detecting the ground and handling the bounce
    if ball.y > HEIGHT - ball.radius:
        ball.y = HEIGHT - ball.radius
        ball.vel_y = -ball.vel_y * 0.9
    ball.x += ball.vel_x * c
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vel_x = -ball.vel_x

def on_key_down(key):
    if key == keys.SPACE:
        ball.vel_y = -500

pgzrun.go()