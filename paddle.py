from turtle import Turtle

PADDLE_MOVEMENT = 40

class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.up()
        self.x_pos = x_pos
        self.y_pos = 0
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(self.x_pos, self.y_pos)


    def move_up(self):
        self.y_pos += PADDLE_MOVEMENT
        self.sety(self.y_pos)

    def move_down(self):
        self.y_pos -= PADDLE_MOVEMENT
        self.sety(self.y_pos)