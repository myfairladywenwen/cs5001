def store_data(filename):
    with open(filename, 'w') as g:
        user_input = str(0)
        while user_input != '999':
            user_input = input('enter your data, 999 to quit: ')
            g.write(user_input + '\n')


def output_data(filename):
    with open(filename, 'r') as g:
        for line in g:
            print(line.strip())


def main():
    done = False
    while not done:
        choice = input('please select S to save data to file' +
                   ' O to output data, and Q to quit: ')
        if choice == 's' or choice == 'S':
            store_data(input('please tell me file name: '))
        elif choice == 'o' or choice == 'O':
            output_data(input('please tell me which file to open: '))
        else:
            done = True

main()
