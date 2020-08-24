from queue import Queue


class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, value):
        if self.queue1.is_empty() and self.queue2.is_empty():
            self.queue1.enqueue(value)
        elif not self.queue1.is_empty() and self.queue2.is_empty():
            self.queue1.enqueue(value)
        elif self.queue1.is_empty() and not self.queue2.is_empty():
            self.queue2.enqueue(value)
# 不会两个都不空的，因为出栈的操作能够保证肯定至少有一个 queue 是空的

    def pop(self):
        if not self.queue1.is_empty():
            if self.queue1.size() == 1:
                return self.queue1.dequeue()
            else:
                while self.queue1.size() > 1:
                    self.queue2.enqueue(self.queue1.dequeue())
                return self.queue1.dequeue()
        else:
            if not self.queue2.is_empty():
                if self.queue2.size() == 1:
                    return self.queue2.dequeue()
                else:
                    while self.queue2.size() > 1:
                        self.queue1.enqueue(self.queue2.dequeue())
                    return self.queue2.dequeue()
