from stack_realize_queue import Queue


my_queue = Queue()
for i in range(4):
    my_queue.enqueue(i)

for i in range(2):
    print(my_queue.dequeue())

