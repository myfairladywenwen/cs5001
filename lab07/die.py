from random import randint


class Die:
    '''A single die.'''
    def __init__(self):
        self.current_value = randint(1, 6)

    def roll(self):
        '''roll the die and set its value.
        None -> None'''
        self.current_value = randint(1, 6)
