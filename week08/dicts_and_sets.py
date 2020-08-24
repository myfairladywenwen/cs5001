my_fruit_counter = {}
my_fruit_counter["banana"] = 5
print(my_fruit_counter)
my_fruit_counter["fig"] = 1
my_fruit_counter["orange"] = 10
my_fruit_counter["apple"] = 3
print(my_fruit_counter)

print(my_fruit_counter.keys())
print(list(my_fruit_counter.keys()))
for fruit in my_fruit_counter.keys():
    print(fruit)
print(list(my_fruit_counter.keys())[0:2])
print(my_fruit_counter.values())
print(my_fruit_counter.items())

print(sorted(my_fruit_counter.values()))
print(sorted(my_fruit_counter.items()))

fruits_by_count = sorted(
    my_fruit_counter.items(),
    key=lambda x: x[1],
    reverse=True
)
print(fruits_by_count)

my_food_type = {
    'vegetable': [],
    'meat': [],
    'fruits': []
}

my_food_type['vegetable'].append('celery')
my_food_type['vegetable'].append('zucchini')
my_food_type['vegetable'].append('carrot')

print(my_food_type)

for food in my_food_type['vegetable']:
    print(food)
print("is equal to")
for i in range(len(my_food_type['vegetable'])):
    print(my_food_type['vegetable'][i])

for food in my_food_type['vegetable']:
    food = 'bubblegum'
    print(food)
print(my_food_type)    # original list not changed


for i in range(len(my_food_type['vegetable'])):
    my_food_type['vegetable'][i] = 'bubblegum'
    print(my_food_type['vegetable'][i])  # original list changed
print(my_food_type)


my_veg_set = set()

my_fruit_set = {'banana', 'fig', 'grapefruit'}


def check_for_fruit(fruit, fruit_set):
    if fruit in fruit_set:
        print('We have a', fruit)
    else:
        print('we do not have a', fruit)


check_for_fruit('banana', my_fruit_set)
check_for_fruit('peach', my_fruit_set)

my_fruit_set.add('peach')
check_for_fruit('peach', my_fruit_set)

my_fruit_set.remove('banana')
check_for_fruit('banana', my_fruit_set)