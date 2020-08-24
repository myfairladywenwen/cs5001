import sys


def main():
    max = int(sys.argv[1])
    # command line 在 python3 02_prime_naive.py 之后输入啥int，max就是啥
    
    print(2)
    i = 3

    while (i <= max):
        is_prime = True
        k = 2
        while (k < i):
            if (i % k == 0):
                is_prime = False
            k += 1
        
        if is_prime:
            print(i)
        i += 1
# for loop 会快一些，因为我们知道 range，
# 不用每次去 while 后面的条件check

main()