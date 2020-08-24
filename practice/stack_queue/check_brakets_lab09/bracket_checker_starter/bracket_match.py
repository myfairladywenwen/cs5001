from stack import Stack


class BracketMatch:
    """Class for evaluating parenthetical strings
    和 lab 做法不同在于，如果是字母或者数字，其实不用入栈，不做处理即可"""

    def __init__(self):
        self.mystack = Stack()

    def brackets_match(self, line):
        result = True
        for char in line:
            if char == "(" or char == "[" or char == "{":
                self.mystack.push(char)
            elif char == ")" or char == "]" or char == "}":
                current_char = self.mystack.peek()
                if not self.match_pair(current_char, char):
                    result = False
                    break
                self.mystack.pop()

        if result is True:
            if len(self.mystack.items) != 0:
                result = False
                # clear the stack
                while len(self.mystack.items) != 0:
                    self.mystack.pop()
        return result

    def match_pair(self, char1, char2):
        if ((char1 == "(" and char2 == ")")
            or (char1 == "[" and char2 == "]")
                or (char1 == "{" and char2 == "}")):
                return True
        else:
            return False
