def draw_cube(size):
    '''This function draws a cube of given size.
    Int -> None'''

    draw_up(size)
    draw_mid(size)
    draw_bottom(size)


def draw_up(size):
    '''This function draws the upper part of the cube of a given size.
    Int -> None'''
    VERTICAL = '|'
    DIAGONAL = '/'

    print(' ' * (size//2 + 1), end='')
    draw_up_line(size)
    for i in range(size//2):
        print(' ' * (size//2 - i), end='')
        print(DIAGONAL, end='')
        print(' ' * 2 * size, end='')
        print(DIAGONAL, end='')
        print(' ' * i, end='')
        print(VERTICAL)
    draw_mid_line(size)


def draw_up_line(size):
    '''This function draws the ceiling of the cube of a given size.
    Int -> None'''
    CORNOR = '+'
    HORIZON = '-'

    print(CORNOR, end='')
    print(HORIZON * 2 * size, end='')
    print(CORNOR)


def draw_mid_line(size):
    '''This function draws the mid line(the upper line of the front)
    of the cube of a given size.
    Int -> None'''
    CORNOR = '+'
    HORIZON = '-'
    VERTICAL = '|'

    print(CORNOR, end='')
    print(HORIZON * 2 * size, end='')
    print(CORNOR, end='')
    print(' ' * (size//2), end='')
    print(VERTICAL)


def draw_mid(size):
    '''This function draws the mid part(the front) of the cube of a given size.
    Int -> None'''
    CORNOR = '+'
    VERTICAL = '|'
    DIAGONAL = '/'

    # draw upper part of mid
    for _ in range(size//2 - 1):
        print(VERTICAL, end='')
        print(' ' * (2 * size), end='')
        print(VERTICAL, end='')
        print(' ' * (size//2), end='')
        print(VERTICAL)
    # draw mid part of mid
    print(VERTICAL, end='')
    print(' ' * (2 * size), end='')
    print(VERTICAL, end='')
    print(' ' * (size//2), end='')
    print(CORNOR)
    # draw lower part of mid
    for i in range(size//2):
        print(VERTICAL, end='')
        print(' ' * 2 * size, end='')
        print(VERTICAL, end='')
        print(' ' * (size//2 - i - 1), end='')
        print(DIAGONAL)


def draw_bottom(size):
    '''This function draws bottom line of the cube of a given size.
    Int -> None'''

    draw_up_line(size)


def main():
    '''This program promt the user for an integer(multiple of 2)
    and draws a cube which size is determined by this user input.
    None -> None'''

    size = int(input('Input cube size (multiple of 2): '))
    draw_cube(size)


main()
