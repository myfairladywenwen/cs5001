from stack import Stack


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if not self.stack1.is_empty():
            if not self.stack2.is_empty():
                return self.stack2.pop()
            else:
                for _ in range(self.stack1.size()-1):
                    self.stack2.push(self.stack1.pop())
                return self.stack1.pop()
        else:
            if not self.stack2.is_empty():
                return self.stack2.pop()
