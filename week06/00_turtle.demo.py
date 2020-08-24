import turtle as t

t.shape("turtle")    # triangle, arrow, classic, circle
# t.hideturtle()
t.delay(1)            # for update
t.speed("slowest")    # speed of turtle

t.pensize(5)
t.pencolor("red")
t.fillcolor("yellow")

# t.pd()    pendown
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

t.pu()

t.goto(-100, -50)
t.pencolor("purple")
t.fillcolor("cyan")
t.setheading(45)    # rotate the direction the pen is going forward

t.pd()
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

t.exitonclick()

t.done()
