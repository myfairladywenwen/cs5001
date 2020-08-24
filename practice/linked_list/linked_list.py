from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        p = self.head
        while p is not None:
            print(p.value, ' ', end='')
            p = p.nextp

    def size(self):
        counter = 0
        p = self.head
        while p is not None:
            counter += 1
            p = p.nextp
        return counter

    def is_empty(self):
        return self.size() == 0

    def insert_at_front(self, value):
        newNode = Node(value)
        newNode.nextp = self.head
        self.head = newNode

    def append(self, value):
        newNode = Node(value)
        if self.is_empty():
            self.head = newNode
        else:
            p = self.head
            while p.nextp is not None:
                p = p.nextp
            p.nextp = newNode

    def search(self, value):
        p = self.head
        while p is not None:
            if p.value == value:
                return True
            else:
                p = p.nextp
        return False

    def index(self, value):
        idx = 0
        p = self.head
        while p is not None:
            if p.value == value:
                print('value is at', str(idx))
                return
            else:
                p = p.nextp
                idx += 1
        print("not found")

    def insert(self, pos, value):
        if pos == 0:
            self.insert_at_front(value)
        elif pos > self.size():
            self.append(value)
        else:
            temp = Node(value)
            prev = None
            p = self.head
            count = 0
            while count < pos:
                prev = p
                p = p.nextp
                count += 1
            prev.nextp = temp
            temp.nextp = p

    def remove(self, value):
        if self.search(value):
            if self.head.value == value:
                self.head = self.head.nextp
                return
            else:
                pre = self.head
                p = pre.nextp
                while p is not None:
                    if p.value == value:
                        pre.nextp = p.nextp
                        return
                    else:
                        pre = p
                        p = p.nextp

    def reverse1(self):
        if self.head is None or self.head.nextp is None:
            return
        else:
            dummy = Node()
            dummy.nextp = self.head
            pre = dummy.nextp
            p = pre.nextp
            while p is not None:
                pre.nextp = p.nextp
                p.nextp = dummy.nextp
                dummy.nextp = p
                p = pre.nextp
            self.head = dummy.nextp

    # def reverse2(self, head):
    #     if head is None or head.nextp is None:
    #         return head
    #     else:
    #         new_head = self.reverse2(head.nextp)
    #         head.nextp.nextp = head
    #         head.nextp = None
    #         return new_head

    def reverse3(self):
        pre = self.head
        temp = pre.nextp
        self.head.nextp = None
        while (temp is not None):
            r = temp.nextp
            temp.nextp = pre
            pre = temp
            temp = r
        self.head = pre

    def reverse4(self):
        pre = self.head.nextp
        while (pre.nextp is not None):
            temp = pre.nextp
            pre.nextp = temp.nextp
            # temp.nextp = pre
            temp.nextp = self.head.nextp
            self.head.nextp = temp
        pre.nextp = self.head
        self.head = self.head.nextp
        pre.nextp.nextp = None

