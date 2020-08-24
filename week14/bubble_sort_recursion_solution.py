def bubble_sort(l):
    """Recursive bubble sort"""
    # bubble_out = bubble(False, l) # non-tail recursive
    bubble_out = bubble_tr(l, len(l), [], False)  # tail recursive
    if not bubble_out[0]:  # if not false, i.e.,没有 swap 过
        return l
    else:
        return bubble_sort(bubble_out[1])


# a single iteration of bubble sort (head recursive)
def bubble(b, l):
    """Recursive bubble sort pass"""
    swapped = False
    if len(l) <= 1:
        return (swapped or b), l
    if l[0] > l[1]:
        swapped = True
        l[0], l[1] = l[1], l[0]
    bubble_out = bubble(swapped or b, l[1:])  # recursive call
    return bubble_out[0], [l[0]] + bubble_out[1]  # concatenation operation


# run a bubble sort on a list (tail recursive)
def bubble_tr(l, l_len, result, swapped):
    """Recursive bubble sort pass using tail recursion"""
    if (len(result) == l_len):
        return (swapped, result)
    else:
        if (len(result) == 0 or l[0] > result[-1]):
            result += [(l[0])]  # append
            return bubble_tr(l[1:], l_len, result, swapped)  # recursive call
        else:
            temp = result[-1]
            result[-1] = l[0]
            result += [temp]   # append
            return bubble_tr(l[1:], l_len, result, True)  # recursive call
            # 只有进入到 else，才会被 swap 过，更新为 True


print("Bubble sort")
print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([5, 4, 3, 1, 2]))
