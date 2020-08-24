from sys import argv
NOSE_TAIL_SYMBOL = '*'
FUSE_SYMBOL = 'X'
STRIP_SYMBOL = '_'


def main():
    ''' This progrm takes in width, length and whether split or nor from the
    command line and decides what kind of rocket to draw.
    None -> None'''

    if len(argv) == 3:
        make_a_rocket(int(argv[1]), int(argv[2]))
    else:
        make_a_rocket(int(argv[1]), int(argv[2]), argv[3])


def make_a_rocket(width, length, do_strip=None):
    ''' This function draws a rocket of given width, length
    and whether striped or not.
    Int, Int, Str -> None'''

    draw_nose(width)

    if do_strip is None:
        draw_fuselage_no_strip(width, length)
    else:
        draw_fuselage_strip(width, length)

    draw_tail(width)


def draw_nose(width):
    ''' This function draws the nose of the rocket of given width.
    Int -> None'''

    if width % 2 != 0:
        for line in range(width // 2):
            print(' ' * ((width - (2 * line + 1)) // 2), end='')
            print(NOSE_TAIL_SYMBOL * (2 * line + 1))
    else:
        for line in range(width // 2 - 1):
            print(' ' * ((width - (2 * (line + 1))) // 2), end='')
            print(NOSE_TAIL_SYMBOL * (2 * (line + 1)))


def draw_fuselage_no_strip(width, length):
    ''' This function draws the middle part of the rocket of given width and
    length, without any strip.
    Int, Int -> None'''

    for _ in range(length):
        for _ in range(width):
            print(FUSE_SYMBOL * width)


def draw_fuselage_strip(width, length):
    ''' This function draws the middle part of the rocket of given width and
    length, with the mid part striped into two style.
    Int, Int -> None'''

    for _ in range(length):
        for _ in range(width // 2):
            print(STRIP_SYMBOL * width)
        for _ in range(width - width//2):
            print(FUSE_SYMBOL * width)


def draw_tail(width):
    ''' This function draws the tail of the rocket of given width.
    Int -> None'''

    sym_num = width//2
    while sym_num <= width - 2:
        print(' ' * ((width - sym_num) // 2), end='')
        print(NOSE_TAIL_SYMBOL * sym_num)
        sym_num += 2
    for _ in range(2):
        print(NOSE_TAIL_SYMBOL * width)


main()
