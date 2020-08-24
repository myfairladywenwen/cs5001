from team import Team
from bench import Bench
import re


def main():
    print("Welcome to the team manager.")
    the_team = Team()
    the_bench = Bench()

    while True:
        # Immediately converting the input to lower() lets the user enter
        # any kind of capitalization, so it's a little less strict.
        command = (input("What do you want to do?\n")).lower()

        if command == "done":
            print("Shutting down team manager\n")
            return
        elif command == "set team name":
            do_set_team_name(the_team)
        elif command == "show roster":
            do_show_team_roster(the_team)
        elif command == "add player":
            do_add_player_to_team(the_team)
        elif command == "check position is filled":
            do_check_position_filled(the_team)
        elif command == "send player to bench":
            do_send_player_to_bench(the_team, the_bench)
        elif command == "get player from bench":
            do_get_player_from_bench(the_bench)
        elif command == "cut player":
            do_cut_player_from_team(the_team, the_bench)
        elif command == "show bench":
            do_show_bench(the_bench)
        else:
            do_not_understand()


def do_set_team_name(the_team):
    done = False
    team_name = input("What do you want to name the team? " +
                      "(team name should be no more than 4 words, " +
                      "separated by space, and all words should be " +
                      "alphanumeric characters)\n")
    while not done:
        team_name_test_list = team_name.strip().split(' ')
        if len(team_name_test_list) > 4:
            team_name = input("Invalid input.  Please enter again:\n")
        else:
            team_name_test = ''.join(team_name_test_list)
            team_name_list = re.findall(r"\W", team_name_test)
            if team_name_list == []:
                the_team.set_team_name(team_name)
                done = True
            else:
                team_name = input("Invalid input.  Please enter again:\n")


def do_show_team_roster(team):
    team.show_team_roster()


def do_check_position_filled(team):
    position = input("What position are you checking for?\n")
    if team.is_position_filled(position):
        print('Yes, the', position, 'position is filled')
    else:
        print('No, the', position, 'position is not filled')


def do_add_player_to_team(team):
    player_name = input("What's the player's name?" +
                        "(player name should be no more than 4 words, " +
                        "separated by space, and all words should be " +
                        "alphanumeric characters)\n")
    done = False
    while not done:
        player_name_test_list = player_name.strip().split(' ')
        if len(player_name_test_list) > 4:
            player_name = input("Invalid input.  Please enter again:\n")
        else:
            player_name_test = ''.join(player_name_test_list)
            player_name_list = re.findall(r"\W", player_name_test)
            if player_name_list == []:
                done = True
            else:
                player_name = input("Invalid input.  Please enter again:\n")

    player_number = input("What's " + player_name + "'s number?" +
                          "(player's number should be 1 as minimum, " +
                          "99 as largest, and should contain only numbers)\n")
    done = False
    while not done:
        if (player_number[0] != '0' and len(player_number) <= 2
                and player_number.isalnum()):
            done = True
        else:
            player_number = input("Invalid input.  Please enter again:\n")

    player_position = input("What's " + player_name + "'s position?\n")

    team.add_player(player_name, player_number, player_position)


def do_send_player_to_bench(team, bench):
    player_name = input("Who do you want to send to the bench?\n")
    if team.is_in_team(player_name):
        bench.send_to_bench(player_name)
        print('Sent', player_name, 'to bench')
    else:
        print(player_name + ' is not in team.')


def do_get_player_from_bench(bench):
    bench.get_from_bench()


def do_cut_player_from_team(team, bench):
    player_name = input('Who do you want to cut?\n')
    if team.is_in_team(player_name):
        if bench.is_in_bench(player_name):
            print(player_name, "is in bench and can not be cut.")
        else:
            team.cut_player(player_name)
            print(player_name, 'is cut from team')
    else:
        print(player_name, 'is not in team')


def do_show_bench(the_bench):
    the_bench.show_bench()


def do_not_understand():
    print("I didn't understand that command")


main()
