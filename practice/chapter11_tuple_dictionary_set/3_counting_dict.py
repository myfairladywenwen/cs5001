from sys import argv


def main():
    '''每个词出现次数'''

    if len(argv) < 2:
        print('no file name in command line')
    else:
        filename = argv[1]
        result = {}
        with open(filename, 'r') as f:
            for line in f:
                words_list = line.strip().split()
                for word in words_list:
                    if word not in result:
                        result[word] = 1
                    else:
                        result[word] += 1
    # for item in result.items():
    #     print(item)
    for a, b in result.items():
        print(a, b)


main()