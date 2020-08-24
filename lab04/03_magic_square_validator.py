def main():
    '''
    This program validate the numblers user input
    between 1 and 9 (without duplicates) make up a magic square.
    '''
    print("Enter a magic number")
    lst = []
    for i in range(3):
        lst_row = [x for x in input()]
        lst.append(lst_row)
    # make sum of row1 as the benchmark
    is_magic = True
    sum0 = 0
    for item in lst[0]:
        sum0 += int(item)  
    # check horizonal
    i = 1
    while (is_magic and i <= 2):
        sum = 0
        for item in lst[i]:
            sum += int(item)
        if sum0 != sum:
            is_magic = False
        else:
            i += 1

    if is_magic:
        # check vertical
        vertical_lst = list(zip(lst[0], lst[1], lst[2]))
        i = 0
        while (is_magic and i <= 2):
            sum = 0
            for item in vertical_lst[i]:
                sum += int(item)
            if sum0 != sum:
                is_magic = False
            else:
                i += 1

    if is_magic:
        # check corner-to-corner diagonals
        if sum0 == int(lst[0][0]) + int(lst[2][2]) + int(lst[1][1]): 
            if sum0 == int(lst[0][2]) + int(lst[2][0])+ int(lst[1][1]):
                is_magic = True
        else:
            is_magic = False
    # output the result
    if is_magic:
        print('This is a magic square!')
    else:
        print('Not a magic square!')

        
main()