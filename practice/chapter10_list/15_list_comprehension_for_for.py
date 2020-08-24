horizon = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vertical_wrong = [row[i] for row in horizon for i in range(3)]
print(vertical_wrong)
vertical_right = [[row[i] for row in horizon] for i in range(3)]
print(vertical_right)
