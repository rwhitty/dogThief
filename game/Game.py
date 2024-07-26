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
            if (inp is not None) and (inp != "") and (inp.lower() not in toLower(players)):
                players += [inp]
        return players

    def collect_move(self, player):
        move = choose_name_from_options(['default', 'def', 'drunk', 'dru', 'seer', 'see', 'revealer', 'rev'],
                                        'Choose an action: ')
        if move == 'default' or move == 'def':  # I want to make this a match/case thingy
            self.default(player)
        elif move == 'drunk' or move == 'dru':
            self.drunk(player)
        elif move == 'seer' or move == 'see':
            self.seer(player)
        elif move == 'revealer' or move == 'rev':
            self.revealer(player)
        else:
            raise Exception('Uhhhhhhhhh')

    def default(self, player):
        picking = True
        while picking:
            inp = input('Choose a card to discard: ').lower()
            if inp == 'left' or inp == 'right':
                player.discard_to(inp, self.discard)
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
        drunk_pile = player.drunk_space('Drunk Pile', [self.draw.pop()])
        print(drunk_pile)
        drunk_pile.discard_pick(self.discard)
        player.pileIntoHand(drunk_pile)

    def seer(self, player):  # Technically Apprentice Seer
        seer_pile = player.drunk_space('Seer Pile', self.draw.peek_top(3, True), False)
        print(seer_pile)
        seer_pile.discard_pick(self.discard)
        seer_pile.shuffle()
        self.discard.push(seer_pile.pop())
        rem_card = seer_pile.cards[0]
        print()
        print('Remaining Card: ' + str(rem_card))
        print("Your Hand: " + player.left.name + " " + player.right.name)
        choice = choose_name_from_options([rem_card.name, player.left.name, player.right.name],
                                          'Choose a card to discard: ')
        if rem_card.hasName(choice):
            self.discard.push(rem_card)
        elif player.left.hasName(choice):
            self.discard.push(player.left)
            player.left = rem_card
        elif player.right.hasName(choice):
            self.discard.push(player.right)
            player.right = rem_card
        else:
            raise Exception('Uhhhhhhhhh')

    def revealer(self, player):
        choo_player = choose_name_from_options([player.name for player in self.players], 'Choose a player to reveal: ')
        for player in self.players:
            if player.name.lower() == choo_player.lower():
                choo_side = choose_name_from_options(['left', 'right'], 'Choose a side: ')
                if choo_side == 'left':
                    player.left.face_up = True
                elif choo_side == 'right':
                    player.left.face_up = True

    def winCheck(self):
        for player in self.getPlayers():
            if player.victory():
                return player
        return None
