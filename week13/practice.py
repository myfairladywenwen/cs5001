def main():
    my_array = [5, 3, 4, 6, 2, 7]
    bubble_sort_practice(my_array)


def bubble_sort_practice(mylist):
        """Sort a list of numbers using bubble sort"""
        # Each iteration of this outer for-loop puts *at least* one element into its
        # proper place. Thus, at most n iterations must be executed to sort the array
        # I.e., it's possible for the array to be sorted in fewer than n iterations
        for i in range(len(mylist)):
            swapped = False
            for j in range(1, len(mylist) - i):
                if mylist[j-1] > mylist[j]:
                    mylist[j-1], mylist[j] = mylist[j], mylist[j-1]
                    swapped = True
        print(mylist)
        if not swapped:
            return

main()