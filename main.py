import turtle as trtl
import random
import keyboard
import sys
import time
import threading
import os


wn = trtl.Screen()

""" portal() """


""" sys.setrecursionlimit(100000) """
#screen setting
sys.setrecursionlimit(100)
sys.setswitchinterval(0.001)
from border import create_border
from gravity import create_gravity


MAGNIFICATION = 1
width = 20000
height = 10000

screen = trtl.Screen()
screen.screensize(width, height)
""" screen.bgcolor("orange") """

trtl.delay(0)
canvas = screen.getcanvas()
canvas.config(xscrollincrement=str(MAGNIFICATION))
canvas.config(yscrollincrement=str(MAGNIFICATION))
trtl.setup(width=1.0, height=1.0)
""" canvas.place(relx=0, rely=0, width=screen.window_width(), height = screen.window_height()) """

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

full_file_paths = get_filepaths("./img")

#add all files in img folder
for i in range (len(full_file_paths)):
  screen.addshape(full_file_paths[i].replace('\\', '/'))

screen.bgpic("./img/background/black.gif")
trtl.pencolor("black")
trtl.speed(0)
color = ["purple", "blue", "black"]


#portal function
def portal(size, x, y):
#portal gif
  global t2
  t2 = trtl.Turtle()
  t2.shape("./img/background/portal.gif")
  t2.shapesize(size)
  t2.pu()
  t2.goto(x, y)


portal(100, width / 2 - 200, 50)
#main character setting
character = trtl.Turtle()
character.shape('./img/character/run/right/frame_0.gif')
""" character.width(MAGNIFICATION) """
character.resizemode('auto')
character.speed(0)
character.penup()
character.goto(-1 * width / 2 + 300, 45)
character.hp = 20
canvas.yview_scroll(-10 * int(canvas.winfo_height() / 20) + 40, "units")
print(-1 * int(canvas.winfo_height() / 2))
canvas.xview_scroll(-100000, "units")
border = create_border()
delay = False

""" test = trtl.Turtle()
test.goto(-1 * width / 2 + 300, 45)
 """



wall = trtl.Turtle()
wall_info = []

def horizontal_rect():
  wall.pendown()
  wall.setheading(0)
  wall.fillcolor(random.choice(color))
  wall.begin_fill()
  wall.forward(70)
  wall.right(90)
  wall.forward(20)
  wall.right(90)
  wall.forward(70)
  wall.right(90)
  wall.forward(20)
  wall.end_fill()
  wall.right(90)
  wall.penup()
  wall.forward(70)
  wall.penup()

def vertical_rect():
  wall.pendown()
  wall.setheading(90)
  wall.fillcolor(random.choice(color))
  wall.begin_fill()
  wall.forward(70)
  wall.right(90)
  wall.forward(20)
  wall.right(90)
  wall.forward(70)
  wall.right(90)
  wall.forward(20)
  wall.end_fill()
  wall.right(90)
  wall.penup()
  wall.forward(70)
  wall.penup()

  
def draw_floor():
  wall.penup()
  wall.goto(width / 2 * -1, int(character.ycor() - 45))
  wall.pendown()
  while(wall.xcor() < width / 2):
      horizontal_rect()

def draw_wall():
  wall.penup()
  wall.goto(width / 2 * -1,int(character.ycor() - 45))
  wall.pendown()
  for i in range(10):
      vertical_rect()

def add_platforms():
  global wall_n
  wall.penup()
  wall.goto(15, -45)
  wall.pendown()
  wall.right(90)
  horizontal_rect()
  horizontal_rect()
  wall.penup()
  wall.goto(155, 30)
  wall.pendown()
  horizontal_rect()
  horizontal_rect()
  wall.goto(-1 * width / 2, 100)
  wall_n = 0
  while(wall.xcor() < width / 2):
      wall.forward(100)
      block_length = random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3])
      if(block_length > 0):
          wall_info.append([wall.ycor(), wall.xcor()])
          while(block_length > 0):
              horizontal_rect()
              block_length -= 1
          wall_info[wall_n].append(wall.xcor())
          wall_n += 1
          


draw_floor()
draw_wall()
add_platforms()


