import sys
import math
import time 


def main():
    max = int(sys.argv[1])
    # command line 在 python3 02_prime_naive.py 之后输入啥int，max就是啥
    
    print(2)
    start = time.time()
    

    for i in range(3, max+1 ,2):
        # increment by 2 fill out all the even numbers, 快了一倍
        is_prime = True
        k = 2
        # while (k < i):
        while(k <= math.sqrt(i) and is_prime):
            # 100,check 到 k = 2,就发现不是 prime了
            # 那么不需要再 check 后面的了
            if (i % k == 0):
                is_prime = False
            k += 1
        
        if is_prime:
            print(i)
    end = time.time()
    print(end - start)
 


main()