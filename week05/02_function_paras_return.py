import sys


def main():
    hello_function("world!")

    string1 = '&' * double_num(6)
    print(string1)
    
    string2 = '%' * add_nums(5, 7)
    string3 = '*' * add_nums(double_num(3), 6)
    print(string2)

    (x, y, z) = multi_value_return()
    print('x is', x)
    print('y is', y)
    print('z is', z)

    no_val_return()

def hello_function(argument):
    """Prints a hello message with a value
    String -> None"""
    print("hello", argument)


def double_num(number):
    """doubles a number
    Number -> Number"""
    return 2 * number


def add_nums(x, y):
    """add 2 numbers
    Number  Number -> Number"""
    return x + y


def multi_value_return():
    """Return three characters
    None -> Character Character Character"""
    return 'a', 'b', 'c'


def no_val_return():
    """Prints a string
    None -> None"""
    print("Just print this and not return anything")
main()