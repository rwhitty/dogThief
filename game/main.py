import itertools

from Game import *


def main():
    game = Game()
    print()
    for player in game.getPlayers():
        print(player)
    print()
    for player in itertools.cycle(game.getPlayers()):
        print(player)
        if game.winCheck() is player:
            print(game.winCheck().name + " won!")
            break
        game.collect_move(player)
        print(player)
        print()
    print('Good Game!')


if __name__ == "__main__":
    main()
