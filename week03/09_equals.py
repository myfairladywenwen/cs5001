a = "hello wild world"[0:5]
b = "hello wiggly world"[0:5]

print(a)
print(b)
# a==b 吗？都是 hello
# a is b 吗？是两个完全不同的 object！！！
if (a==b):
    print ('the strings are same')
    #会 output 这行，因为==不看 deep truth
else:
    print('the strings are not same')

if (a is b):
     print ('the strings are REALLY same')
else:
    print('the strings are not REALLY same')
    #会 output 这行，因为is看deep truth：是不是same objects!!!

if (a is "hello"):
    print("A is helo")
else:
    print("it is not true")#会output这行，因为is看deep truth：是不是same objects!!!

if (a == "hello"):
    print("A == helo")#会output这行，因为==不看deep truth
else:
    print("it is not true by ==")

a = b
if (a is b):
    print("REALLY same") #会output这行，a和b是同一个obj了
else:
    print("not same object")

c = "Hello"
d = "Hello"
if (c is d):
    print("REALLY same") 
    #会output这行，当 create a string, python checks if this obj是否存在，如果存在，c和d是同一个obj
    #和前面的不同，前面的是从 string 里 slice 出来的，python 认为不是同一个
else:
    print("not same object")

c = ''.join(d)
if (c is d):
    print("REALLY same") 
else:
    print("not same object")#会out这行

two1 = '22'
two2 = "22"
print(two1)
print(two2)


