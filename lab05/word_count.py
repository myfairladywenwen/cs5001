import re


def main():
    '''read the file that user input directs,
    count the words,
    non-whitespace characters (including punctuation),
    and alphanumeric characters (letters and numbers, excluding punctuation)
    None -> None'''
    filename = input('Enter the file name: ')
    try:
        myfile = open(filename, 'r')
    except:
        print('Can\'t open', filename)
        return
    word_count = 0
    char_count = 0
    alph_num_count = 0
    for line in myfile:
        if line != "\n":
            whole_line_str = line.strip()
            word_list = whole_line_str.split(' ')
            word_count += len(word_list)

            for word in word_list:
                word_len = len(word)
                char_count += word_len

            alph_num_lst = re.findall(r"\w", whole_line_str)
            alph_num_count_line = len(alph_num_lst)
            alph_num_count += alph_num_count_line

    print('Words:', word_count)
    print('Characters:', char_count)
    print('Letters & numbers:', alph_num_count)


main()
