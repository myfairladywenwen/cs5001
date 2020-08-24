from math import sqrt
n = int(input('enter a number: '))
result1 = [(x,n//x) for x in range(1, n+1) if n % x == 0]
print(result1)
result2 = [(x,n//x) for x in range(1, int(sqrt(n))+1) if n % x == 0]
#result2 = [(x,n//x) for x in range(1, n+1) for (n//x) in range(int(sqrt(n))+1, n+1) if n % x == 0]
print(result2)
