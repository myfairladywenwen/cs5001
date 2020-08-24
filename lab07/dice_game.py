from game_controller import GameController


def main():
    '''This program is a simple dice game.
    None -> None'''

    gc = GameController()
    print("--------------------------------")
    print("Welcome to street craps!")
    print("Rules:")
    print("If you roll 7 or 11 on your first roll, you win.")
    print("If you roll 2, 3, or 12 on your first role, you lose.")
    print("If you roll anything else, that's your 'point', and")
    print("you keep rolling until you either roll your point")
    print("again (win) or roll a 7 (lose)")

    gc.start_game()


main()
