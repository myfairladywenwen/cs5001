from turtle import *
# Part 1
# Create a turtle object named t1
# Create a second turtle object named t2
# t1's pen color is red
t1 = Turtle()
t2 = Turtle()
t1.pencolor('red')
t2.pencolor('blue')  # t2's pen color is blue
t2.left(90)    # Point t2 up (t1 automatically points to the right)
t1.forward(100)
t2.forward(50)
# Part 2
t2 = t1         # Make the second turtle just like the first?
t2.right(45)    # Turn turtle 2 (but not turtle 1?)
t2.forward(50)  # Move turtle 2 (why does turtle 1 move instead?)
done()
