import sys


def main():
    height = int(sys.argv[1])
    for h in range(height):
        print('*' * h)


main()