from turtle import Turtle, Screen
from random import random
import keyboard

MAGNIFICATION = 10
character_img = 0

def move_left():
    canvas.xview_scroll(-1, "units")
    turtle.setx(turtle.xcor() - MAGNIFICATION)

def move_right():
    global character_img
    print( chr(character_img))
    print('./Img/character/frame_' + str(character_img) + '.gif')
    char_shape = './Img/character/frame_' + str(character_img) + '.gif'
    print(char_shape)
    turtle.shape(char_shape)
    canvas.xview_scroll(1, "units")
    turtle.setx(turtle.xcor() + MAGNIFICATION)
    character_img += 1

def move_up():
    canvas.yview_scroll(-1, "units")
    turtle.sety(turtle.ycor() + MAGNIFICATION)

def jump():
    if keyboard.is_pressed('Left'):
        print("a")
        canvas.xview_scroll(-2, "units")
        turtle.sety(turtle.ycor() + 100)
        canvas.xview_scroll(-2, "units")
        turtle.setx(turtle.xcor() - 100)
        canvas.xview_scroll(-3, "units")
        turtle.sety(turtle.ycor() - 100)
        canvas.xview_scroll(-3, "units")
    elif keyboard.is_pressed("Right"):
        print("b")
        canvas.xview_scroll(2, "units")
        turtle.sety(turtle.ycor() + 100)
        canvas.xview_scroll(2, "units")
        turtle.setx(turtle.xcor() + 100)
        canvas.xview_scroll(3, "units")
        turtle.sety(turtle.ycor() - 100)
        canvas.xview_scroll(3, "units")
    else:
        print("x")
        turtle.sety(turtle.ycor() + 100)
        turtle.sety(turtle.ycor() - 100)
        canvas.yview_scroll(0, "units")
    """ turtle.goto(turtle.xcor(), turtle.ycor() + 100)
    turtle.goto(turtle.xcor(), turtle.ycor() - 100) """
    """ turtle.sety(turtle.ycor() + 100)
    turtle.setx(turtle.xcor() + move_x)
    turtle.sety(turtle.ycor() - 100) """

def move_down():
    canvas.yview_scroll(1, "units")
    turtle.sety(turtle.ycor() - MAGNIFICATION)

screen = Screen()
width, height = screen.screensize()
screen.screensize(10000, 800)

canvas = screen.getcanvas()
canvas.config(xscrollincrement=str(MAGNIFICATION))
canvas.config(yscrollincrement=str(MAGNIFICATION))

# turtle initialization
screen.addshape("./Img/character/frame_0.gif")
screen.addshape("./Img/character/frame_1.gif")
screen.addshape("./Img/character/frame_2.gif")
screen.addshape("./Img/character/frame_3.gif")
screen.addshape("./Img/character/frame_4.gif")
screen.addshape("./Img/character/frame_5.gif")
turtle = Turtle("turtle", visible=False)
turtle.shape('./Img/character/frame_0.gif')
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
screen.onkeypress(jump, "Up")
screen.onkey(move_down, "Down")
screen.listen()

screen.mainloop()