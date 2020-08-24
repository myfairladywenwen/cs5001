from die import Die


class PairOfDice:
    '''A pair of Dice.'''

    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def roll_dice(self):
        '''roll the two dice.
        None -> None'''
        self.die1.roll()
        self.die2.roll()

    def current_value(self):
        '''summarize the two dice.
        None -> Int'''
        return self.die1.current_value + self.die2.current_value
