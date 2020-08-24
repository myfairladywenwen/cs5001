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
    # this way 不 work:
    # lst =[[]] * 3 
    # 这里有坑：这三个都 refer to 一个 list，如果 append 就会全 append 过来
    # for i in range(3):
    #     lst_row = [x for x in input()]
    #     lst[i] = lst_row
    #     lst += lst[i] 
    # print(lst)
    # [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
    #  '1', '2', '3', '4', '5', '6', '7', '8', '9']

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
    # check vertical
    # ver_lst = []
    # ver_lst_col = []
    # for j in range(n):
    #     for i in range (n):
    #         ver_lst_item = lst[i][j]
    #         ver_lst_col.append(ver_lst_item)
    #     ver_lst.append(ver_lst_col)
    # 这个是错的，每次都往lst_col里 append，
    # ver_lst随着变，重复 n次----为什么 ver_lst会跟着变呢？
    # ----因为
    # [['1', '1', '1', '2', '2', '2', '3', '3', '3'], 
    # ['1', '1', '1', '2', '2', '2', '3', '3', '3', ],
    # ['1', '1', '1', '2', '2', '2', '3', '3', '3', ],
    # ['1', '1', '1', '2', '2', '2', '3', '3', '3', ]]

    # for j in range(n):
    #     for i in range (n):
    #         ver_lst_item = lst[i][j]
    #         ver_lst_col.append(ver_lst_item)
    # ver_lst.append(ver_lst_col)
    # 这个也不对，成一维的list 了----
    # 应该把ver_lst_col = []放在循环里才可以每次新建一个list
    # [['1', '1', '1', '2', '2', '2', '3', '3', '3']]

        ver_lst = []
        for j in range(n):
            ver_lst_col = []
            for i in range (n):
                ver_lst_col_item = lst[i][j]
                ver_lst_col.append(ver_lst_col_item)
            ver_lst.append(ver_lst_col)
    #print(ver_lst)
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
         
    if  is_magic == True:
        print('This is a magic square!')
    else:
         print('Not a magic square!')

        
main()