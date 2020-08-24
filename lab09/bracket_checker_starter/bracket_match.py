from stack import Stack


class BracketMatch:
    """Class for evaluating parenthetical strings"""

    def __init__(self):
        self.mystack = Stack()

    def brackets_match(self, line):
        result = True
        for char in line:
            if char != ")" and char != "]" and char != "}":
                self.mystack.push(char)
            else:
                if len(self.mystack.items) == 0:
                    result = False
                    break
                else:
                    while (self.mystack.peek() != "("
                            and self.mystack.peek() != "["
                            and self.mystack.peek() != "{"
                            and len(self.mystack.items) != 0):
                        pop_item = self.mystack.pop()
                    if self.mystack.peek() == "(" and char == ")":
                        pop_item = self.mystack.pop()
                    elif self.mystack.peek() == "[" and char == "]":
                        pop_item = self.mystack.pop()
                    elif self.mystack.peek() == "{" and char == "}":
                        pop_item = self.mystack.pop()
                    else:
                        result = False
                        break
        # all chars have been gone through and still not detected false
        if result is True:
            if len(self.mystack.items) == 0:
                result = True
        # for the case of leaving alphe-num chars in stack
            else:
                while len(self.mystack.items) != 0:
                    pop_item = self.mystack.pop()
                    if (pop_item == "(" or pop_item == "["
                            or pop_item == "{"):
                        result = False
                        break
                    result = True

        # clear the stack
        while len(self.mystack.items) != 0:
            pop_item = self.mystack.pop()

        return result
