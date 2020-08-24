from queue import Queue
from stack import Stack


class WordLadder:
    """A class providing functionality to create word ladders"""

    def __init__(self, w1, w2, wordlist):
        self.word1 = w1
        self.word2 = w2
        self.valid_words_set = wordlist
        self.myqueue = Queue()
        self.mystack = Stack()
        self.word_visited_set = set()

    def make_ladder(self):
        if len(self.word1) != len(self.word2):
            return None
        else:
            self.mystack.push(self.word1)
            self.myqueue.enqueue(self.mystack)
            self.word_visited_set.add(self.word1)
            alpha_list = self.generate_alphe_list()
            while not self.myqueue.isEmpty():
                curr_stack = self.myqueue.dequeue()
                curr_word = curr_stack.peek()
                for i in range(len(curr_word)):
                    for letter in alpha_list:
                        new_word = curr_word[:i] + letter + curr_word[i+1:]
                        if (new_word in self.valid_words_set
                                and new_word not in self.word_visited_set):
                                self.word_visited_set.add(new_word)
                                new_stack = curr_stack.copy()
                                new_stack.push(new_word)
                                if new_word == self.word2:
                                    return new_stack
                                else:
                                    self.myqueue.enqueue(new_stack)
            return None

    def generate_alphe_list(self):
        alphe_list = []
        for each in range(ord('a'), ord('a')+26):
            alphe_list += [chr(each)]
        return alphe_list
