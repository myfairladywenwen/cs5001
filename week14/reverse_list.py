class Reverse:
    """takes a list and returns a list with the elements reversed"""

    @staticmethod
    def rev_list(array):
        # if len(array) == 0:
        #     return
        if len(array) <= 1:
            return array
        else:
            return Reverse.rev_list(array[1:]) + [array[0]]

    @staticmethod
    def rev_list_tr(array, output, length):
        # output starts from []
        start = 0
        if length == len(output):
            return output
        else:
            # return Reverse.rev_list_tr(array[1:], [array[0]] + output, start+1)
            # putting the element in front of our reversed list so far
            output = [array[start]] + output
            return Reverse.rev_list_tr(array[start+1:], output, length)
