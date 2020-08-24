from random import randrange, seed
seed(23)
for i in range(0,10):
    print(randrange(1,100),end=' ')
print()

print('showing dice')
for round in range(0,3):
    result = randrange(1,7)
    if result == 1:
        print('*')
    elif result == 2:
        print('**')
    elif result == 3:
        print('***')
    elif result == 4:
        print('****')
    elif result == 5:
        print('*****')
    elif result == 6:
        print('******')


