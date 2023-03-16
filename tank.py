import turtle as trtl
import time

def create_tank(character_x):
    tank = trtl.Turtle()
    tank.shape('./img/tank/moving/left/frame_0.gif')
    tank.resizemode('auto')
    tank.speed(3)
    tank.penup()
    tank.state = "move"
    i = 0
    while(True):
        if(tank.state == "move"):
            tank.shape('./img/tank/moving/left/frame_'+str(i % 6) + '.gif')
            tank.setheading(180)
            tank.forward(1)
            time.sleep(0.001)
            i+=1
            print(character_x, character)
        elif(tank.state == "fire1"):
            tank.shape('./img/tank/fire1/left/frame_'+str(i % 6) + '.gif')