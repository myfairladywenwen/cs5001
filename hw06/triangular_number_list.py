def triangular_number(n):
    ''' This prgram calculates the triangular number for the input,
    print it and return it.
    int -> int '''
    sum = 0
    for i in range(1, n+1):
        sum += i
    print("The triangular number for", n, "is", sum)
    return sum


def main():
    ''' This program prompts for user input and will print the triangular
    number for the user input unless user input is done.
    When done, the program prints the list of all former triangular numbers.
    None -> None '''

    KEY = 'done'  # set the input value to end the program as a constant KEY

    mylist = []
    while True:
        user_input = input('Enter a number, or enter \'done\': ')
        if user_input == KEY:
            break
        else:
            result = triangular_number(int(user_input))
            mylist.append(result)
    print(mylist)


main()
