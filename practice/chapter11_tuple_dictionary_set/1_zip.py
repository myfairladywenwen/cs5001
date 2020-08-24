def gen(n):
    for i in range(n):
        yield i*2 # this generator is shorter than the list
for p in zip([10, 20, 30, 40, 50, 60],gen(4)):
    print(p, end ='')
