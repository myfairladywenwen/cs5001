class Player:
    """A class representing a dodgeball player"""

    def __init__(self, name, num, position):
        self.name = name
        self.num = num
        self.position = position

    def __str__(self):
        '''make sure the presentation of player is with some format
        Player object -> String'''

        return '{:<6}{:<20}{:<10}'.format(self.num, self.name, self.position)
