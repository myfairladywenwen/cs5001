from player import Player
from bench import Bench


class Team:
    """A class representing a dodgeball team"""

    def __init__(self):
        self.team_name = "Anonymous Team"
        self.players = []

    def set_team_name(self, team_name):
        self.team_name = team_name

    def add_player(self, player_name, player_number, player_position):
        new_player = Player(player_name, player_number, player_position)
        self.players.append(new_player)
        print('Added', player_name, 'to', self.team_name)

    def cut_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                self.players.remove(player)

    def is_position_filled(self, position):
        for player in self.players:
            if player.position == 'position':
                return True
        return False

    def show_team_roster(self):
        print('The line up for', self.team_name, 'is:')
        if len(self.players) == 0:
            print('The team currently has no players')
        else:
            for player in self.players:
                print(player)

    def is_in_team(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return True
        return False
