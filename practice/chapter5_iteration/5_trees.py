height = int(input('enter the height of the tree:'))
#method1
for row in range(1,height+1):
    for i in range(height-row):
        print(' ',sep='', end='')
    for j in range(2*row-1):
        print('*',sep='', end='')
    for i in range(height-row):#这两句没有意义，画空格干啥
        print(' ',sep='', end='')
    print()
#method2

row = 1
while row <= height:
    count = 0
    while count < height-row:
        print(' ', end ='')
        count+=1
    star = 0
    while star < 2*row -1:
        print('*', end ='')
        star+=1
    row+=1
    print()


