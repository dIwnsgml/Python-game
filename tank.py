import turtle as trtl
import time

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
    while(True):
        print(tanks_info[0][2])
        if(tanks_info[tanks_n - 1][2] == "move"):
            tank.shape('./img/tank/moving/left/frame_'+str(i % 6) + '.gif')
            tank.forward(1)
            tank.setheading(tanks_info[tanks_n - 1][0])
            time.sleep(0.001)
            print(x, character.xcor())
        elif(tanks_info[tanks_n - 1][2] == "fire1"):
            tank.shape('./img/tank/fire1/left/frame_'+str(i % 10) + '.gif')
            time.sleep(0.1)
        elif(tanks_info[tanks_n - 1][2] == "fire1"):
            tank.shape('./img/tank/fire2/left/frame_'+str(i % 7) + '.gif')
            time.sleep(0.001)
        i+=1
