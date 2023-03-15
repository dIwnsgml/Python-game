import turtle as trtl

def create_tank():
    tank = trtl.Turtle()
    tank.shape('./Img/tank/moving/left/frame_0.gif')
    tank.resizemode('auto')
    tank.speed(3)
    tank.penup()
    i = 0
    while(True):
        tank.shape('./Img/tank/moving/left/frame_'+str(i % 6) + '.gif')
        tank.setheading(180)
        tank.forward(3)
        i+=1