class LinearS:
    """takes a value and a list,
    returns the index of the value if the value is found in the list,
    and returns -1 if not, using the linear search algorithm"""

    @staticmethod
    def linera_search(array, value):
        if len(array) == 0:
            return -1
        elif len(array) == 1:
            if array[0] == value:
                return 0
            else:
                return -1
        else:
            if array[0] == value:
                return 0
            else:
                if LinearS.linera_search(array[1:], value) == -1:
                    return -1
                else:
                    return LinearS.linera_search(array[1:], value) + 1

    @staticmethod
    def linera_search_tr(key, start, array):
        if array[start] == key:
            return start
        else:
            start += 1
            return LinearS.linera_search_tr(key, start, array)