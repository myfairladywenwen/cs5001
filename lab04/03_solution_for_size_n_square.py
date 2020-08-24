def main():
    '''
    This program validate the numblers user input from 1-9 with no duplicate
    to make up a magic square.
    '''
    n = int(input("enter the size of the square: "))
    print('enter the magic number: ')
    lst = []
    for i in range(n):
        lst_row = [x for x in input()]
        lst.append(lst_row)

    # make sum of row1 as the benchmark
    is_magic = True
    sum0 = 0
    for item in lst[0]:
        sum0 += int(item)

    # check horizonal
    i = 1
    while is_magic and i < n:
        sum = 0
        for item in lst[i]:
            sum += int(item)
        if sum0 != sum:
            is_magic = False
        else:
            i += 1

    if is_magic:
        ver_lst = []
        for j in range(n):
            ver_lst_col = []
            for i in range(n):
                ver_lst_col_item = lst[i][j]
                ver_lst_col.append(ver_lst_col_item)
            ver_lst.append(ver_lst_col)
            # print(ver_lst)
        i = 0
        while is_magic and i < n:
            sum_v = 0
            for item in ver_lst[i]:
                sum_v += int(item)
            if sum0 != sum_v:
                is_magic = False
            else:
                i += 1

    if is_magic:
        # check corner-to-corner diagonals
        left_diag = []
        i = 0
        for row in lst:
            item = row[i]
            left_diag.append(item)
            i += 1
        # print(left_diag)
        sum_l_d = 0
        for item in left_diag:
            sum_l_d += int(item)

        right_diag = []
        i = n - 1
        for row in lst:
            item = row[n-1]
            right_diag.append(item)
            i -= 1

        sum_r_d = 0
        for item in right_diag:
            sum_r_d += int(item)

        if sum0 == sum_l_d and sum0 == sum_r_d:
            is_magic = True
        else:
            is_magic = False

    if is_magic:
        print('This is a magic square!')
    else:
        print('Not a magic square!')


main()