from turtle import Turtle

class PADDLE(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=0.2, stretch_len=3.2)
        self.goto(x=0, y=-250) 
    def move_forward(self):
        self.forward(10)
    def move_back(self):
        self.backward(10)