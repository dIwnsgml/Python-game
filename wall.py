import turtle as trtl
import random
trtl.speed(0)
trtl.delay(0)
screen = trtl.Screen()
wn = trtl.Screen()

floor = trtl.Turtle()
spikes = trtl.Turtle()
def sqaure_drawer(x, y):
    global floor
    floor.penup()
    floor.goto(x, y)
    floor.pendown()
    floor.pencolor("#f8c381")
    floor.pensize(3)
    floor.begin_fill()
    floor.fillcolor("#aa6109")
    floor.goto(x + 40, y)
    floor.goto(x + 40, y - 40)
    floor.goto(x, y - 40)
    floor.goto(x, y)
    floor.end_fill()
    floor.goto(x + 30, y)
    floor.pencolor("#000")
    floor.goto(x + 30, y - 10)
    floor.goto(x + 40, y - 10)
    floor.goto(x + 30, y - 10)
    floor.goto(x + 20, y - 35)
    floor.goto(x +18, y - 40)
    floor.goto(x + 20, y - 35)
    floor.goto(x, y - 30)
    floor.penup()
    floor.goto(x, y)


def add_spikes(startx, starty, endx):
    global spikes
    spikes.penup()
    spikes.goto(startx + 40, starty)
    spikes.pendown()
    while(spikes.xcor() < endx):
        spikes.goto(spikes.xcor() + 10, spikes.ycor() + 50)
        spikes.goto(spikes.xcor() + 10, spikes.ycor() - 50)
    spikes.penup()

""" 
          floor_info.append([floor.ycor(), floor.xcor()])
          while(block_length > 0):
              horizontal_rect()
              block_length -= 1
          floor_info[floor_n].append(floor.xcor())
 """
def draw_floor(startx, starty, endx):
    global floor_info, floor_info_n
    floor_info = []
    floor_info_n = 0
    #0 = normal floor, -1 = floor that goes under 1, -2 = floor that goes under 2, -3 = spikes, -4 = no block
    floor_percentage = [0, 0 ,0 ,0, 0, 0, 0,-1, -1 ,-2 ,-3, -4]
    floor.penup()
    floor.goto(startx, starty)
    floor.pendown()
    for i in range(20):
        sqaure_drawer(floor.xcor() + 40, floor.ycor())
    """ for i in range(2):
        sqaure_drawer(floor.xcor(), floor.ycor() - 40)
        floor_info.append([floor.ycor(), floor.xcor() + 40])
    for i in range(4):
        sqaure_drawer(floor.xcor() + 40, floor.ycor())
    floor_info[floor_info_n].append(floor.xcor())
    floor_info[floor_info_n].append(-1)
    for i in range(2):
        sqaure_drawer(floor.xcor(), floor.ycor() + 40)
    for i in range(4):
        sqaure_drawer(floor.xcor() + 40, floor.ycor())
    floor_info_n += 1 """
    while(floor.xcor() < endx):
        floor_state = random.choice(floor_percentage)
        if(floor_state == 0):
            for i in range(5):
                sqaure_drawer(floor.xcor() + 40, floor.ycor())
        elif(floor_state == -1):
            for i in range(2):
                sqaure_drawer(floor.xcor(), floor.ycor() - 40)
            floor_info.append([floor.ycor(), floor.xcor() + 40])
            for i in range(4):
                sqaure_drawer(floor.xcor() + 40, floor.ycor())
            floor_info[floor_info_n].append(floor.xcor())
            floor_info[floor_info_n].append(floor_state)
            for i in range(2):
                sqaure_drawer(floor.xcor(), floor.ycor() + 40)
            for i in range(4):
                sqaure_drawer(floor.xcor() + 40, floor.ycor())
            floor_info_n += 1
        elif(floor_state == -2):
            for i in range(4):
                sqaure_drawer(floor.xcor(), floor.ycor() - 40)
            floor_info.append([floor.ycor(), floor.xcor() + 40])
            for i in range(8):
                sqaure_drawer(floor.xcor() + 40, floor.ycor())
            floor_info[floor_info_n].append(floor.xcor())
            floor_info[floor_info_n].append(floor_state)
            for i in range(4):
                sqaure_drawer(floor.xcor(), floor.ycor() + 40)
            for i in range(4):
                sqaure_drawer(floor.xcor() + 40, floor.ycor())
            floor_info_n += 1
        elif(floor_state == -3):
            for i in range(4):
                sqaure_drawer(floor.xcor(), floor.ycor() - 40)
            add_spikes(floor.xcor(), floor.ycor(), floor.xcor() + 320)
            floor_info.append([floor.ycor(), floor.xcor() + 40])
            for i in range(8):
                sqaure_drawer(floor.xcor() + 40, floor.ycor())
            floor_info[floor_info_n].append(floor.xcor())
            floor_info[floor_info_n].append(floor_state)
            for i in range(4):
                sqaure_drawer(floor.xcor(), floor.ycor() + 40)
            for i in range(4):
                sqaure_drawer(floor.xcor() + 40, floor.ycor())
            floor_info_n += 1
        elif(floor_state == -4):
            for i in range(4):
                sqaure_drawer(floor.xcor(), floor.ycor() - 40)
            floor_info.append([floor.ycor(), floor.xcor() + 40])
            sqaure_drawer(floor.xcor() + 200, floor.ycor())
            floor_info[floor_info_n].append(floor.xcor())
            floor_info[floor_info_n].append(floor_state)
            for i in range(4):
                sqaure_drawer(floor.xcor(), floor.ycor() + 40)
            for i in range(4):
                sqaure_drawer(floor.xcor() + 40, floor.ycor())
            floor_info_n += 1
    
    return [floor_info, floor_info_n]