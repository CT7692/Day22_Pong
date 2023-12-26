from turtle import Turtle
import secrets

BALL_SPEED = 25
BALL_MEASURE = 1
class Ball(Turtle):
    def __init__(self, initial_x, player_serve):
        super().__init__()
        self.x_pos = initial_x
        self.y_pos = 0
        self.x_speed = BALL_SPEED
        self.player_serve = player_serve
        self.y_direction = secrets.SystemRandom().randint(a=-15, b=15)
        self.shape("square")
        self.up()
        self.shapesize(stretch_wid=BALL_MEASURE, stretch_len=BALL_MEASURE)
        self.color("white")
        self.speed(0)
        self.setpos(self.x_pos, self.y_pos)

    def move(self):
        if self.player_serve:
            self.x_pos += self.x_speed
        elif not self.player_serve:
            self.x_pos -= self.x_speed
        self.y_pos += self.y_direction
        self.goto(self.x_pos, self.y_pos)

    def bounce(self):
        if self.y_direction < 1 and self.y_direction > -1:
            self.y_direction += 1.5
        self.y_direction *= -1
        self.y_direction /= 2
        if not self.player_serve:
            self.player_serve = True
        elif self.player_serve:
            self.player_serve = False

    def rim_bounce(self):
        if self.y_direction < 1 and self.y_direction > -1:
            self.y_direction += 2
        self.y_direction *= -2
        if not self.player_serve:
            self.player_serve = True
        elif self.player_serve:
            self.player_serve = False