character_img = 0
character_dir = 1
character_animation = 0
def move_left():
    global collide
    collide = False
    """ this line avoid event stacking """
    screen.onkeypress(None, 'Left')
    global character_img
    global character_dir
    global character_animation
    character_animation = 1
    character.shape('./img/character/run/left/frame_' + str(character_img % 6) + '.gif')
    canvas.xview_scroll(-20, "units")
    character.forward(-20)
    character_img += 1
    character_dir = -1
    """ create_gravity(border, character) """
    screen.onkeypress(move_left, 'Left')
    character_animation = 0
    for i in range(wall_n):
        if(abs(character.xcor() - (wall_info[i][1] + wall_info[i][2]) / 2) <= abs(wall_info[i][1] - wall_info[i][2]) / 2 + 30):
            collide = True
            break
    if(collide == False):
        create_gravity(border, character)
        """ create_gravity(border, character) """
        collide = True
    #remove elements as player moves
    if(tanks_n > 0):
        if(abs(tank.xcor() - character.xcor()) > canvas.winfo_width()):   
            tank.reset()
            tank.clear()
        


def move_right():
    global collide
    collide = False
    """ this line avoid event stacking """
    screen.onkeypress(None, 'Right')
    global character_img
    global character_dir
    global character_animation
    character_animation = 1
    character.shape('./img/character/run/right/frame_' + str(character_img % 6) + '.gif')
    canvas.xview_scroll(20, "units")
    character.forward(20)
    character_img += 1
    character_dir = 1
    """ create_gravity(border, character) """
    screen.onkeypress(move_right, 'Right')
    character_animation = 0
    for i in range(wall_n):
        if(abs(character.xcor() - (wall_info[i][1] + wall_info[i][2]) / 2) <= abs(wall_info[i][1] - wall_info[i][2]) / 2 + 30):
            collide = True
            break
    if(collide == False):
        create_gravity(border, character)
        """ create_gravity(border, character) """
        collide = True
    
    """ standing() """
    """ if (abs(character - t2 < 5)):
      trtl.pu()
      trtl.goto(0,0)
      trtl. """
        #remove elements as player moves
    if(tanks_n > 0):
        if(character.xcor() - tank.xcor() > 600):   
            tank.reset()
            tank.hp = 0
    else:
        t[0] = threading.Thread(target=create_tank, args=(character.xcor() + canvas.winfo_width(), 0))
        t[0].start()
        
        


def jump():
    """ print(wall_info) """
    collide = False
    screen.onkeypress(None, 'Up')
    global character_dir
    global character_animation
    character_animation = 1
    jump_angle = 90
    if keyboard.is_pressed('Left') or character_dir == -1:
        character.setheading(90)
        while(character.ycor() > border.ycor() + 40 and collide == False):
            for i in range(wall_n):
                if(abs(character.xcor() - (wall_info[i][1] + wall_info[i][2]) / 2) < abs(wall_info[i][1] - wall_info[i][2]) / 2 + 10 and abs(character.ycor() - wall_info[i][0]) <= 20):
                    collide = True
                    print("collide")
                    break
            if(collide == False):
                character.forward(14)
                """ character.right(jump_angle) """
                character.setheading(jump_angle)
                time.sleep(0.0000001)
                canvas.xview_scroll(-8, "units")
                if(jump_angle < 250):
                    jump_angle += 8

        if(character.ycor() > wall_info[i][0]): 
            character.sety(wall_info[i][0] + 40)
        else:
            create_gravity(border, character)
        character_dir = -1
    else:
        character.setheading(90)
        while(character.ycor() > border.ycor() + 40 and collide == False):
            for i in range(wall_n):
                if(abs(character.xcor() - (wall_info[i][1] + wall_info[i][2]) / 2) < abs(wall_info[i][1] - wall_info[i][2]) / 2 + 10 and abs(character.ycor() - wall_info[i][0]) <= 20):
                    collide = True
                    print("collide")
                    break
            if(collide == False):
                character.forward(14)
                """ character.right(jump_angle) """
                character.setheading(jump_angle)
                time.sleep(0.0000001)
                canvas.xview_scroll(8, "units")
                if(jump_angle > -70):
                    jump_angle -= 8

        if(character.ycor() > wall_info[i][0]): 
            character.sety(wall_info[i][0] + 40)
        else:
            create_gravity(border, character)
        character_dir = 1
        
    """ else:
        print("x")
        while(character.ycor() < 160):
          character.sety(character.ycor() + 0.2)
        while(character.ycor() > 45):
          character.sety(character.ycor() - 0.2)
        canvas.yview_scroll(0, "units") """
    
    """ create_gravity(border, character) """
    character.setheading(0)
    screen.onkeypress(jump, 'Up')
    character_animation = 0
    """ standing() """

