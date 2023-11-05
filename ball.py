from turtle import Turtle
X_MOVE = 10
Y_MOVE = 10
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=0.8,stretch_len=0.8)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.sped = 0.1
    def bounce(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
    def bounce_ball(self):
        self.y_move *= -1
    def move(self):
        x = self.xcor() - self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
    def reset_position(self):
        self.goto(0, 0)
        self.sped = 0.1
        self.bounce_ball()
