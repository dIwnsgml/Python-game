import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=1.0, height=1.0)

# Load the background image
bg_image = "image.png"
screen.addshape(bg_image)

# Get the size of the screen
screen_width, screen_height = screen.window_width(), screen.window_height()

# Set the background image
screen.bgpic(bg_image)

# Resize the background image to fill the screen
bg_turtle = turtle.Turtle()
bg_turtle.speed(0)
bg_turtle.penup()
bg_turtle.goto(0, 0)
bg_turtle.shape(bg_image)
bg_turtle.shapesize(screen_width / 20, screen_height / 20)

turtle.done() # Keep the window open
