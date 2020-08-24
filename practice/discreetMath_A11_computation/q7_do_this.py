def do_this(userList, i, j):
    if (i > j):
        return
    m = (i + j)/2
    do_this(userList, i, m)
    do_this(userList, m+1, j)
    if userList[j] < userList[m]:
        swapPositions(userList, j, m)
    do_this(userList, i, j-1)


def swapPositions(alist, pos_a, pos_b):
    pair = (alist[pos_a], alist[pos_b])
    alist[pos_b], alist[pos_a] = pair
    return alist


A = [7, 4, 5, 3, 9, 2, 11]
do_this(A, 0, 6)