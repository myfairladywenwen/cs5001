horizon = [[1,2,3],[4,5,6],[7,8,9]]
print(horizon)
vertical = [row[i] for row in horizon for i in range(3)]
print(vertical)

matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
new = [[row[i] for row in matrix] for i in range(3)]
print(new)
new2 = list(zip(*matrix))
print(new2)