def bubble_sort(array):
    for i in range(len(array) - 1):
        swapped = False
        for j in range(i+1, len(array) - i):
            # j does not need to reach len(array) -1,
            # since the tail has been sorted
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swapped = True
        if swapped is False:
            # if no swapping happened, means all has been sorted
            return
    # O(n2)
    # best: O(n); worst:O(n^2); avg:O(n^2)

def main():
    array = [5, 7, 4, 2, 8, 1]
    bubble_sort(array)
    print(array)


main()
