from add_list import Add
from reverse_list import Reverse
from linear_search import LinearS
from binary_search import BinS
from bubble_sort import BubbleS


def main():
    demo_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # result1_1 = Add.add_list(demo_list)
    # print("result of add list is:", result1_1)
    # result1_2 = Add.add_list_tr(demo_list, 0, 0)
    # print("using tail recursion, result of add list is:", result1_2)

    # result2 = Reverse.rev_list(demo_list)
    # print("the reversed list is:", result2)
    result2_2 = Reverse.rev_list_tr(demo_list, [], 9)
    print("using tail recursion, the reversed list is:", result2_2)

    # result3 = LinearS.linera_search(demo_list, 5)
    # print("index of 5 is:", result3)
    # result3_2 = LinearS.linera_search(demo_list, 5)
    # print("using tail recursion, index of 5 is:", result3_2)
    # result3_3 = LinearS.linera_search(demo_list, 0)
    # print("using tail recursion, index of 0 is:", result3_3)
    # result3_4 = LinearS.linera_search(demo_list, -1)
    # print("index of -1 is:", result3_4)

    # result4_1 = BinS.binary_search(demo_list, 5)
    # print("index of 5 is:", result4_1)
    # result4_2 = BinS.binary_search_tr(5, 0, demo_list)
    # print("index of 5 is:", result4_2)

    # new_list = [4, 6, 8, 2, 1, 5, 3]
    # # BubbleS.bubble_sort1(new_list, 6)
    # # print("using method1, sorted new list is:", new_list)
    # BubbleS.bubble_sort2(new_list, 0)
    # print("using method2, sorted new list is:", new_list)


main()
