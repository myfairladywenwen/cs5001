def main():
    interview()


def interview():
    '''Conducts an interview
    None -> None'''    # takes in no argument -> no output
    questions()
    print("We are done here.")  # no output, since output is given by return


def questions():
    """ Poses questions to the user
    None -> None"""
    answer = 'yes'
    while answer == 'yes':
        answer = input("Do you want to work here?\n")


main()