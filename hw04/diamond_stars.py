EDGE = 1


def main():
    '''
    This program draws a diamond star of the height given by user input.
    The shape would be a bit different when it comes to the mid,
    according to the parity of the input.
    '''

    height = int(input("Enter the height of the diamond: "))
    if height % 2 == 1:
        for i in range(-int((height-1)/2), int((height-1)/2)+1):
            number_of_spaces = abs(i)
            print(' ' * number_of_spaces, end='')
            print('*' * (height - 2 * number_of_spaces))
    else:
        for i in range(-int(height/2), int(height/2)):
            if i < 0:
                number_of_spaces = abs(i) - 1
                print(' ' * number_of_spaces, end='')
                print('*' * (height - EDGE - 2 * number_of_spaces))
            else:
                number_of_spaces = i
                print(' ' * number_of_spaces, end='')
                print('*' * (height - EDGE - 2 * number_of_spaces))


main()