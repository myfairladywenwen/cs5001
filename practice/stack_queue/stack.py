class Stack:
    def __init__(self):
        self.stacklist = []

    def push(self, value):
        self.stacklist.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stacklist.pop()

    def size(self):
        return len(self.stacklist)

    def is_empty(self):
        if len(self.stacklist) == 0:
            return True
        else:
            return False
