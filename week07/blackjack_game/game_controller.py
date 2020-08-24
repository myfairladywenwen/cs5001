from dealer import Dealer
from hand import Hand


class GameController:
    '''A controller for a simple Blackjack game'''

    def __init__(self):
        self.BLACKJACK = 21
        self.dealer = Dealer()
        self.player_hand = Hand()

    def start_play(self):
        '''Start the game'''
        print("The dealer's score is", self.dealer.score)
        self.deal_two()
        self.display_hand()

    def deal_two(self):
        '''Deal two cards'''
        self.player_hand.receive_cards(self.dealer.deal_one())
        self.player_hand.receive_cards(self.dealer.deal_one())

    def display_hand(self):
        '''Display the hand'''
        self.player_hand.display()
        self.stay_or_hit(input('Would you like to stay or hit?\n'))

    def stay_or_hit(self, s_or_h):
        if s_or_h == 'hit':
            self.player_hand.receive_cards(self.dealer.deal_one())
            self.display_hand()
            if self.player_is_bust():
                self.do_bust()
            else:
                self.stay_or_hit(input('Would you like to stay or hit?\n'))
        elif s_or_h == 'stay':
            self.do_stay()
        else:
            self.stay_or_hit(input('Would you like to stay or hit?\n'))

    def player_is_bust(self):
        '''Determine if player is bust'''
        return self.player_hand.score(self.BLACKJACK) > self.BLACKJACK

    def do_stay(self):
        if self.player_hand.score(self.BLACKJACK) > self.dealer.score:
            print('You win!')
        elif self.player_hand.score(self.BLACKJACK) < self.dealer.score:
            print('You lose!')
        else:
            print('You tied!')

    def do_bust(self):
        print('**************')
        print('     BUST     ')
        print('**************')
