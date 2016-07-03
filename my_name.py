import turtle


def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('blue')
    brad.speed(2)

    brad.left(90)
    brad.forward(250)
    brad.right(90)
    brad.forward(120)
    brad.right(180)
    brad.forward(120)
    brad.left(90)
    brad.forward(70)
    brad.left(90)
    brad.forward(70)
    brad.left(180)
    brad.forward(70)
    brad.right(90)
    brad.forward(70)
    brad.right(90)
    brad.forward(120)
    brad.color('yellow')
    brad.forward(120)
    brad.right(180)
    brad.forward(120)
    brad.left(90)
    brad.forward(250)
    brad.left(90)
    brad.forward(120)

    window.exitonclick()

draw_shapes()
