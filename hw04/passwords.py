import random
SYMBOLS = '@#$%^&*'
USERNAME_MIDPART_LEN = 7
ORIGIN_A = 'a'
SIMI_A = '@'
ORIGIN_O = 'o'
SIMI_O = '0'
ORIGIN_L = 'l'
SIMI_L = '1'
ORIGIN_S = 's'
SIMI_S = '$'


def main():
    '''
    This program generate username and password for the user
    according to the infomation they provide and the naming rules.
    '''
    # prompt for user input of their related infomation
    print("Welcome to the username and password generator!")
    first_name = input("Please enter your first name: \n")
    last_name = input("Please enter your last name: \n")
    f_word = input("I also need one of your favorite word: \n")

    # generate the user name, following the rule of:
    # the first letter of the user's first name,followed by
    # first 7 letters of the usee's last name (if last name shorter than 7,
    # random symbols from @#$%^&* will make up the spot, selected randomly),
    # followed by random integer between 0 and 99
    # letters in the username should all be lower case

    first_name_lower = first_name.lower()
    last_name_lower = last_name.lower()
    first_letter_lower = first_name[0].lower()
    # generate the 7 letters:
    if len(last_name_lower) < USERNAME_MIDPART_LEN:
        symbols = ''
        for _ in range(USERNAME_MIDPART_LEN):
            symbols += random.choice(SYMBOLS)
        symbol_lst = list(symbol for symbol in symbols)
        for i in range(len(last_name_lower)):
            symbol_lst[i] = last_name_lower[i]
        symbol_str = ''
        for i in range(USERNAME_MIDPART_LEN):
            symbol_str += symbol_lst[i]
    else:
        symbol_str = ''
        symbol_str = last_name_lower[:7]
    number_digit = random.randint(0, 99)
    user_name = first_letter_lower + symbol_str + str(number_digit)
    print("Thanks", first_name, "your user name is", user_name)
    print()
    print("Here are three suggested passwords for you to consider: ")
    print()

    # generate first password
    # the concatenation of the user's first and last names, in lower case,
    # with a random integer in the range 0 – 99 between them.
    # Some of the characters in the resulting string are then replaced by
    # similar-looking digits and punctuation characters
    # All a characters should be replaced by @, o by 0, l by 1, and s by $.
    first_name_simi = first_name_lower
    for char in first_name:
        if char == ORIGIN_A:
            first_name_simi = first_name_simi.replace(char, SIMI_A)
        elif char == ORIGIN_O:
            first_name_simi = first_name_simi.replace(char, SIMI_O)
        elif char == ORIGIN_L:
            first_name_simi = first_name_simi.replace(char, SIMI_L)
        elif char == ORIGIN_S:
            first_name_simi = first_name_simi.replace(char, SIMI_S)
    last_name_simi = last_name_lower
    for char in last_name_lower:
        if char == ORIGIN_A:
            last_name_simi = last_name_simi.replace(char, SIMI_A)
        elif char == ORIGIN_O:
            last_name_simi = last_name_simi.replace(char, SIMI_O)
        elif char == ORIGIN_L:
            last_name_simi = last_name_simi.replace(char, SIMI_L)
        elif char == ORIGIN_S:
            last_name_simi = last_name_simi.replace(char, SIMI_S)
    pswd1 = first_name_simi + str(number_digit) + last_name_simi
    print("Password 1:", pswd1)

    # generate the second password which is an "acronym",
    # consisting of the first and last character from the user's first name,
    # the first and last character of their last name,
    # and the first and last letter of their favorite word.
    # In each case, the first letter of the pair should be lower case and
    # the second should be upper case.
    pswd2 = ''
    for i in (first_name, last_name, f_word):
        pswd2 += i[0].lower() + i[-1].upper()
    print("Password 2:", pswd2)

    # generate the third password which
    # takes a random-length portion of the first name,
    # combined with random-length portions of the favorite word
    # and last name(in any order).
    # In each case, those random-length pieces should
    # start at the beginning of the string,
    # and the code should be written such that it's possible to
    # get the entire string if the largest possible random number is produced.
    # At least one character from each part should appear in the password.
    pswd3 = ''
    first_name_lst = []
    pswd3_lst = []
    for i in range(1, len(first_name)+1):
        x = first_name[:i]
        first_name_lst.append(x)
    pswd3_lst.append(first_name_lst)
    last_name_lst = []
    for i in range(1, len(last_name)+1):
        x = last_name[:i]
        last_name_lst.append(x)
    pswd3_lst.append(last_name_lst)
    f_word_lst = []
    for i in range(1, len(f_word)+1):
        x = f_word[:i]
        f_word_lst.append(x)
    pswd3_lst.append(f_word_lst)

    for word in pswd3_lst:
        str_idx = random.randint(0, len(word)-1)
        pswd3 += word[str_idx]
    print("Password 3:", pswd3)


main()