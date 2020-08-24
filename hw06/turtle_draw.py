import turtle
import math
STAR_SIDES = 5
STAR_SIDE_LEN = 500
STAR_COLOR = 'red'
STAR_FILL_COLOR = 'yellow'
CIRCLE_COLOR = 'blue'
CIRCLE_FILL_COLOR = 'cyan'
PENTA_ANGLE = 540
STRAIGHT_ANGLE = 180
SUM_OF_TRIANGLE = 180
# set the precision for the circle, the bigger this number,
# the closer it looks like a circle
CIRCLE_PRECISION = 500


def draw_circle(pos, color, r, cir_precision, fillcol):
    '''This function draws a circle of given size, from the given positon
    Tuple, string, float, int, string -> None'''
    ROUND_ANGLE = 360

    circle_distance = (2 * math.pi * r)/CIRCLE_PRECISION
    circle_angle = (ROUND_ANGLE/CIRCLE_PRECISION)
    turtle.penup()
    turtle.setposition(pos)
    turtle.pendown()
    turtle.fillcolor(fillcol)
    turtle.begin_fill()
    for _ in range(CIRCLE_PRECISION):
        turtle.pencolor(color)
        turtle.forward(circle_distance)
        turtle.right(circle_angle)
    turtle.end_fill()


def draw_star(pos, color, side_len, number_of_sides, fillcol):
    '''This function draws a star of given size, from the given positon
    Tuple, string, int, int, string -> None'''

    turtle.pencolor(color)
    turtle.penup()
    turtle.setposition(pos)
    take_turn1 = STRAIGHT_ANGLE - PENTA_ANGLE/number_of_sides
    turtle.right(take_turn1)
    turtle.pendown()
    turtle.fillcolor(fillcol)
    turtle.begin_fill()
    turtle.forward(side_len)
    take_turn2 = STRAIGHT_ANGLE - (SUM_OF_TRIANGLE - 2 * take_turn1)
    for _ in range(number_of_sides - 1):
        turtle.right(take_turn2)
        turtle.forward(side_len)
    turtle.end_fill()


def main():
    '''This program draws a circle and a star of given size,
    at the given positon, and fill the graph with given color
    None -> None'''

    # calculate the radius of the circle
    r = (STAR_SIDE_LEN / 2)/math.cos(math.radians((SUM_OF_TRIANGLE -
                                                  2 * (STRAIGHT_ANGLE -
                                                   PENTA_ANGLE/STAR_SIDES))/2))
    star_pos = (0, r)
    cir_precision = CIRCLE_PRECISION
    draw_circle(star_pos, CIRCLE_COLOR, r, cir_precision, CIRCLE_FILL_COLOR)
    draw_star(star_pos, STAR_COLOR, STAR_SIDE_LEN, STAR_SIDES, STAR_FILL_COLOR)
    turtle.exitonclick()


main()
