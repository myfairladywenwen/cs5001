import random as r
from card import Card  # 因为会 call Card constructor所以必须 importCard


class Deck:
    '''A deck of cards'''
    def __init__(self):
        suits = ["hearts", "spades", "diamonds", "clubs"]
        values = ["ace", "2", "3", "4", "5", "6", "7", "8",
                  "9", "10", "jack", "queen", "king"]
        self.cards = [Card(suit, value)
                      for suit in suits
                      for value in values]    # works as a nested loop
        r.shuffle(self.cards)  # mutate the list inside, no return value

    def deal_one(self):
        '''Deal one card from the deck'''
        return self.cards.pop()
