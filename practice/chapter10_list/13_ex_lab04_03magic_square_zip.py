def main():
    '''
    This program validate the numblers user input from 1-9 with no duplicate
    to make up a magic square.
    '''
    n = int(input("enter the size of the square: "))
    print('enter the magic number: ')
    matrix = []
    for i in range(n):
        matrix.append(input())
    print('the horizonal way of matrix is', matrix)
    # make sum of row1 as the benchmark
    is_magic = True
    sum0 = 0
    for item in matrix[0]:
        sum0 += int(item)

    # check horizonal
    i = 1
    while is_magic and i < n:
        sum = 0
        for item in matrix[i]:
            sum += int(item)
        if sum0 != sum:
            is_magic = False
        else:
            i += 1

    if is_magic:
        # transpose the matrix
        matrix_trans = list(zip(*matrix))
        print('the vertical way of matrix is', matrix_trans)
        i = 0
        while is_magic and i < n:
            sum_v = 0
            for item in matrix_trans[i]:
                sum_v += int(item)
            if sum0 != sum_v:
                is_magic = False
            else:
                i += 1

    if is_magic:
        # check corner-to-corner diagonals
        left_diag = [matrix[i][i] for i in range(n)]
        print('left diag is ', left_diag)
        sum_l_d = 0
        for item in left_diag:
            sum_l_d += int(item)

        right_diag = [matrix[i][n-1-i] for i in range(n)]
        print('right diag is ', left_diag)
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