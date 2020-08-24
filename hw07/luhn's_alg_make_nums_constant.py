def main():
    '''    This program validates a variety of identification numbers.
    None -> None'''
    NUM1 = 79927398713
    NUM2 = 49927398716
    NUM3 = 1234567812345670
    NUM4 = 12345675
    NUM5 = 49927398717
    NUM6 = 1234567812345678
    validate(NUM1)
    validate(NUM2)
    validate(NUM3)
    validate(NUM4)
    validate(NUM5)
    validate(NUM6)


def validate(input):
    '''    This function uses Luhn’s algorithm to
    validates a given sequence of numbers.
    Int -> None'''

    EDGE = 1    # starting from the second to right-most digit
    KEY = 10
    input_list = [int(x) for x in str(input)]
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
    if sum % KEY == 0:
        print(input, 'is valid.')
    else:
        print(input, 'is not valid.')


main()
