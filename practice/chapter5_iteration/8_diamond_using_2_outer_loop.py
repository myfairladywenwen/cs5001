height = 7
for row in range(0, int(height/2) + 1):
    print(' ' * int((height - (2*row + 1))/2), end='')
    print('*' * (2*row + 1))
for row in range(0, int(height/2)):
    print(' ' * (row+1), end='')
    print('*' * (height-(2*(row+1))))