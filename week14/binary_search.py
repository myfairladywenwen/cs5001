class BinS:

    """takes a value and a list,
    returns the index of the value if the value is found in the list,
    returns -1 if not, using the binary search algorithm."""

    @staticmethod
    def binary_search(array, value):
        if len(array) == 0:
            return -1
        else:
            low = 0
            high = len(array) - 1
            if low == high:
                if array[low] == value:
                    return low
                else:
                    return -1
            else:
                mid = int((low + high)/2)
                if array[mid] > value:
                    high = mid - 1
                    temp_array = array[low:high+1]
                    return (BinS.binary_search(temp_array, value))
                elif array[mid] == value:
                    return mid
                else:
                    low = mid + 1
                    temp_array = array[low:]
                    return (BinS.binary_search(temp_array, value))

    @staticmethod
    def binary_search_tr(x, lower, array):
        mid = len(array)//2
        if array[mid] == x:
            return lower + mid
        elif len(array) == 1:
            return -1
        elif array[mid] > x:
            return BinS.binary_search_tr(x, lower, array[:mid])
        else:
            return BinS.binary_search_tr(x, mid+1, array[mid+1:])
