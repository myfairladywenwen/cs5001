from linked_list import LinkedList


def main():
    my_linked_list = LinkedList(['A'])
    my_linked_list.extend('B')
    my_linked_list.extend('C')

    print("List contains B:", my_linked_list.contains('B'))
    print("List contains M:", my_linked_list.contains('M'))

    print("Here's the list as a string\n")
    print(my_linked_list)

    print("Here's the list as a repr string\n")
    print(repr(my_linked_list))

    my_linked_list2 = LinkedList("A string will work")
    print(my_linked_list2)

    my_ll3 = LinkedList([])
    my_ll3.insert('A')
    print(my_ll3)


main()