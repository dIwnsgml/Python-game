from turtle import Turtle, Screen
from random import random
import keyboard

MAGNIFICATION = 10
character_img = 0
character_dir = 1
def move_left():
    global character_img
    global character_dir
    
    char_shape = './Img/character/left/frame_' + str(character_img % 6) + '.gif'
    turtle.shape(char_shape)
    canvas.xview_scroll(-1, "units")
    turtle.setx(turtle.xcor() - MAGNIFICATION)
    character_img += 1
    character_dir = -1

def move_right():
    global character_img
    global character_dir
    
    char_shape = './Img/character/right/frame_' + str(character_img % 6) + '.gif'
    turtle.shape(char_shape)
    canvas.xview_scroll(1, "units")
    turtle.setx(turtle.xcor() + MAGNIFICATION)
    character_img += 1
    character_dir = -1

def move_up():
    canvas.yview_scroll(-1, "units")
    turtle.sety(turtle.ycor() + MAGNIFICATION)

def jump():
    global character_dir
    if keyboard.is_pressed('Left'):
        print("a")
        canvas.xview_scroll(-2, "units")
        turtle.sety(turtle.ycor() + 100)
        canvas.xview_scroll(-2, "units")
        turtle.setx(turtle.xcor() - 100)
        canvas.xview_scroll(-3, "units")
        turtle.sety(turtle.ycor() - 100)
        canvas.xview_scroll(-3, "units")
        character_dir = -1
    elif keyboard.is_pressed("Right"):
        print("b")
        canvas.xview_scroll(2, "units")
        turtle.sety(turtle.ycor() + 100)
        canvas.xview_scroll(2, "units")
        turtle.setx(turtle.xcor() + 100)
        canvas.xview_scroll(3, "units")
        turtle.sety(turtle.ycor() - 100)
        """ turtle.setheading(-90)
        turtle.speed(10)
        turtle.circle(50, -180)
        turtle.speed(1) """
        canvas.xview_scroll(3, "units")
        character_dir = 1
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

def shoot():
    shooting_animation = 0
    print("shoot")
    if(character_dir == 1):
      char_shape = './Img/character/shooting/right/frame_'
    else:
      char_shape = './Img/character/shooting/left/frame_'
    for i in range(3):
      char_shape += str(i) + '.gif'
      turtle.shape(char_shape)
    

screen = Screen()
width, height = screen.screensize()
screen.screensize(10000, 800)

canvas = screen.getcanvas()
canvas.config(xscrollincrement=str(MAGNIFICATION))
canvas.config(yscrollincrement=str(MAGNIFICATION))

# turtle initialization
screen.addshape("./Img/character/right/frame_0.gif")
screen.addshape("./Img/character/right/frame_1.gif")
screen.addshape("./Img/character/right/frame_2.gif")
screen.addshape("./Img/character/right/frame_3.gif")
screen.addshape("./Img/character/right/frame_4.gif")
screen.addshape("./Img/character/right/frame_5.gif")
screen.addshape("./Img/character/left/frame_0.gif")
screen.addshape("./Img/character/left/frame_1.gif")
screen.addshape("./Img/character/left/frame_2.gif")
screen.addshape("./Img/character/left/frame_3.gif")
screen.addshape("./Img/character/left/frame_4.gif")
screen.addshape("./Img/character/left/frame_5.gif")
screen.addshape("./Img/character/shooting/left/frame_0.gif")
screen.addshape("./Img/character/shooting/left/frame_1.gif")
screen.addshape("./Img/character/shooting/left/frame_2.gif")
screen.addshape("./Img/character/shooting/left/frame_3.gif")
screen.addshape("./Img/character/shooting/right/frame_0.gif")
screen.addshape("./Img/character/shooting/right/frame_1.gif")
screen.addshape("./Img/character/shooting/right/frame_2.gif")
screen.addshape("./Img/character/shooting/right/frame_3.gif")
turtle = Turtle("turtle", visible=False)
turtle.shape('./Img/character/right/frame_0.gif')
turtle.width(MAGNIFICATION)
turtle.resizemode('auto')
turtle.speed(3)
### Generate a landscape to explore

screen.tracer(False)

RULES = {'x':'x+yf+', 'y':'-fx-y', 'f':'f', '+':'+', '-':'-'}
sub_string = string = "fx"
LEVEL = 1

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
screen.onkeypress(shoot,"space")
screen.listen()

screen.mainloop()