from sys import argv
from math import sqrt


def main():
    '''
        This program draws a circle of the radius
        get from the command line
    '''

    r = int(argv[1])
    d = 2 * r
    # make every dot in the list
    lst_of_dots = []
    for y in range(d+1):
        lst = [(x, y) for x in range(d+1)]
        lst_of_dots.append(lst)

    # start drawing
    for line in lst_of_dots:
        for dot in line:
            # decide what character should the dot be
            x, y = dot
            distance = int(sqrt((x - r) ** 2 + (y - r) ** 2))
            if distance >= r:
                print(' ', end='')
            else:
                print('o', end='')
        print('\n')


main()