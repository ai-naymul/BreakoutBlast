import turtle
import time
import random

## Screen size
turtle.setup(width=800, height=600)


## Get random postion for bricks within 250 hundard in y axis
def get_random_postion():
    x = random.randint(0,300)
    y = random.randint(0,250)
    return x,y





## Turtle window
window = turtle.Screen()
window.title("BreakoutBlast: Brick Buster Challenge")
window.bgcolor('black')

## Keyboard interaction
def move_forward():
    paddle.forward(10)
def move_back():
    paddle.backward(10)


## User interaction using keyboard
window.onkey(move_forward, 'd')
window.onkey(move_back, 'a')


## Listen for keystrokes
window.listen()



## Game elements
paddle = turtle.Turtle()
ball = turtle.Turtle()






## Paddle Structure
paddle.color('white')
paddle.penup()
paddle.shape('square')
paddle.shapesize(stretch_wid=0.2, stretch_len=3.2)
paddle.goto(x=0, y=-250)



## Ball Structure
ball.color('white')
ball.shape('circle')
ball.shapesize(stretch_len=0.9)
for i in range(50):
    time.sleep(0.1)
    def move_ball():
        y = ball.ycor() + -10
        x = ball.xcor()
        ball.goto(x,y)

    move_ball()


## Brick Structure
num_turtle = 20
turtles = []
for _ in range(num_turtle):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.shape('square')
    new_turtle.shapesize(stretch_wid=0.4,stretch_len=1)
    new_turtle.color('white')
    new_turtle.goto(get_random_postion())
    turtles.append(new_turtle)






window.mainloop()