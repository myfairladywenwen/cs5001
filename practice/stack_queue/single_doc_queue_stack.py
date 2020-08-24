class Stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, value):
        if (self.queue1 == [] and self.queue2 == []):
            self.queue1.append(value)
        elif (self.queue1 != [] and self.queue2 == []):
            self.queue1.append(value)
        elif (self.queue1 == [] and self.queue2 != []):
            self.queue2.append(value)

    def pop(self):
        if self.queue1 != []:
            if len(self.queue1) == 1:
                return self.queue1.pop()
            else:
                while len(self.queue1) != 1:
                    self.queue2.append(self.queue1.pop(0))
                return self.queue1.pop()
        else:
            if self.queue2 != []:
                if len(self.queue2) == 1:
                    return self.queue2.pop()
                else:
                    while len(self.queue2) > 1:
                        self.queue1.append(self.queue2.pop(0))
                    return self.queue2.pop()


my_stack = Stack()
for i in range(4):
    my_stack.push(i)
for i in range(2):
    print(my_stack.pop())
