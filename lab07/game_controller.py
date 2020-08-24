from pair_of_dice import PairOfDice


class GameController:
    '''A controller for a simple dice game'''
    def __init__(self):
        self.player_dice = PairOfDice()

    def start_game(self):
        '''interact with user, roll the pair of die and
        determine whether the user wins or not.
        None -> None'''

        input("Press enter to roll the dice...")
        self.player_dice.roll_dice()
        result = self.player_dice.current_value()
        if result == 7 or result == 11:
            print("You rolled " + str(result) + ". You win!")
        elif result == 2 or result == 3 or result == 12:
            print("You rolled " + str(result) + ". You lose.")
        else:
            done = False
            point = result
            while not done:
                print("Your point is " + str(point) + ".")
                input("Press enter to roll the dice...")
                self.player_dice.roll_dice()
                result = self.player_dice.current_value()
                if result == point:
                    print("You rolled " + str(result) + ". You win!")
                    done = True
                elif result == 7:
                    print("You rolled " + str(result) + ". You lose.")
                    done = True
