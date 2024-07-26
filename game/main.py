from Pile import *
from Player import *


class Game:

    def __init__(self, cards=all_cards):
        player_names = Game.collect_player_names()
        self.players = [Player(name) for name in player_names]
        deal = cards.copy_without_type('Deal', 'Wolf')
        wolves = cards.copy_only_type('Wolves', 'Wolf')
        deal.shuffle()
        for player in self.players:
            player.draw_from(deal)
        draw = Pile.merge(deal, wolves, 'Draw')
        draw.shuffle()

    def getPlayers(self):
        return self.players

    @staticmethod
    def collect_player_names():
        print("Type in the name of each player. Maximum 10 players. When finished, type done \n")
        players = []
        while len(players) < 10:
            inp = input("Player " + str(len(players) + 1) + ": ")
            if inp.lower() == 'done':
                break
            if (inp is not None) and (inp != ""):
                players += [inp]
        return players


def main():
    game = Game()
    print()
    for player in game.getPlayers():
        print(player)


if __name__ == "__main__":
    main()
