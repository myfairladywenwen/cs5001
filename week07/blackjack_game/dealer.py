import random as r
from deck import Deck


class Dealer:
    '''A blackjack dealer'''
    def __init__(self):
        DEALER_RANGE = (17, 21)
        self.score = r.randint(*DEALER_RANGE)  # pass in a tuple as argument
        self.deck = Deck()  # call Deck constructor 所以要 import Deck

    def deal_one(self):
        return self.deck.deal_one()

