def main():
    '''
    This is a program that draws a rectangle for
    the user, using the use's choice of symbol,
    with the size the user input.
    '''

    # prompt for user input
    symbol = input("I can draw a rectriagle for you with a single" +
                   " symbol (e.g., &, #, +, n, s, 3)" +
                   " Please enter which symbol you want: ")
    width = int(input("now enter the width: "))
    height = int(input("also please enter the height: "))

    # draw the top
    print(symbol * width)

    # draw middle part
    for i in range(height - 2):
        print(symbol, end='')
        print(' ' * (width - 2), end='')
        print(symbol)

    # draw the bottom
    print(symbol * width)


main()