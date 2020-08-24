class Queue:
    def __init__(self):
        self.list1 = []
        self.list2 = []

    def enqueue(self, value):
        self.list1.append(value)

    def dequeue(self):
        if self.list1 != []:
            if self.list2 != []:
                return self.list2.pop()
            else:
                for _ in range(len(self.list1)-1):
                    self.list2.append(self.list1.pop())
                return self.list1.pop()
        else:
            if self.list2 != []:
                return self.list2.pop()


def main():
    my_queue = Queue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)

    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())

main()
