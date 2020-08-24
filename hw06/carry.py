def num_to_digit(n_string):
    '''This function takes in a number in string type and
    returns the corresponding list of consisting numbers.
    String -> List'''

    n_list = [int(x) for x in n_string]
    return n_list


def add_and_print(n1, n2):
    '''This function takes in two numbers in string type and
    add each digit up to get the addition of the two, and
    counts the time of carry over.
    Str, Str -> None'''

    mylist = []
    row1 = num_to_digit(n1)
    row2 = num_to_digit(n2)
    row1.reverse()    # add from last digit, so we need to reverse the list
    mylist.append(row1)
    row2.reverse()
    mylist.append(row2)

    len1 = len(row1)
    len2 = len(row2)
    # make up the rest digit with 0 for calculation
    if len1 != len2:
        edge = abs(len1 - len2)
        if len1 > len2:
            for _ in range(edge):
                mylist[1].append(0)
        else:
            for _ in range(edge):
                mylist[0].append(0)
    # add one empty digit for calculation of the last(highest) digit
    for i in range(2):
        mylist[i].append(0)
    length = len(mylist[0])

    carry = []          # initiate an empty row to count carry over
    result_row = []    # initiate an empty row to store sum of each digit
    for i in range(length):
        result = mylist[0][i] + mylist[1][i]
        if result >= 10:
            result = result - 10
            mylist[1][i+1] += 1
            carry.append(1)
        result_row.append(result)
    result_row.reverse()

    # deal with case that no carry over at the last addition
    if result_row[0] == 0:
        del result_row[0]

    mylist.append(result_row)
    mylist.append(carry)

    result_str = ''
    for item in mylist[2]:
        result_str += str(item)

    print(n1, '+', n2, '=', result_str)
    print('Number of carries:', str(len(mylist[3])))


def main():
    n1_str = input('Enter the first number: ')
    n2_str = input('Enter the second number: ')
    add_and_print(n1_str, n2_str)


main()
