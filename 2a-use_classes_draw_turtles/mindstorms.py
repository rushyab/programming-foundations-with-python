import turtle

def draw_square(some_turtle):
    for _ in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    # Create the turle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)
    for _ in range(36):   # 36 x 10 = 360 degrees 
        draw_square(brad) # draw square
        brad.right(10)    # turn right by 10 degrees
    
    # Create the turtle Angie - Draws a Circle
    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("red")
    # angie.circle(100)

    window.exitonclick()


draw_art()

