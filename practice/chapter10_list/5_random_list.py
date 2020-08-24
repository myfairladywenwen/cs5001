from random import randint
# build a list of n random numbers in range 0~99


def random_list(n):
    lst = []
    for count in range(n):
        value = randint(0, 99)
        lst += [value]
        # lst[count] = randint(0,99)是 out of range
        # 因为最开始是 empty list，没法 lst【0】
        # lst += [lst[count]]
    return lst


def main():
    num_of_item = int(input('how many items would you like in the list: '))
    the_lst = random_list(num_of_item)
    print(the_lst)

main()