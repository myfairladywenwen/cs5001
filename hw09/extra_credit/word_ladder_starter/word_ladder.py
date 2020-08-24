from queue import Queue
from stack import Stack


class WordLadder:
    """A class providing functionality to create word ladders"""

    def __init__(self, w1, w2, wordlist):
        self.startword = w1
        self.endword = w2
        self.mydictionary = wordlist
        self.myqueue = Queue()
        self.mystack = Stack()
        self.word_exist_set = set()

    def make_ladder(self):
        ALPHE_LIST = ['a', 'b', 'c', 'd', 'e', 'f',
                      'g', 'h', 'i', 'j', 'k', 'l',
                      'm', 'n', 'o', 'p', 'q', 'r',
                      's', 't', 'u', 'v', 'w', 'x',
                      'y', 'z']
        self.mystack.push(self.startword)
        self.myqueue.enqueue(self.mystack)
        self.word_exist_set.add(self.startword)
        while not self.myqueue.isEmpty():
            current_stack = self.myqueue.dequeue()
            current_word = current_stack.peek()
            # change one digit
            for i in range(len(current_word)):
                for letter in ALPHE_LIST:
                    new_word = current_word[:i] + letter + current_word[i+1:]
                    if (new_word in self.mydictionary[len(new_word)] and
                            new_word not in self.word_exist_set):
                        self.word_exist_set.add(new_word)
                        new_stack = current_stack.copy()
                        new_stack.push(new_word)
                        if new_word == self.endword:
                            return new_stack
                        else:
                            self.myqueue.enqueue(new_stack)
            # add one digit
            for i in range(len(current_word)+1):
                for letter in ALPHE_LIST:
                    new_word = current_word[:i] + letter + current_word[i:]
                    if len(new_word) in self.mydictionary.keys():
                        if (new_word in self.mydictionary[len(new_word)] and
                                new_word not in self.word_exist_set):
                            self.word_exist_set.add(new_word)
                            new_stack = current_stack.copy()
                            new_stack.push(new_word)
                            if new_word == self.endword:
                                return new_stack
                            else:
                                self.myqueue.enqueue(new_stack)
            # delete one digit
            for i in range(len(current_word)):
                new_word = current_word.replace(current_word[i], "", 1)
                if len(new_word) in self.mydictionary.keys():
                    if (new_word in self.mydictionary[len(new_word)] and
                            new_word not in self.word_exist_set):
                        self.word_exist_set.add(new_word)
                        new_stack = current_stack.copy()
                        new_stack.push(new_word)
                        if new_word == self.endword:
                            return new_stack
                        else:
                            self.myqueue.enqueue(new_stack)
        return None
