lst1 = [] * 3
print(lst1)

lst2 = [[]] * 3
print(lst2)
for i in range(3):
    lst2.append(i)
print(lst2)

lst2 = [[]] * 3
for i in range(3):
    lst2 += [i]
print(lst2)

lst2 = []
for i in range(3):
    lst2.append(input())
print(lst2)

lst3 = [[]] * 3
print(lst3)

lst4 = []
for row in range(3):
        lst_row = [x for x in input()]
        lst4.append(lst_row)
print(lst4)