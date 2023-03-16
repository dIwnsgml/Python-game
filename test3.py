import turtle as trtl
from random import random
import keyboard
import sys
import time
import threading
import multiprocessing

""" sys.setrecursionlimit(100000) """
sys.setrecursionlimit(100)
sys.setswitchinterval(0.001)
from border import create_border
from gravity import create_gravity
from tank import create_tank

MAGNIFICATION = 10

screen = trtl.Screen()
width, height = screen.screensize()
screen.screensize(10000, 800)

canvas = screen.getcanvas()
canvas.config(xscrollincrement=str(MAGNIFICATION))
canvas.config(yscrollincrement=str(MAGNIFICATION))
screen.addshape("./Img/character/run/right/frame_0.gif")
# character initialization
character = trtl.Turtle()
character.shape('./Img/character/run/right/frame_0.gif')
def create_element():
    # Create a new element on the canvas
    character.shape('./Img/character/run/right/frame_0.gif')
# Create a new canvas

# Create a new process to create the element

process = multiprocessing.Process(target=create_element, args=())
print(__name__)
if __name__ == '__main__':
    print("A")
    process.start()
    process.join()

screen.listen()
screen.mainloop()