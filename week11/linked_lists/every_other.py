import sys
from linked_list import LinkedList


def every_other(linked_list):
    every_other_list = LinkedList("")
    return every_other_node(every_other_list, linked_list.first)
    #相当于往一个空的 list 里面加every other node 形成一个新的 list


def every_other_node(every_other_list, node):
    if node:
        every_other_list.extend(node.value)
        if (node.next is not None and
           node.next.next is not None):
            return every_other_node(every_other_list, node.next.next)
        else:
            return every_other_list
    else:
        return every_other_list


def main():
    linked_list = LinkedList(sys.argv[1])
    print(every_other(linked_list))


main()