def create_bullet():
  bullet = trtl.Turtle()
  bullet.shape('./img/character/fire/right/bullet.gif')
  bullet.penup()
  bullet.goto(character.xcor() + 20, character.ycor() + 15)
  while(character.xcor() + screen.window_width() > bullet.xcor() and not(abs(bullet.xcor() - tank.xcor()) < 20 and abs(bullet.ycor() - tank.ycor()) < 10)):
      bullet.forward(1)
      if(abs(bullet.xcor() - tank.xcor()) < 30 and abs(bullet.ycor() - tank.ycor() + 40) < 10):
          tank.hp -= 10
          bullet.clear()
          bullet.reset()
          if(tank.hp <= 0):
              break
  bullet.clear()
  bullet.reset()

def shoot():
    print(canvas.xview()[1], screen.window_width(), character.xcor())
    """ this line avoid event stacking """
    global character_animation
    """ global tanks_info
    tanks_info[0][2] = "fire1" """
    character_animation = 1
    screen.onkeypress(None, 'space')

    if(character_dir == 1):
        for i in range(3):     
          character.shape('./img/character/fire/right/frame_'+str(i) + '.gif')
          time.sleep(0.003)
        #bullet stops when hit the wall
        t[1] = threading.Thread(target=create_bullet, args=())
        t[1].start()
    else: 
        for i in range(3):   
          character.shape('./img/character/fire/left/frame_'+str(i) + '.gif')
          time.sleep(0.003)

    time.sleep(0.1)
    standing()
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
def tank_missile(x, y):
    missile = trtl.Turtle()
    missile.penup()
    missile.goto(x, y)
    missile.shape('./img/tank/fire1/missile1.gif')
    missile.setheading(90)
    while(missile.ycor() > 20):
        missile.forward(30)
        missile.left(5)
        """ 
                 missile.forward(2)
        missile.left(0.2)
           """
        if(missile.heading() > 180):
            missile.shape('./img/tank/fire1/missile2.gif')
        time.sleep(0.001)
    for i in range(10):
        missile.shape('./img/tank/fire1/explode/frame_'+str(i % 10) + '.gif')
        time.sleep(0.01)
    if(missile.xcor() - 100 < character.xcor() < missile.xcor() + 100):
        print("hit missile")
        character.hp -= 10
        if(character.hp <= 0):
            character.shape("./img/character/dead/ghost.gif")
            screen.onkeypress(None, "Left")
            screen.onkeypress(None, "Right")
            screen.onkeypress(None, "Up")
            screen.onkeypress(None,"space")
            screen.onkeyrelease(None, "Right")
            screen.onkeyrelease(None, "Left")
    missile.clear()
    missile.reset()

def tank_bullet(x, y):
  tank_bullet = trtl.Turtle()
  tank_bullet.penup()
  tank_bullet.goto(x, y - 30)
  tank_bullet.shape('./img/tank/fire1/bullet.gif')
  tank_bullet.setheading(180)
  """ while(x - screen.window_width() < tank_bullet.xcor() and (character.xcor() < tank_bullet.xcor() and character.ycor() -45 > tank_bullet.ycor())):  """
  print(character.ycor() - 45, tank_bullet.ycor())
  while(True):
      if(abs(character.xcor() - tank_bullet.xcor()) < 30 and abs(character.ycor() - tank_bullet.ycor() + 20) < 30):
          print("hit", tank_bullet.ycor(), character.ycor())
          character.hp -= 5
          tank_bullet.clear()
          tank_bullet.reset()
          if(character.hp <= 0):
            character.shape("./img/character/dead/ghost.gif")
            screen.onkeypress(None, "Left")
            screen.onkeypress(None, "Right")
            screen.onkeypress(None, "Up")
            screen.onkeypress(None,"space")
            screen.onkeyrelease(None, "Right")
            screen.onkeyrelease(None, "Left")

          break
      tank_bullet.forward(15)
      time.sleep(0.007)

