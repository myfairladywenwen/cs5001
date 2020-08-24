import turtle

def main():
    turtle.pencolor('red')
    turtle.forward(200)
    turtle.left(90)
    turtle.pencolor('blue')  # Change pen color to blue
    turtle.forward(150)
    turtle.left(90)
    turtle.pencolor('green') # Change pen color to green
    turtle.forward(200)      # Move pen forward 200 units (create top)
    turtle.left(90)          # Turn pen by 90 degrees
    turtle.pencolor('black') # Change pen color to black
    turtle.forward(150)
    turtle.hideturtle()
    turtle.exitonclick()

main()