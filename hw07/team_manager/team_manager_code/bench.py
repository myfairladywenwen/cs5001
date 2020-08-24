from player import Player


class Bench:
    """A class representing a sidelines bench"""
    def __init__(self):
        self.players_in_bench = []
        self.count = 0

    def send_to_bench(self, player_name):
        self.players_in_bench.append(player_name)
        self.count += 1

    def get_from_bench(self):
        '''when need to send a player from bench to play, send the one first
        put to bench.
        Bench object -> None'''

        if self.count != 0:
            player_get = self.players_in_bench.pop(0)
            print('Got ' + player_get + ' from bench')
            self.count -= 1
        else:
            print('The bench is empty.')

    def show_bench(self):
        if self.count != 0:
            print('The bench currently includes:')
            for player in self.players_in_bench:
                print(player)
        else:
            print('The bench is empty.')

    def is_in_bench(self, player_name):
        for player in self.players_in_bench:
            if player == player_name:
                return True
        return False
