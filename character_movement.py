def freeze():
    screen.onkeypress(None, "Left")
    screen.onkeypress(None, "Right")
    screen.onkeypress(None, "Up")
    screen.onkeypress(None,"space")
    screen.onkeyrelease(None, "Right")
    screen.onkeyrelease(None, "Left")