ENTREES = 5
print('enter '+ str(ENTREES) +' numbers:')
sum = 0.0
numbers = []
for i in range (1, ENTREES+1):
    number = float(input('enter number' + str(i) + ' : '))
    numbers += [number]
    sum += number
print(end= 'number entered: ')

for number in numbers:
    print(number, end=" ")
print()
print("avg = " , sum/ENTREES)