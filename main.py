import turtle as trtl

#-----setup-----

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)

wn.bgpic("bgtest.gif")
  
player = trtl.Turtle()
player.color("blue")
player.shape("square")
player.shapesize(5, 10)

camera_dx = 0

def left():
    wn.xview_scroll(-1, "units")
    global camera_dx
    camera_dx -= 5
    player.forward(-10)

def right():
    global camera_dx
    camera_dx += 5
    player.forward(10)

wn.onkeypress(left, 'Left')
wn.onkeypress(right, 'Right')
wn.listen()
wn.mainloop()