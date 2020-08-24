MAX = 20
n = 1
print('method 1:')
while n <= MAX:
    print(n, ':', sep ='', end='')
    #print(end = str(n)+':')
    factor = 1
    while factor <= n:
        if n % factor == 0:
            print(factor,'', end='')
        factor+=1
    print()
    n+=1
print('method 2:')
n = 1
for n in range(1, MAX+1):
    print(n,':', sep='', end='')
    factor = 1
    for factor in range(1, n+1):
        if n%factor == 0:
            print(factor,'', end='')
        factor+=1
    print()




