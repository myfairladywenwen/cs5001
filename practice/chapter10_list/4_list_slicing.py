# print prefix and suffix
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# prefix
for i in range(0, len(lst)+1):
    print('<', lst[0:i], '>')
# suffix
for i in range(0, len(lst)+1):
    #print('<', lst[:len(lst)-i], '>')
    print('<', lst[i:len(lst)+1], '>')