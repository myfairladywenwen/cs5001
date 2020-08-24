from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def __init__(self):
        self.mystack = Stack()

    def process_string(self, input_string):
        solution_string = ""
        for char in input_string:
            if char != "*" and char != "^":
                self.mystack.push(char)
            elif char == "*":
                if len(self.mystack.items) == 0:
                    break
                else:
                    solution_string += self.mystack.pop()
            elif char == "^":
                if len(self.mystack.items) < 2:
                    break
                else:
                    for _ in range(2):
                            solution_string += self.mystack.pop()
        # clear the stack
        while len(self.mystack.items) != 0:
            _ = self.mystack.pop()

        return solution_string
