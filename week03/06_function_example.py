def f1():
    print('i am func1')#side effect
    f2()
    return "i am an output value"

#f2() this will not work 
#f1() this will not work

def f2():
    print('i am func2')

# f1() #work
# print(f1())
# print("here is an output:" + f1())#work
print("here is an output:" + f2()) # not work
# print("here is an output:" + str(f2()))#work
