import turtle as trtl
import time
import random
screen = trtl.Screen()
tanks_info = []
tanks_n = 0

def tank_missile(x, y, character):
    missile = trtl.Turtle()
    missile.penup()
    missile.goto(x, y)
    missile.shape('./img/tank/fire1/missile1.gif')
    missile.setheading(90)
    while(missile.ycor() > 20):
        missile.forward(30)
        missile.left(5)
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
    missile.clear()
    missile.reset()

def tank_bullet(x, y, character):
  tank_bullet = trtl.Turtle()
  tank_bullet.penup()
  tank_bullet.goto(x, y - 20)
  tank_bullet.shape('./img/tank/fire1/bullet.gif')
  tank_bullet.setheading(180)
  """ while(x - screen.window_width() < tank_bullet.xcor() and (character.xcor() < tank_bullet.xcor() and character.ycor() -45 > tank_bullet.ycor())):  """
  print(character.ycor() - 45, tank_bullet.ycor())
  while(True):
      if(abs(character.xcor() - tank_bullet.xcor()) < 20 and abs(character.ycor() - tank_bullet.ycor()) < 10):
          print("hit", tank_bullet.ycor(), character.ycor())
          break
      tank_bullet.forward(10)
      time.sleep(0.01)

def create_tank(x, y, character):
    global tanks_n
    global tanks_info
    tanks_n += 1
    tank = trtl.Turtle()
    tank.penup()
    tank.goto(x, y + 60)
    tank.shape('./img/tank/moving/left/frame_0.gif')
    words = ["orange", "red", "pink", "purple", "green", "cyan", "blue"]
    rand_enemy = random.choice(words)
    enemylist = []
    enemylist.append(rand_enemy)
    tanks_info.append([180, 1, "move"])
    tank.resizemode('auto')
    i = 0
    tank_type = random.randrange(0, 1)

    while(True):
        if(tanks_info[tanks_n - 1][2] == "move" and character.xcor() + screen.window_width() < tank.xcor()):
            tank.shape('./img/tank/moving/left/frame_'+str(i % 6) + '.gif')
            tank.forward(1)
            tank.setheading(tanks_info[tanks_n - 1][0])
            time.sleep(0.001)
            """ print(x, character.xcor(), tank.xcor()) """
        else:
            tank.shape('./img/tank/fire1/left/frame_'+str(i % 17) + '.gif')
            time.sleep(0.12)
            if(i % 17 == 3):
                t[2] = threading.Thread(target=tank_bullet, args=(tank.xcor(), tank.ycor(), character))
                t[2].start()
            elif(i % 17 == 10):
                t[2] = threading.Thread(target=tank_missile, args=(tank.xcor(), tank.ycor(), character))
                t[2].start()
        i+=1