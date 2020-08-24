from sys import argv
from math import sqrt


if len(argv) < 3:
    print('not enough info')
else:
    for n in range(int(argv[1]), int(argv[2])+1):
        print(n, sqrt(n))
