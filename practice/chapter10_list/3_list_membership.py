lst = list(range(0,22,2))
for i in range(-2,23):
    if i in lst:
        print(i, "is in the list", lst)
    else:
        print(i, "is not in the list", lst)