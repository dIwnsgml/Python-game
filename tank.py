import turtle as trtl

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
      tank_bullet.forward(30)
      time.sleep(0.015)

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
            elif(i % 17 == 10):
                t[2] = threading.Thread(target=tank_missile, args=(tank.xcor(), tank.ycor()))
                t[2].start()
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