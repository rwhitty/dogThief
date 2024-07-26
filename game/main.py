import itertools

from Game import *


def main():
    game = Game()
    print()
    for player in game.getPlayers():
        print(player)
    print()
    for player in itertools.cycle(game.getPlayers()):
        print(player.name + "'s Turn")
        print('Your cards: ' + player.left.name + ', ' + player.right.name)
        if game.winCheck() is player:
            print(game.winCheck().name + " won!")
            break
        game.collect_move(player)
        print()
        for player_out in game.getPlayers():
            print(player_out)
        print()
    print('Good Game!')


if __name__ == "__main__":
    main()
