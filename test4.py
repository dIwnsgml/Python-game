import turtle
import multiprocessing

def draw_square(screen):
    # Create a turtle object and draw a square
    t = turtle.Turtle()
    t.screen = screen
    for i in range(4):
        t.forward(100)
        t.right(90)

def draw_triangle(screen):
    # Create a turtle object and draw a triangle
    t = turtle.Turtle()
    t.screen = screen
    for i in range(3):
        t.forward(100)
        t.left(120)

if __name__ == '__main__':
    # Create a turtle screen object
    screen = turtle.Screen()

    # Create a new process for each function, passing the screen as an argument
    process1 = multiprocessing.Process(target=draw_square, args=(screen,))
    process1.start()

    process2 = multiprocessing.Process(target=draw_triangle, args=(screen,))
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    # Update the turtle screen in the main process
    screen.mainloop()
