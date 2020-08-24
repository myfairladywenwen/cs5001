from random import seed, randint
def main():
    CORRECT_DIFF = 0
    SCAILING_HOT_DIFF = 1
    EXTRE_WARM_DIFF = 2
    VERY_WARM_DIFF = 3
    WARM_DIFF = 5
    COLD_DIFF = 8
    VERY_COLD_DIFF = 13
    EXTRE_COLD_DIFF = 20
    LUCKY_COUNT = 1
    AMAZING_COUNT = 4
    OK_COUNT = 6
    MEH_COUNT = 7
    NOT_GAME_COUNT = 9 

    print("Welcome to the Guessing Game!")
    seed()
    key = randint(1,50)
    user_guess = int(input("I picked a number between 1 and 50." 
                        +" Try and guess!"+"\n"))
    counter = 1
    while True:
        diff = user_guess - key
        diff = diff if diff >= 0 else -diff
        if diff == CORRECT_DIFF:
            break
        elif diff == SCAILING_HOT_DIFF:
            user_guess = int(input("Your guess is scalding hot"+"\n"))
        elif diff == EXTRE_WARM_DIFF:
            user_guess = int(input("Your guess is extremely warm"+"\n"))
        elif diff == VERY_WARM_DIFF:
            user_guess = int(input("Your guess is very warm"+"\n"))
        elif VERY_WARM_DIFF < diff <= WARM_DIFF:
            user_guess = int(input("Your guess is warm"+"\n"))
        elif WARM_DIFF < diff <= COLD_DIFF:
            user_guess = int(input("Your guess is cold"+"\n"))
        elif COLD_DIFF < diff <= VERY_COLD_DIFF:
            user_guess = int(input("Your guess is very cold"+"\n"))
        elif VERY_COLD_DIFF < diff <= EXTRE_COLD_DIFF:
            user_guess = int(input("Your guess is extremely cold"+"\n"))
        else:
            user_guess = int(input("Your guess is icy freezing miserably cold"+"\n"))
        counter+=1 # no matter what the result is, counter should add one

    print("Congratulations. You figured it out in "+
            str(counter)+" tries.")
    #mock or compliment the guesser
    if counter == LUCKY_COUNT:
        print("That was lucky!")
    elif LUCKY_COUNT < counter <= AMAZING_COUNT:
        print("That was amazing!")
    elif AMAZING_COUNT < counter <= OK_COUNT:
        print("That was okay.")
    elif counter== MEH_COUNT:
        print("Meh")
    elif MEH_COUNT < counter <= NOT_GAME_COUNT:
        print("This is not your game.")
    else:
        print("You are the worst guesser I've ever seen.")
main()



