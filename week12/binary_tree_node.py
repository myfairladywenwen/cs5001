class Node:
    """A binary tree node"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Use __repr__ for more detailed debugging output
    def __repr__(self, indent=2):
        repr_string = "\n" + \
            " " * indent + " Node{\n" + \
            " " * indent + "  value: '" + self.value + "',\n" + \
            " " * indent + "  left: "
        if self.left is None:
            repr_string += self.left.__repr__() + "\n"
                                    # None 的 default __repr__
        else:
            repr_string += self.left.__repr__(indent + 2)
                                    # Node 的__repr__
        repr_string += " " * indent + "  right: "
        if self.right is None:
            repr_string += self.right.__repr__() + "\n"
        else:
            repr_string += self.right.__repr__(indent + 2)
        repr_string += " "*indent + "}\n"
        return repr_string

    def __str__(self):
        return (self.value +
                " (" + str(self.left) + ", " + str(self.right) + ")")