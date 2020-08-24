class Add:
    """takes a list of numbers and returns the sum of the numbers"""

    @staticmethod
    def add_list(array):
        if len(array) == 0:
            return 0
        if len(array) == 1:
            return array[0]
        else:
            return array[0] + Add.add_list(array[1:])

    @staticmethod
    def add_list_tr(l, ind, total):
        # ind is the number of times we have done the addition,
        # i.e., where we are at the list now
        if (len(l) == ind):  # 每一个都加过了
            return total
        else:
            total += l[ind]  # 之前的 total + 当前的 idx
            return Add.add_list_tr(l, ind+1, total)
