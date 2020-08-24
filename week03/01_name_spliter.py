fullname = input('input your name: ')
name_break = fullname.rfind(' ')

first_and_middle = fullname[: name_break]
last = fullname[name_break+1:]
print('your name in last-name first format:')
print(last + ', ' + first_and_middle)
