import turtle
## Screen size
turtle.setup(width=500, height=400)

## Turtle window
window = turtle.Screen()
window.title("BreakoutBlast: Brick Buster Challenge")






## Game elements
paddle = turtle.Turtle()
ball = turtle.Turtle()
bricks = turtle.Turtle()



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


## element location
paddle.goto(x=0, y=-180)


window.mainloop()