def main():
    function_caller_args(f1, "hi there")
    function_caller(f2)
    function_caller(f3)
    function_caller(f3())

def function_caller(foodbar):
    print("I call a function")
    foodbar()

def function_caller_args(foodbar,argument):
    print("I call the function I got passed")
    foodbar(argument)

def f1(some_string):
    print("i am f1", "here is my argument", some_string)


def f2():
    print("i am f2")


def f3():
    def f4():
        print("i am f4")
    return f4
main()