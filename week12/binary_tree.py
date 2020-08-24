from binary_tree_node import Node


class BinaryTree:
    def __init__(self, val):
        self.root = Node(val)

    def __str__(self):
        return "BinTree(" + str(self.root) + ")"

    def __repr__(self):
        return "BinTree:\n{" + repr(self.root) + "}"

    def add_val_l(self, val):  
        '''put a new node on the left and fill it up with a val'''
        n = Node(val)  # 这里只是新建了一个 node,还需要把它和原来的树连起来
        self.add_node_l(self.root, n)

    def add_node_l(self, current_node, new_node):
        if (current_node.left is None):
            current_node.left = new_node
        elif (current_node.right is None):
            current_node.right = new_node
        else:
            self.add_node_l(current_node.left, new_node)

    def add_val_r(self, val):
        n = Node(val)
        self.add_node_r(self.root, n)

    def add_node_r(self, current_node, new_node):
        if (current_node.right is None):
            current_node.right = new_node
        elif (current_node.left is None):
            current_node.left = new_node
        else:
            self.add_node_r(current_node.right, new_node)

    def contains(self, value):
        return self.contains_node(self.root, value)

    def contains_node(self, root, value):
        if root.value == value:
            return True
        else:
            if root.left:
                if self.contains_node(root.left, value):
                    return True
            if root.right:
                if self.contains_node(root.right, value):
                    return True
        return False
        # 其实不用写这行，因为如果都没有 return true，会 return None-->false
