import utils
def create_player(name: str):
    player_dict = {"name": name, "sum_dice": 0}
    return player_dict


def star_game():
    player1 = create_player("yosi")
    player2 = create_player("shalom")
    return [player1, player2]


def play_game(player):
    player_decision = input("choose your game \n")
    while not utils.turn_decision(player_decision):
        player_decision = input("choose your game (r or p)\n")
    if player_decision == "r":
        tupl_dice = utils.roll_two_d6()
        sum1 = utils.sum_roll(tupl_dice, player["sum_dice"])
        if utils.is_bust():
            pass