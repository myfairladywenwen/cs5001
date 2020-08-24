from linked_list import LinkedList
from node import Node


def main():
    my_lklist = LinkedList()
    my_lklist.head = Node(1)
    my_lklist.head.nextp = Node(2)
    my_lklist.head.nextp.nextp = Node(3)

    my_lklist.print_list()
    print()
    my_lklist.insert_at_front(0)
    my_lklist.print_list()
    print()
    my_lklist.append(4)
    my_lklist.print_list()
    print()
    result = my_lklist.search(4)
    if result:
            print('exist', 4)
    else:
        print('not exist', 4)
    result = my_lklist.search(5)
    if result:
            print('exist', 5)
    else:
        print('not exist', 5)
    print()
    my_lklist.index(4)
    my_lklist.index(5)
    print()

    my_lklist.insert(0, -1)
    my_lklist.print_list()
    print()
    my_lklist.insert(2, 1.5)
    my_lklist.print_list()
    print()

    my_lklist.remove(-1)
    my_lklist.print_list()
    print()
    my_lklist.remove(1.5)
    my_lklist.print_list()
    print()
    my_lklist.reverse1()
    print("using reverse1: ", end='')
    my_lklist.print_list()
    print()

    # print(my_lklist)
    # new_head = my_lklist.reverse2(my_lklist.head)
    # print("using reverse2: ", end='')
    # # my_lklist.print_list()
    # print()
    # p = new_head
    # while p is not None:
    #     print(p.value, end=' ')
    #     p = p.nextp

    my_lklist.reverse3()
    print("using reverse3: ", end='')
    my_lklist.print_list()
    print()

    my_lklist.reverse4()
    print("using reverse4: ", end='')
    my_lklist.print_list()


main()