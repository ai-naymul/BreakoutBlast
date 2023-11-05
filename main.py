import turtle
import time
import random
from ball import Ball
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
ball = Ball()






## Paddle Structure
paddle.color('white')
paddle.penup()
paddle.shape('square')
paddle.shapesize(stretch_wid=0.2, stretch_len=3.2)
paddle.goto(x=0, y=-250)



## Ball Structure




## Brick Structure
num_turtle = 20
# turtles = []
# for _ in range(num_turtle):
#     new_turtle = turtle.Turtle()
#     new_turtle.penup()
#     new_turtle.shape('square')
#     new_turtle.shapesize(stretch_wid=0.4,stretch_len=1)
#     new_turtle.color('white')
#     new_turtle.goto(get_random_postion())
#     turtles.append(new_turtle)


IS_GAME_ON = True

## Collison Detection 
## Detect collison with paddle
while IS_GAME_ON:
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280:
        ball.bounce()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    if ball.distance(paddle) < 50:
        ball.bounce_ball()
    if ball.ycor() < -300:
        print('Game Over')





    









window.mainloop()

