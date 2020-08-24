from linked_list_node import Node


class LinkedList:
    def __init__(self, python_seq):
        # create a new linked list from a sequence
        if len(python_seq) == 0:
            self.first = None
            self.last = self.first
        else:
            node = Node(python_seq[0])
            self.first = node
            self.last = node
            for n in python_seq[1:]:
                self.extend(n)

    def __str__(self):
        # return a human-readable string for users
        return("linked_list("+str(self.first)+")")

    def __repr__(self):
        # return a detailed string for debugging
        return("linked_list("+repr(self.first)+")")

    def extend(self, value):
        """Add a value to the end of the list"""
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def insert(self, value):
        """Add a value to the beginning fo the list"""
        node = Node(value)
        node.next = self.first
        self.first = node
        if self.last is None:
            self.last = node

    def remove_last(self):
        """Remove and return the last value of the list"""
        node = self.remove_last_node(self.first)
        if node:
            return node.value
        else:
            return None
    
    def remove_last_node(self, node):
        if node is None:
            return None
        elif node.next is None:
            last = node
            self.first = None
            self.last = None
            return last
        elif node.next.next is None:
            node_to_remove = node.next
            node.next = None
            self.last = node
            return node_to_remove
        else:
            return self.remove_last_node(node.next)

    def contains(self, value):
        """Determine whether the list contains a value"""
        return self.search_node(self.first, value)

    def search_node(self, anode, value):
        if anode.value == value:
            return True
        elif anode.next:
            return self.search_node(anode.next, value)
        else:
            return False