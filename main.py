import turtle

turtle.setup(width=500, height=400)

window = turtle.Screen()
window.title("BreakoutBlast: Brick Buster Challenge")



paddle = turtle.Turtle()
ball = turtle.Turtle()
bricks = turtle.Turtle()

paddle.goto(x=0, y=-180)


window.mainloop()