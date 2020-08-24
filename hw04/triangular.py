import sys


def main():
    '''
    This program calulate the triangel number
    of the user input from command line.
    '''

    n = int(sys.argv[1])
    sum = 0
    for i in range(1, n+1):
        sum += i
    print("The triangular number of", n, "is", sum, end='')
    print(".")

main()