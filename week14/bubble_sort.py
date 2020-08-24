class BubbleS:
    """ takes a list,
    returns a list of the same elements, sorted."""

    @staticmethod
    def bubble_sort1(array, left_to_figure):
        if left_to_figure == 0:
            return
        else:
            # put the max at the end, i.e., idx = to_do_len -1
            BubbleS.put_max_to_end1(array, 0, left_to_figure)
            BubbleS.bubble_sort1(array, left_to_figure - 1)

    @staticmethod
    def put_max_to_end1(array, start, end):
        BubbleS.swapping1(array, start, end)

    @staticmethod
    def swapping1(array, start, end):
        if start == end:
            return
        else:
            if array[start] > array[start+1]:
                array[start], array[start+1] = array[start+1], array[start]
            # start += 1
            BubbleS.swapping1(array, start+1, end)

    @staticmethod
    def bubble_sort2(array, count_max):
        if count_max == len(array) - 1:
            return
        else:
            BubbleS.find_max2(array, 0, len(array)-count_max-1)
            #  指定一个区间去 find_max
            BubbleS.bubble_sort2(array, count_max+1)

    @staticmethod
    def find_max2(array, start, end):
        BubbleS.swapping2(array, start, end)

    @staticmethod
    def swapping2(array, start, end):
        if start == end:
            return
        else:
            if array[start] > array[start+1]:
                array[start], array[start+1] = array[start+1], array[start]
            BubbleS.swapping2(array, start+1, end)

    @staticmethod
    def bubble_sort3(array, times):
        if len(array) <= 1:
            return array
        else:
            if times == len(array) - 1:
                return array
            else:
                return BubbleS.bubble_sort_helper(array, 1, times)

    @staticmethod
    def bubble_sort_helper(array, start, times):
        if array[start-1] > array[start]:
            array[start-1], array[start] = array[start], array[start-1]
        if start < len(array)-1:
            return BubbleS.bubble_sort_helper(array, start+1, times)
        else:
            return BubbleS.bubble_sort3(array, times+1)
