from queue_realize_stack import Stack


def main():
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.push(4)
    print(my_stack.pop())
    print(my_stack.pop())
    print(my_stack.pop())
    my_stack.push(5)
    print(my_stack.pop())


main()
