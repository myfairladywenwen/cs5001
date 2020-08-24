size= int(input('enter the size:'))
print("     ", end = '')
for column in range(1, size+1):
    print('{0:>4}'.format(column), end='')
print()
print("    +", end ='')
for column in range(1, size+1):
    print('----', end='')
print()

for row in range(1, size+1):
    print('{0:>3}'.format(row), ' |', sep = '', end = '')
    for column in range(1, size+1):
        product = row*column
        print('{0:>4}'.format(product), end = '')
    print()
print('finish')

    


    


#for row in range(1, size+1):
#    for column in range (1, size+1):
#        product = row*column
#        print('{0:>4}'.format(product), end = '')
#    print(end = '\n')

