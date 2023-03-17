import turtle as trtl
import random
import keyboard
import sys
import time
import threading
import os
import glob

""" sys.setrecursionlimit(100000) """
sys.setrecursionlimit(100)
sys.setswitchinterval(0.001)
from border import create_border
from gravity import create_gravity


MAGNIFICATION = 10
width = 10000
height = 800

screen = trtl.Screen()
screen.screensize(width, height)

trtl.delay(0)
canvas = screen.getcanvas()
canvas.config(xscrollincrement=str(MAGNIFICATION))
canvas.config(yscrollincrement=str(MAGNIFICATION))
""" canvas.place(relx=0, rely=0, width=screen.window_width(), height = screen.window_height()) """

dir = './img'
depth = 0
def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths("./img")
for i in range (len(full_file_paths)):
  screen.addshape(full_file_paths[i].replace('\\', '/'))
""" print(os.scandir("./img"))
print(os.scandir("./img"))
i = 0
while(len(os.listdir(dir)) != 0):
    print(os.listdir(dir))
    if(os.listdir(dir)[0].find('gif') < 0 and len(os.listdir(dir)) > i):
        print(os.listdir(dir)[0].find('gif'))
        dir += '/'+ os.listdir(dir)[i]
    else:
        dir = dir.split(dir.split('/')[len(dir.split('/')) - 1])[0]
        print(dir)
        i += 1
    print(dir)
    time.sleep(1)
    depth += 1 """

character = trtl.Turtle()
character.shape('./img/character/run/right/frame_0.gif')
character.width(MAGNIFICATION)
character.resizemode('auto')
character.speed(0)
character.penup()
character.goto(-1 * width / 2 + 100, 0)
canvas.xview_scroll(-100000, "units")
border = create_border()
delay = False

""" tanks = trtl.Turtle()
tanks.shape('./img/tank/moving/left/frame_0.gif')
tanks.width(MAGNIFICATION)
tanks.resizemode('auto')
tanks.speed(3)
tanks.penup() """
character_img = 0
character_dir = 1
character_animation = 0
def move_left():
    """ this line avoid event stacking """
    screen.onkeypress(None, 'Left')
    global character_img
    global character_dir
    global character_animation
    character_animation = 1
    character.shape('./img/character/run/left/frame_' + str(character_img % 6) + '.gif')
    canvas.xview_scroll(-1, "units")
    character.forward(-10)
    character_img += 1
    character_dir = -1
    create_gravity(border, character)
    screen.onkeypress(move_left, 'Left')
    character_animation = 0
    """ standing() """


def move_right():
    """ this line avoid event stacking """
    screen.onkeypress(None, 'Right')
    global character_img
    global character_dir
    global character_animation
    character_animation = 1
    character.shape('./img/character/run/right/frame_' + str(character_img % 6) + '.gif')
    canvas.xview_scroll(1, "units")
    character.forward(10)
    character_img += 1
    character_dir = 1
    create_gravity(border, character)
    screen.onkeypress(move_right, 'Right')
    character_animation = 0
    """ standing() """


def jump():
    screen.onkeypress(None, 'Up')
    global character_dir
    global character_animation
    character_animation = 1
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
    trtl.delay(0)
    screen.onkeypress(jump, 'Up')
    character_animation = 0
    """ standing() """

def create_bullet():
  bullet = trtl.Turtle()
  bullet.shape('./img/character/fire/right/bullet.gif')
  bullet.penup()
  bullet.goto(character.xcor() + 20, character.ycor() + 15)
  while(character.xcor() + screen.window_width() > bullet.xcor()):
      bullet.forward(30)
      time.sleep(0.0001)

def shoot():
    print(canvas.xview()[1], screen.window_width(), character.xcor())
    """ this line avoid event stacking """
    global character_animation
    global tanks_info
    tanks_info[0][2] = "fire1"
    character_animation = 1
    screen.onkeypress(None, 'space')

    if(character_dir == 1):
        for i in range(3):     
          character.shape('./img/character/fire/right/frame_'+str(i) + '.gif')
          time.sleep(0.1)
        #bullet stops when hit the wall
        t[2] = threading.Thread(target=create_bullet, args=())
        t[2].start()
        """ while(character.xcor() + screen.window_width() > bullet.xcor()):
            bullet.forward(30)
            time.sleep(0.00001) """
        """ for i in range(50):
            bullet.forward(20)
            time.sleep(0.0001) """
    else: 
        for i in range(3):   
          character.shape('./img/character/fire/left/frame_'+str(i) + '.gif')
          time.sleep(0.05)
        bullet = trtl.Turtle()
        bullet.penup()
        bullet.goto(character.xcor() - 20, character.ycor() + 15)
        bullet.shape('./img/character/fire/left/bullet.gif')
        for i in range(50):
            bullet.forward(-20)
            time.sleep(0.0001)

    """ for i in range(3):
      if(character_dir == 1):
        character.shape('./img/character/fire/right/frame_'+str(i) + '.gif')
      else:
        character.shape('./img/character/fire/left/frame_'+str(i) + '.gif')
      time.sleep(0.05) """
    time.sleep(0.1)
    character_animation = 0
    screen.onkeypress(shoot, 'space')

def standing():
  global character_animation
  """ while (not (keyboard.is_pressed("Right") and keyboard.is_pressed("Left") and keyboard.is_pressed("Up") and keyboard.is_pressed("Space"))): """
  i = 0
  """ while True:
    if(character_animation == 1 or keyboard.is_pressed("Right") or keyboard.is_pressed("Left") or keyboard.is_pressed("Up") or keyboard.is_pressed("Space")):
       break
    if(character_dir == 1):
      character.shape('./img/character/standing/right/frame_'+str(i % 6) + '.gif')
    else:
      character.shape('./img/character/standing/left/frame_'+str(i % 6) + '.gif')
    time.sleep(0.2)
    i += 1 """
  print('test')
  if(character_dir == 1):
      character.shape('./img/character/standing/right/frame_'+str(0) + '.gif')
  else:
      character.shape('./img/character/standing/left/frame_'+str(0) + '.gif')

tanks_info = []
tanks_n = 0
def create_tank(x, y):
    global tanks_n
    global tanks_info
    tanks_n += 1
    tank = trtl.Turtle()
    tank.shape('./img/tank/moving/left/frame_0.gif')
    tanks_info.append([180, 1, "move"])
    tank.resizemode('auto')
    tank.penup()
    i = 0
    tank_type = random.randrange(0, 1)

    while(True):
        print(tanks_info[0][2])
        if(tanks_info[tanks_n - 1][2] == "move" and character.xcor() + screen.window_width() < tank.xcor()):
            tank.shape('./img/tank/moving/left/frame_'+str(i % 6) + '.gif')
            tank.forward(1)
            tank.setheading(tanks_info[tanks_n - 1][0])
            time.sleep(0.001)
            print(x, character.xcor(), tank.xcor())
        else:
            tank.shape('./img/tank/fire1/left/frame_'+str(i % 17) + '.gif')
            time.sleep(0.1)
        i+=1


t = [0, 0, 0]
print(int(character.xcor()))
t[1] = threading.Thread(target=create_tank, args=(0, 0))
t[1].start()



""" standing() """

screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(jump, "Up")
screen.onkeypress(shoot,"space")

""" when release any keys, change the state to standing """
screen.onkeyrelease(standing, "Left")
screen.onkeyrelease(standing, "Right")
screen.onkeyrelease(standing,"space")
screen.listen()

screen.mainloop()