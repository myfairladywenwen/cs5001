class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        return self.list.pop(0)

    def size(self):
        return len(self.list)

    def is_empty(self):
        return (self.size() == 0)
