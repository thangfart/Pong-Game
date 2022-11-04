from turtle import Turtle


class ScoreSheet(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.p_left_score = 0
        self.p_right_score = 0
        self.updateLeftScoresheet()
        self.updateRightScoresheet()

    def updateLeftScoresheet(self):
        self.goto(-300,245)
        self.write(self.p_left_score,align="center",font=("arial",50,"bold"))

    def updateRightScoresheet(self):
        self.goto(300,245)
        self.write(self.p_right_score,align="center",font=("arial",50,"bold"))

    def incScoreLeft_p(self):
        self.p_left_score += 1
        self.clear()
        self.updateRightScoresheet()
        self.updateLeftScoresheet()

    def incScoreRight_p(self):
        self.p_right_score += 1
        self.clear()
        self.updateLeftScoresheet()
        self.updateRightScoresheet()
