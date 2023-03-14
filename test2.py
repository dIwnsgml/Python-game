from turtle import Turtle, Screen
from random import random
import sys

sys.setrecursionlimit(30)
MAGNIFICATION = 10

def move_left():
    canvas.xview_scroll(-1, "units")
    turtle.setx(turtle.xcor() - MAGNIFICATION)

def move_right():
    canvas.xview_scroll(1, "units")
    turtle.setx(turtle.xcor() + MAGNIFICATION)

def move_up():
    canvas.yview_scroll(-1, "units")
    turtle.sety(turtle.ycor() + MAGNIFICATION)

def move_down():
    canvas.yview_scroll(1, "units")
    turtle.sety(turtle.ycor() - MAGNIFICATION)

screen = Screen()
width, height = screen.screensize()
screen.screensize(width * MAGNIFICATION, height * MAGNIFICATION)

canvas = screen.getcanvas()
canvas.config(xscrollincrement=str(MAGNIFICATION))
canvas.config(yscrollincrement=str(MAGNIFICATION))

# turtle initialization
turtle = Turtle("turtle", visible=False)
turtle.width(MAGNIFICATION)
turtle.resizemode('auto')

### Generate a landscape to explore

screen.tracer(False)

RULES = {'x':'x+yf+', 'y':'-fx-y', 'f':'f', '+':'+', '-':'-'}
sub_string = string = "fx"
LEVEL = 13

for _ in range(LEVEL):

    turtle.pencolor(random(), random(), random())

    for character in sub_string:
        if character == '+':
            turtle.right(90)
        elif character == '-':
            turtle.left(90)
        elif character == 'f':
            turtle.forward(5 * MAGNIFICATION)

    screen.update()

    full_string = "".join(RULES[character] for character in string)
    sub_string = full_string[len(string):]
    string = full_string

screen.tracer(True)

### Finished generating a landscape to explore

turtle.penup()
turtle.home()
turtle.setheading(90)
turtle.color('dark green', 'light green')
turtle.showturtle()

screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.listen()

screen.mainloop()