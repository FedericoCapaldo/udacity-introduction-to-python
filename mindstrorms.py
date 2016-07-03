import turtle

def draw_square(my_turtle):
    for i in range(1,5):
        my_turtle.forward(100)
        my_turtle.right(90)

def draw_start(my_turtle):
    for i in range(1,10):
        my_turtle.forward(300)
        my_turtle.right(160)

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('blue')
    brad.speed(200)

    n=0
    while(n<37):
        draw_square(brad)
        brad.right(10)
        n = n+1

    littleTurtle = turtle.Turtle()
    littleTurtle.shape('turtle')
    littleTurtle.color('white')
    littleTurtle.speed('200')

    x=0
    while(x<13):
        littleTurtle.circle(100)
        littleTurtle.right(10)
        draw_square(littleTurtle)
        littleTurtle.right(20)
        x = x+1

    zigzagTurtle = turtle.Turtle()
    zigzagTurtle.shape('turtle')
    zigzagTurtle.color('yellow')
    zigzagTurtle.speed(200)


    for i in range(1,6):
        draw_start(zigzagTurtle)
        zigzagTurtle.left(72)

    window.exitonclick()

draw_shapes()
