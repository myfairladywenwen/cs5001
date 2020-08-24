import sys


def main(number):
    print(tri(number))

def tri(number):
    if number == 0:
        return 0
    return number + tri(number - 1)

main(int(sys.argv[1]))