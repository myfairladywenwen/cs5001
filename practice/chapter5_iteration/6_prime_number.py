value = int (input('enter a positive number:'))
print('method1: ', end='')
for i in range(1, value+1):
    divisor_count = 0
    for divisor in range(1, i+1):
        if i % divisor == 0:
            divisor_count +=1
    if divisor_count == 2:
        print(i, ' ',end='')
print()

print('method2: ', end='')
i = 2 #最小的质数是 2
while i <= value:
    is_prime = True #这句如果放在 while 外面就不对了
                #因为一旦 isPrime 成了 false，永远 false，回不来了
    divisor = 2
    while divisor < i:     #这里也可以rewrite:while is_prime and divisor<i
        if i%divisor == 0:                      #is_prime = (i%divisor!=0)
            is_prime = False                    #divisor+=1
            break
        divisor += 1
    else:#没有触发 while 里的 break，所以出来执行 else。
         #这里也可以写成if isPrime:
        print(i,' ',end='')
    i +=1
print()
print('method3: ',end='')
i = 2
for i in range(2, value):
    #is_prime = True 不需要设 flag 了
    for divisor in range(2, i):
        if (i%divisor == 0):
            break
        #divisor+=1
    else:
        print(i,' ', end='')
print()

print('method4: ',end='')
from math import sqrt
i = 2
for i in range(2, value+1):
    for divisor in range(2, int(sqrt(i)+1)):#在 2~这个数的平方根的之间找，
        #因为如果平方根之后还有 divisor，那么必然在平方根之前出现过 divisor
        if i%divisor == 0:
            break
    else:
        print(i, ' ',end='')
print()
        



