import turtle
import multiprocessing

def draw_circle(x, y, screen):
    t = turtle.Turtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(50)
    screen.exitonclick()

if __name__ == '__main__':
    # Initialize the turtle screen
    screen = turtle.Screen()
    screen.setup(800, 600)

    # Create a shared queue to communicate between the processes
    queue = multiprocessing.Queue()

    # Spawn two processes to draw on the turtle screen
    p1 = multiprocessing.Process(target=draw_circle, args=(0, 0, screen))
    p2 = multiprocessing.Process(target=draw_circle, args=(100, 100, screen))
    p1.start()
    p2.start()

    # Wait for the processes to finish
    p1.join()
    p2.join()