def create_tank(x, y):
    global tanks_n
    global tanks_info
    global tank
    tanks_n += 1
    tank = trtl.Turtle()
    tank.penup()
    tank.goto(x, y + 100)
    print("tank cor: ",tank.xcor(), tank.ycor())
    tank.hp = 30
    tank.shape('./img/tank/moving/left/frame_0_delay-0.1s.gif')
    tanks_info.append([180, 1, "move"])
    tank.resizemode('auto')
    i = 0
    while(True):
        if(character.xcor() + screen.window_width() - 300 < tank.xcor() and tank.hp > 0):
            tank.shape('./img/tank/moving/left/frame_'+str(i % 6) + '_delay-0.1s.gif')
            tank.forward(10)
            tank.setheading(tanks_info[tanks_n - 1][0])
            time.sleep(0.001)
            """ print(x, character.xcor(), tank.xcor()) """
        elif(character.xcor() + screen.window_width() > tank.xcor() and tank.hp > 0):
            tank.shape('./img/tank/fire1/left/frame_'+str(i % 17) + '_delay-0.1s.gif')
            time.sleep(0.12)
            if(i % 17 == 3):
                t[2] = threading.Thread(target=tank_bullet, args=(tank.xcor(), tank.ycor()))
                t[2].start()
                time.sleep(0.5)
            elif(i % 17 == 10):
                t[2] = threading.Thread(target=tank_missile, args=(tank.xcor(), tank.ycor()))
                t[2].start()
                time.sleep(0.5)
        elif(tank.hp <= 0):
            tank.sety(tank.ycor() + 50)
            for j in range(43):
                tank.shape('./img/tank/destroyed/left/frame_'+str(j) + '_delay-0.1s.gif')
                time.sleep(0.03)
            tank.clear()
            tank.reset()
            tanks_n -= 1
            return 0
        i+=1


"""  """


helicopters_info = []
helicopters_n = 0
def helicopters_missile(x, y):
    missile = trtl.Turtle()
    missile.penup()
    missile.goto(x, y)
    missile.shape('./img/tank/fire1/missile1.gif')
    missile.setheading(270)
    collide = False
    while(missile.ycor() >= 0 and collide == False):
        for i in range(wall_n):
          if(abs(missile.xcor() - (wall_info[i][1] + wall_info[i][2]) / 2) < abs(wall_info[i][1] - wall_info[i][2]) / 2 + 10 and abs(missile.ycor() - wall_info[i][0]) <= 70):
              collide = True
              print("collide")
              break
        if(collide == False):
            missile.forward(30)
        time.sleep(0.001)
    for i in range(10):
        missile.shape('./img/tank/fire1/explode/frame_'+str(i % 10) + '.gif')
        time.sleep(0.01)
    if(abs(missile.xcor() - character.xcor()) < 50 and abs(missile.ycor() - character.ycor()) < 80):
        print("hit missile")
        character.hp -= 10
        if(character.hp <= 0):
            character.shape("./img/character/dead/ghost.gif")
            screen.onkeypress(None, "Left")
            screen.onkeypress(None, "Right")
            screen.onkeypress(None, "Up")
            screen.onkeypress(None,"space")
            screen.onkeyrelease(None, "Right")
            screen.onkeyrelease(None, "Left")
    missile.clear()
    missile.reset()


