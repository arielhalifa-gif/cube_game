if __name__ == "__main__":
    import game
    import utils
    game = game.start_game()
    winner = False
    while not winner:
        pass_ = 0
        for i in range(2):
            print(f"player {i+1} your turn")
            print(f"you score is {game[i]["sum_dice"]}")
            result = game.play_game(game[i])
            if result != "pass":
                print(f"your score for now is {result}")
            else:
                print(f"you have passed")
                pass_ += 1
        if pass_ == 2:
            winner = True