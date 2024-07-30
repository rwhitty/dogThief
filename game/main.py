import itertools
from Game import *


def main():
    game = Game()
    print()
    for player_in in game.getPlayers():
        print(player_in)
    print()
    plyr_turn = 0
    while len(game.getPlayers()) > 0:
        all_plyrs = game.getPlayers()
        plyr_turn %= len(all_plyrs)
        player = all_plyrs[plyr_turn]
        print(player.name + "'s Turn")
        print('Your cards:  ' + player.left.name + '    ' + player.right.name)
        if player in game.winCheck():  # if player is victory-eligible
            print(game.winCheck().name + " won!")
            break
        game.collect_move(player)
        print()
        for player_out in game.getPlayers():
            print(player_out)
        print()
        plyr_turn += 1
    print('Good Game!')


if __name__ == "__main__":
    main()
