d = {}
d = {1: 'a', 2: 'b'}
print(d)
# d1 = dict('1'='a', '2'='b')    keyword can't be an expression
# print(d1)

d2 = dict(name = 'Gabby', age = 15)
print(d2)


d3 = dict.fromkeys([1,2,3],['a','b','c'])
print(d3)

second_value = d3.pop(2)
print(second_value)

last_pair = d3.popitem()
print(last_pair)

print(d3)
d3.clear()
# del d3
print(d3)

dishes = {'eggs': 3, 'bread': 5, 'bacon': 2}
keys = dishes.keys()
values = dishes.values()
item = dishes.items()
del dishes['eggs']
print(type(keys))
print(keys)
print(type(values))
print(values)
print(type(item))
print(item)
print(len(keys))
iter(keys)
print(keys)

newkeys = keys & {'bread', 'apple'}
print(keys)
print(newkeys)