def selection_sort(array):
    for i in range(len(array) - 1):
        minIdx = i
        for j in range(i+1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j
        if minIdx != i:
            array[minIdx], array[i] = array[i], array[minIdx]
    # O(n2)
    # best: n(no need to swap); worst: n2


def main():
    array = [5, 7, 4, 2, 8, 1]
    selection_sort(array)
    print(array)


main()
