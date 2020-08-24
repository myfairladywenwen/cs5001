from sys import argv


def main():
    '''相同字母个数的词放一起'''
    
    if len(argv) < 2:
        print('no file name in command line')
    else:
        filename = argv[1]
        result = {}
        with open(filename, 'r') as f:
            for line in f:
                words_list = line.strip().split()
                for word in words_list:
                    size = len(word)
                    if size in result:
                        if word not in result[size]:
                            # result[size] += [word] a list as the iterable obj
                            # result[size] += word就错了
                            # 会把 string 作为 iterable object
                            result[size].append(word)
                    else:
                        result[size] = [word]
        print(result)


main()