import copy
lista = [[1, 2, 3], [4, 5, 6]]
listb = []
for item in lista[1:]:
    listb.append(item)
print(listb)
print(lista is listb)
print(lista[1] is listb[0])
lista[1].append(4)

print("after append sth in lista[1], listb[0]:", listb[0])

print("lista:", lista)
print("listb:", listb)

# listc = []
# listc = copy.deepcopy(lista)
# print(listc)