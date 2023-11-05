import turtle
import time
import random
from ball import Ball
import tkinter as tk
from tkinter import messagebox
import sys
from paddle import PADDLE
## Screen size
turtle.setup(width=800, height=600)


## Get random postion for bricks within 250 hundard in y axis
def get_random_postion():
    x = random.randint(-300,300)
    y = random.randint(0,220)
    return x,y


## Game elements
paddle = PADDLE()
ball = Ball()


## Turtle window
window = turtle.Screen()
window.title("BreakoutBlast: Brick Buster Challenge")
window.bgcolor('black')

## Keyboard interaction



## User interaction using keyboard
window.onkey(paddle.move_forward, 'd')
window.onkey(paddle.move_back, 'a')


## Listen for keystrokes
window.listen()










## Paddle Structure




## Ball Structure




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

IS_GAME_ON = True
SCORE = 0

## Show popup window
def score_popup():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Popup Window", f"Your Score : {SCORE}")
    root.destroy()

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
        IS_GAME_ON = False
        score_popup()
        sys.exit()

    
    ## Detecting collison with bricks
    for turtle in turtles:
        if ball.distance(turtle) < 30:
            SCORE += 1
            turtle.hideturtle()






    









window.mainloop()

