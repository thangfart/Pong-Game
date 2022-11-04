from turtle import Turtle
import math
from Exercises.day22PongGame.class_Paddle import Paddle
START_X = 0
START_Y = 0
STEPSIZE = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        #self.shapesize()
        self.color("white")
        self.penup()
        #self.goto(360,0)
        self.x_projection = STEPSIZE
        self.y_projection = STEPSIZE
        #self.distance()

    #method for the projectile movement of the ball
    def move(self):
        new_x = self.xcor() + self.x_projection
        new_y = self.ycor() + self.y_projection
        self.goto(new_x,new_y)

    #check for collision with horizontal wall,meaning bounce back time!
    def crashed_wall(self):
        """
        Returns bool
        Ball has crashed to either upper or lower wall, when its y cord
        has either surpassed +- HEIGHT/2 value with margin of +-20 pixels.
        """
        if self.ycor() >= 280 or self.ycor() <= -280:
            print("crashed with wall")
            return True
        return False
    def bounce_y_back(self):
        #when hitting a wall projection in y direction must be reversed
        #if it was increasing in y, before the hit, the y projection must be neg. and vice versa
        #this can controlled creating two attributes, self.x_projection and self.y_projection
        self.y_projection *= -1

    def bounce_x_back(self):
        # same process as for y
        self.x_projection *= -1

    # detection of when ball miss a paddle
    def passed_right_paddle(self):
        if self.xcor() >= 380:
        #means it outside of the right-sided boundary
        #then it should start in the middle, projecting in the opposite direction
            return True
        return False

    def passed_left_paddle(self):
        if self.xcor() <= -390:
            return True
        return False


    #check for collision with paddle, meaning bounce back time!
    #the way we know it hit the paddle is if the balls x cord is close to paddles x cord and that
    # the distance (abs) of them are less than sqrt(50^2 + 20^2)
    #def paddle_collision(self,right_paddle:Paddle,left_paddle:Paddle):
        #if self.xcor() >= right_paddle.xcor() and self.distance(right_paddle) <= math.sqrt(50**2 + 20**2):
            #print("ball just hit the right paddle")
            #print(right_paddle.position())
            #return True
        #if self.xcor() <= left_paddle.xcor()and self.distance(left_paddle) <= math.sqrt(50**2 + 20**2):
            #print("ball just hit the left paddle")
            #print(left_paddle.position())
            #return True
        #else:
            #print("Ball is in free space")
            #return False






