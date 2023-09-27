from turtle import Turtle
from paddle import Paddle

Y_POS = 220
ALIGNMENT = "center"
MY_FONT = ('OCR A Extended', 40, 'normal')


class Player(Turtle):
    score = 0
    scored = False
    def __init__(self, scoreboard_x, paddle_x, boundary):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color("white")
        self.setpos(scoreboard_x, Y_POS)
        self.update_score()
        self.paddle = Paddle(paddle_x)

    def scored_point(self):
        self.clear()
        self.score += 1
        self.update_score()

    def update_score(self):
        self.write(arg=f"{self.score}", move=False, align=ALIGNMENT, font=MY_FONT)
