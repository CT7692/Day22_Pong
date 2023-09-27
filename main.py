from turtle import Turtle, Screen
from player import Player, MY_FONT, ALIGNMENT
from paddle import Paddle
from ball import Ball
from time import sleep

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
HIGH_BOUND = 300
LOW_BOUND = -300
P1_BOARD_X = -100
P2_BOARD_X= 100
P1_PADDLE_X = -360
P2_PADDLE_X = 360
P1_GOAL_X = -400
P2_GOAL_X = 400
PADDLE_COLLISION = 50

def get_screen():
    scr_obj = Screen()
    scr_obj.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    scr_obj.bgcolor("black")
    scr_obj.title("Pong")
    return scr_obj

def draw_line():
    y_pos = HIGH_BOUND
    while y_pos != LOW_BOUND:
        line = Turtle(shape="square")
        line.color("white")
        line.up()
        line.sety(y_pos)
        y_pos -= 40


def gameplay(p1, screen_obj):
    screen_obj.listen()
    screen_obj.onkeypress(key="p", fun=p1.paddle.move_up)
    screen_obj.onkeypress(key="l", fun=p1.paddle.move_down)

def computer_play(p2, ball, screen_obj):
    if (ball.player_serve and p2.paddle.ycor() < ball.ycor() - 30
            and ball.xcor() > P1_GOAL_X and ball.xcor() < P2_GOAL_X):
        p2.paddle.move_up()
    elif (ball.player_serve and p2.paddle.ycor() > ball.ycor() + 30
          and ball.xcor() > P1_GOAL_X and ball.xcor() < P2_GOAL_X):
        p2.paddle.move_down()


def wall_collision(ball):
    high_condition = ball.ycor() > HIGH_BOUND - 20
    low_condition = ball.ycor() < LOW_BOUND + 20
    if high_condition or low_condition:
        ball.y_direction *= -1

def paddle_collision(p1, p2, ball):
    if p1.paddle.distance(ball) < PADDLE_COLLISION and ball.xcor() > p1.paddle.xcor():
        if ball.ycor() > p1.paddle.ycor() + 20 or ball.ycor() < p1.paddle.ycor() - 20:
            ball.rim_bounce()
        else:
            ball.bounce()
    elif p2.paddle.distance(ball) < PADDLE_COLLISION and ball.xcor() < p2.paddle.xcor():
        if ball.ycor() > p1.paddle.ycor() + 20 or ball.ycor() < p1.paddle.ycor() - 20:
            ball.rim_bounce()
        else:
            ball.bounce()


def get_result(p1, p2, ball):
    result = Turtle()
    if p1.score == 11:
        result.color("blue")
        result.write(arg="Player Wins", move=False, align=ALIGNMENT, font=MY_FONT)
    elif p2.score == 11:
        result.color("red")
        result.write(arg="Computer Wins", move=False, align=ALIGNMENT, font=MY_FONT)
    return result

def play(p1, p2, ball, screen_obj):
    ball_served = True
    while ball_served:
        sleep(0.1)
        screen_obj.update()
        ball.move()
        gameplay(p1, screen_obj)
        computer_play(p2, ball, screen_obj)
        wall_collision(ball)
        paddle_collision(p1, p2, ball)
        ball_served = goal(p1, p2, ball, screen_obj)
        ball = get_new_ball(p1, p2, ball, screen_obj)
        if p1.score < 11 and p2.score < 11:
            ball_served = True
        else:
            ball_served = False
            outcome = get_result(p1, p2, ball)

def goal(p1, p2, ball, screen_obj):
    is_served = True
    if ball.xcor() > P2_GOAL_X:
        is_served = False
        p1.scored_point()
        p1.scored = True
        p2.scored = False
    elif ball.xcor() < P1_GOAL_X:
        is_served = False
        p2.scored_point()
        p1.scored = False
        p2.scored = True
    return is_served

def get_new_ball(p1, p2,ball, screen_obj):
    ball.clear()
    screen_obj.tracer(0)
    if p1.scored:
        ball = Ball(initial_x=P1_BOARD_X, player_serve=True)
        p1.scored = False
    elif p2.scored:
        ball = Ball(initial_x=P2_BOARD_X, player_serve=False)
        p2.scored = False
    screen_obj.update()
    return ball



my_screen = get_screen()
my_screen.tracer(0)
draw_line()
player1 = Player(P1_BOARD_X, P1_PADDLE_X, P1_GOAL_X)
player2 = Player(P2_BOARD_X, P2_PADDLE_X, P2_GOAL_X)
my_ball = Ball(initial_x=P2_BOARD_X, player_serve=False)
my_screen.update()
play(player1, player2, my_ball, my_screen)
my_screen.exitonclick()

