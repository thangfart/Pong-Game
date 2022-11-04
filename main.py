from turtle import Screen,Turtle
#from Exercises.day22PongGame.class_Ball import Ball
from Exercises.day22PongGame.class_Paddle import Paddle
from Exercises.day22PongGame.class_Ball import Ball
from Exercises.day22PongGame.scoreboard import ScoreSheet
TIMESTEP =0.1
WIDTH = 800
HEIGHT = 600

import time


#Initialize main window
window = Screen()
window.setup(width=WIDTH,height=HEIGHT)
window.bgcolor("black")
window.title("Pong")
window.tracer(0)

#the ball
ball = Ball()

#paddles
right_paddle = Paddle((380,0))
left_paddle = Paddle((-390,0))

#scoreboard
sb = ScoreSheet()

#setup of key events, for both paddles, right paddel uses up/down key, left paddle uses w/s
window.listen()
window.onkeypress(right_paddle.move_up,"Up")
window.onkeypress(right_paddle.move_down,"Down")
window.onkeypress(left_paddle.move_up,"Right")
window.onkeypress(left_paddle.move_down,"Left")
# game loop
game_is_on = True
game_speed = 0.1
DT = 0.9

while game_is_on:
    window.update()
    ball.move()
    print(ball.xcor(),ball.ycor())
    time.sleep(game_speed)

    #check if there has been any bumps with a wall
    if ball.crashed_wall():
        #bounce action in y direction needed
        ball.bounce_y_back()
    # 360 for x right paddle works perfect, and -370 in x for left paddle perfect
    #check if theres been any hits with paddle
    if (ball.xcor() >= 360 and ball.distance(right_paddle) <= 50) or (ball.xcor() <= -370 and ball.distance(left_paddle) <= 50) :
        ball.bounce_x_back()
        game_speed *= DT
        #ball.speed()

    if ball.passed_left_paddle():
        ball.goto(0,0)
        game_speed = TIMESTEP
        ball.bounce_x_back()
        sb.incScoreRight_p()
    if ball.passed_right_paddle():
        ball.goto(0,0)
        game_speed = TIMESTEP
        ball.bounce_x_back()
        sb.incScoreLeft_p()
    print(f"hastighet på ball: {game_speed}")


#shut down main window
window.exitonclick()
