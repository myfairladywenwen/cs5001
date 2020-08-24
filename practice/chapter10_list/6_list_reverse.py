lst = [1, 2, 3]
lst.extend([4,5,6])
print(lst)
lst.reverse()
print(lst)#[6,5,4,3,2,1] 
lst2 = reversed(lst)
for i in lst2:
    print(lst[i-1])  # print(lst[i])就会少一个 6
#也可以:
for i in reversed(lst):
    print(lst[i-1])