r = 1
n = 3
for i in range(n):
    for j in range(1, n+1):
        for k in range(1, j+1):
            r = r * 2
print(r)