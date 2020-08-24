def main():
    '''    This program validates a variety of identification numbers.
    None -> None'''

    done = False
    while not done:
        input_string = input('Please enter a number you want to validate' +
                             '(\'done\' to quit): ')
        if input_string == 'done':
            done = True
        else:
            if validate(input_string):
                print('Your sequence is valid.')
            else:
                print('Your sequence is not valid.')


def validate(input):
    '''    This function uses Luhn’s algorithm to
    validates a given sequence of numbers.
    String -> Bool'''

    EDGE = 1    # starting from the second to right-most digit
    KEY = 10
    input_list = [int(x) for x in input]
    i = len(input_list) - 1 - EDGE
    while i >= 0:
        i_value = 2 * input_list[i]
        if i_value >= 10:
            m = i_value
            i_value = m // 10 + m % 10
        input_list[i] = i_value
        i -= 2
    sum = 0
    for num in input_list:
        sum += num
    return(sum % KEY == 0)


main()
