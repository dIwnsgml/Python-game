import turtle as trtl
from random import random
import keyboard
import sys
import time
""" sys.setrecursionlimit(100000) """
sys.setrecursionlimit(100)
from border import create_border
from gravity import create_gravity

MAGNIFICATION = 10
character_img = 0
character_dir = 1

screen = trtl.Screen()
width, height = screen.screensize()
screen.screensize(10000, 800)

canvas = screen.getcanvas()
canvas.config(xscrollincrement=str(MAGNIFICATION))
canvas.config(yscrollincrement=str(MAGNIFICATION))

# character initialization
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

character = trtl.Turtle()
character.shape('./Img/character/right/frame_0.gif')
character.width(MAGNIFICATION)
character.resizemode('auto')
character.speed(3)

character.penup()

border = create_border()
delay = False
def move_left():
    """ this line avoid event stacking """
    screen.onkeypress(None, 'Left')
    global character_img
    global character_dir
    character.shape('./Img/character/left/frame_' + str(character_img % 6) + '.gif')
    canvas.xview_scroll(-1, "units")
    character.forward(-10)
    character_img += 1
    character_dir = -1
    create_gravity(border, character)
    screen.onkeypress(move_left, 'Left')
    
    return 0


def move_right():
    """ this line avoid event stacking """
    screen.onkeypress(None, 'Right')
    global character_img
    global character_dir
    character.shape('./Img/character/right/frame_' + str(character_img % 6) + '.gif')
    canvas.xview_scroll(1, "units")
    character.forward(10)
    character_img += 1
    character_dir = 1
    create_gravity(border, character)
    screen.onkeypress(move_right, 'Right')
    
    return 0


def jump():
    screen.onkeypress(None, 'Up')
    global character_dir
    if keyboard.is_pressed('Left'):
        print("a")
        canvas.xview_scroll(-2, "units")
        character.sety(character.ycor() + 100)
        canvas.xview_scroll(-2, "units")
        character.setx(character.xcor() - 100)
        canvas.xview_scroll(-3, "units")
        character.sety(character.ycor() - 100)
        canvas.xview_scroll(-3, "units")
        character_dir = -1
    elif keyboard.is_pressed("Right"):
        print("b")
        canvas.xview_scroll(2, "units")
        character.sety(character.ycor() + 100)
        canvas.xview_scroll(2, "units")
        character.setx(character.xcor() + 100)
        canvas.xview_scroll(3, "units")
        character.sety(character.ycor() - 100)
        """ character.setheading(-90)
        character.speed(10)
        character.circle(50, -180)
        character.speed(1) """
        canvas.xview_scroll(3, "units")
        character_dir = 1
        
    else:
        print("x")
        character.sety(character.ycor() + 100)
        character.sety(character.ycor() - 100)
        canvas.yview_scroll(0, "units")
    create_gravity(border, character)
    screen.onkeypress(jump, 'Up')

def shoot():
    """ this line avoid event stacking """
    screen.onkeypress(None, 'space')
    for i in range(3):
      if(character_dir == 1):
        character.shape('./Img/character/shooting/right/frame_'+str(i) + '.gif')
      else:
        character.shape('./Img/character/shooting/left/frame_'+str(i) + '.gif')
    time.sleep(0.1)
    screen.onkeypress(shoot, 'space')


screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(jump, "Up")
screen.onkeypress(shoot,"space")
screen.listen()

screen.mainloop()