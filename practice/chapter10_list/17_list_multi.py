a = [0] * 5
b = a
a[0] = 1
print(a)  # [1,0,0,0,0]
print(b)  #[1,0,0,0,0]

c = [0]
d = c * 5
print(d)  # [0,0,0,0,0]
c = [1]
print(c)  # [1]
print(d)  # [0,0,0,0,0]why not [1, 1, 1, 1, 1]

c = [[0]]
d = c * 5
print(d[0] is d[1])  # true
c[0][0] = 1
print(d)  # [[1],[1],[1],[1],[1]]

l = [[]] * 3
l[0].append(1)
print(l)  # [[1], [1], [1]]
l = [[]] * 3
l[0] = 1
l[1] = 2
l[2] = 3
print(l)  # [1, 2, 3]