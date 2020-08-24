TOP = '*'
LEFT_SIDE = '/'
RIGHT_SIDE = '\\'
BOTTOM = '_'


def main():
    '''
    This a program drwaing Christmas tree with user input of an odd number,
    representing the width of the tree.
    The program will not accept even numbers and will prompt the user for
    another odd number until the user provides the valid value.
    '''
    # ensure valid user input
    width = int(input('Please enter an odd number: '))
    while width % 2 == 0:
        width = int(input('Only odd numbers are valid.  ' +
                          'Please enter an odd number:'))

    # draw the top
    print(' ' * ((width - 1) // 2), end='')
    print(TOP)

    # draw the middle part
    for i in range(1, width - 2, 2):
        print(' ' * ((width - i - 2) // 2), end='')
        print(LEFT_SIDE, end='')
        print(' ' * i, end='')
        print(RIGHT_SIDE)

    # draw the bottom
    print(LEFT_SIDE, end='')
    for i in range(width - 2):
        print(BOTTOM, end='')
    print(RIGHT_SIDE)


main()