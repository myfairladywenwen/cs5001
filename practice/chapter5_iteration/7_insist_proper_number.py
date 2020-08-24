print('method1:')
user_input = int(input('enter a number between 1-15:'))
times = 1
while user_input > 15 or user_input < 1:
    user_input = int(input('invalid, the right range is 1-15:'))
    times+=1
single_or_plural_time = 'time' if times== 1 else 'times'
print('you use', times, single_or_plural_time, 'to input a right number.')

print('method2:')
user_input= 0 #ensure the loop will start
times = 0
while user_input > 15 or user_input < 1:
    user_input = int(input('enter a number between 1-15:'))
    times+=1
single_or_plural_time = 'time' if times== 1 else 'times'
print('you use', times, single_or_plural_time, 'to input a right number.')