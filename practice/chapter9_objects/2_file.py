f = open('3_file_test.py', 'r+')
f.write('data\n')
f.write('compute\n')
f.write('process\n')

for line in f:
    print(line.strip())

f.close()

g = open('4_content.py', 'a')
g.write('I write sth here to append in 4_content.py through obgject g')
g.close()

with open('4_content.py', 'w') as h:
    h.write('\n i write sth again, through h')


# g = open('4_content.py','w')
# h = open('3_file_test.py', 'r')
# read_string = h.read()
# print(read_string)
