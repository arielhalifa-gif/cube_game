import utils
def create_player(name: str):
    player_dict = {"name": name, "sum_dice": 0}
    return player_dict


def star_game():
    player1 = create_player("yosi")
    player2 = create_player("shalom")


def play_game(player):
    player_decision = input("please enter your game \n")
    while not utils.turn_decision(player_decision):
        player_decision = input("please enter your game \n")
    if player_decision == "r":
        tupl_dice = roll_two_d6()
        sum1 = sum_roll(player["sum_dice"])