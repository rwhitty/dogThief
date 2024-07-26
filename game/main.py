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
        self.draw = Pile.merge(deal, wolves, 'Draw')
        self.draw.shuffle()
        self.discard = Pile('Discard', [])

    def getPlayers(self):
        return self.players

    @staticmethod
    def collect_player_names():
        print()
        print('Enter the name of each player. Maximum 10 players. When finished, type "done" \n')
        players = []
        while len(players) < 10:
            inp = input("Player " + str(len(players) + 1) + ": ")
            if inp.lower() == 'done':
                break
            if (inp is not None) and (inp != ""):
                players += [inp]
        return players

    def collect_move(self, player):
        picking = True
        while picking:
            move = input('Enter your chosen action: ').lower()
            if move == 'default' or move == 'def':
                self.default(player)
                picking = False
            elif move == 'drunk' or move == 'dru':
                self.drunk(player)
                picking = False
            else:
                print('Valid move please!')

    def default(self, player):
        picking = True
        while picking:
            inp = input('Choose a card to discard: ').lower()
            if inp == 'left' or inp == 'right':
                player.discard_to(inp, self.discard)
                picking = False
                break

            elif inp in player.hand():
                where = player.whereCard(inp)
                if where == 'left' or where == 'right':
                    player.discard_to(where, self.discard)
                    picking = False
                elif where == 'both':
                    inp2 = None
                    while inp2 != 'left' and inp2 != 'right':
                        inp2 = input('Choose which ' + inp + ' to discard: ').lower()
                    player.discard_to(inp2, self.discard)
                    picking = False
                else:
                    raise Exception("This shouldn't be happening!")
            else:
                print('Valid input please!')
        player.draw_from(self.draw)

    def drunk(self, player):
        drunk_pile = player.drunk_space(self.draw.pop())
        print(drunk_pile)
        drunk_pile.pile2Pile(self.discard)
        player.pileIntoHand(drunk_pile)


def main():
    game = Game()
    print()
    for player in game.getPlayers():
        print(player)
    print()
    for player in game.getPlayers():
        print(player)
        game.collect_move(player)
        print(player)
        print()


if __name__ == "__main__":
    main()