helicopter_ = "destroy"
def create_helicopter(x, y):
    global helicopters_n
    global helicopters_info
    global helicopter
    helicopters_n += 1
    helicopter = trtl.Turtle()
    helicopter_pen = trtl.Turtle()
    helicopter.hp = 30
    helicopter.penup()
    helicopter.goto(x, y + 60)
    helicopter.shape('./img/helicopter/moving/left/frame_0_delay-0.1s.gif')
    helicopters_info.append([180, 1, "move"])
    helicopter.resizemode('auto')
    i = 0
    screen.onkeypress(typedD, "d")
    screen.onkeypress(typedE, "e")
    screen.onkeypress(typedS, "s")
    screen.onkeypress(typedT, "t")
    screen.onkeypress(typedR, "r")
    screen.onkeypress(typedO, "o")
    screen.onkeypress(typedY, "y")


    while(True):
        if(abs(character.xcor() - helicopter.xcor()) > 50 and helicopter.hp > 0):
            if((character.xcor() - helicopter.xcor()) >= 0):
                helicopter.shape('./img/helicopter/moving/right/frame_'+str(i % 12) + '_delay-0.1s.gif')
                helicopter.forward(-20)
            else:
                helicopter.shape('./img/helicopter/moving/left/frame_'+str(i % 12) + '_delay-0.1s.gif')
                helicopter.forward(20)
            helicopter.setheading(helicopters_info[helicopters_n - 1][0])
            time.sleep(0.001)
            """ print(x, character.xcor(), tank.xcor()) """
        elif(character.xcor() + screen.window_width() > helicopter.xcor() and helicopter.hp > 0):
            if((character.xcor() - helicopter.xcor()) >= 0):
                helicopter.shape('./img/helicopter/fire/right/frame_'+str(i % 6) + '_delay-0.1s.gif')
            else:
                helicopter.shape('./img/helicopter/fire/left/frame_'+str(i % 6) + '_delay-0.1s.gif')
            time.sleep(0.2)
            if(i % 6 == 3):
                t[2] = threading.Thread(target=helicopters_missile, args=(helicopter.xcor(), helicopter.ycor()))
                t[2].start()
        elif(helicopter.hp <= 0):
            for j in range(11):
                helicopter.shape('./img/helicopter/destroyed/frame_'+str(j) + '_delay-0.1s.gif')
                time.sleep(0.05)
            helicopter.clear()
            helicopter.reset()
            break
        helicopter_pen.clear()
        helicopter_pen.goto(helicopter.xcor() + 100, helicopter.ycor())
        helicopter_pen.write(helicopter_, font=("Arial", 11, "bold"))
        i+=1
    screen.onkeypress(None, "d")
    screen.onkeypress(None, "e")
    screen.onkeypress(None, "s")
    screen.onkeypress(None, "t")
    screen.onkeypress(None, "r")
    screen.onkeypress(None, "o")
    screen.onkeypress(None, "y")
t = [0, 0, 0, 0]
print(int(character.xcor()))
""" t[0] = threading.Thread(target=create_tank, args=(-2000, 0))
t[0].start() """

t[3] = threading.Thread(target=create_helicopter, args=(character.xcor() + screen.window_width()+100, screen.window_height() - 230))
t[3].start()


screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(jump, "Up")
screen.onkeypress(shoot,"space")

""" when release any keys, change the state to standing """
screen.onkeyrelease(standing, "Right")
screen.onkeyrelease(standing, "Left")


def typedD():
    global helicopter_

    helicopter_ = helicopter_.replace("d", "") 
    print(helicopter_)
    if(len(helicopter_) == 0):
       helicopter.hp = 0

def typedE():
    global helicopter_

    helicopter_ = helicopter_.replace("e", "")   
    if(len(helicopter_) == 0):
       helicopter.hp = 0

def typedS():
    global helicopter_

    helicopter_ = helicopter_.replace("s", "")   
    if(len(helicopter_) == 0):
       helicopter.hp = 0

def typedT():
    global helicopter_

    helicopter_ = helicopter_.replace("t", "")   
    if(len(helicopter_) == 0):
       helicopter.hp = 0

def typedR():
    global helicopter_

    helicopter_ = helicopter_.replace("r", "")   
    if(len(helicopter_) == 0):
       helicopter.hp = 0

def typedO():
    global helicopter_

    helicopter_ = helicopter_.replace("o", "")   
    if(len(helicopter_) == 0):
       helicopter.hp = 0

def typedY():
    global helicopter_

    helicopter_ = helicopter_.replace("y", "")   
    if(len(helicopter_) == 0):
       helicopter.hp = 0
      
screen.listen()
screen.mainloop()
wn.mainloop()