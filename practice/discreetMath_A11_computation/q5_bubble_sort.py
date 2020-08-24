def main():
    lista = [7, 6, 6, 5, 4, 9, 2, 1]
    for i in range(len(lista)):
        for j in range(1, len(lista)-i):  # no need to go through the entire list
            if lista[j-1] > lista[j]:
                lista = swapPositions(lista, j-1, j)
    print(lista)


def swapPositions(alist, pos_a, pos_b):
    pair = (alist[pos_a], alist[pos_b])
    alist[pos_b], alist[pos_a] = pair
    return alist

main()