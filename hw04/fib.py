import sys
INITIAL_NUM_1 = 0
INITIAL_NUM_2 = 1


def main():
    '''
    This program output the fisrt N Fibonacci sequence
    where N is the input value from the command line.
    The output would be a list.
    '''

    n = int(sys.argv[1])
    fib_lst = [INITIAL_NUM_1, INITIAL_NUM_2]
    for idx in range(2, n):
        curr_num = int(fib_lst[idx - 2]) + int(fib_lst[idx - 1])
        fib_lst.append(curr_num)
    print(fib_lst)


main()