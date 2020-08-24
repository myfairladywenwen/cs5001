v = "This v is a global variable"

def main():
    f1()
    f2()

def f1():
    # v = "this v is local to f1"
    global v
    v = "this global v has been monkeyed with by f1"
    x = "A variable in f1"
    print(x)
    print(v)

def f2():
    # print(x)  # error
    x = "A variable in f2"
    print(x)
    print(v)

main()