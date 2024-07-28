from Player import *


#  from flask import Flask
#  from flask_socketio import SocketIO


class Game:

    def __init__(self):

        player_names = Game.collect_player_names()
        self.players = [Player(name) for name in player_names]

        self.draw_pile = Pile(all_cards)
        self.discard_pile = Pile([])

        wolves = self.draw_pile.pop_type('Wolf')
        self.draw_pile.shuffle()
        for player in self.players:
            player.draw_from(self.draw_pile)

        self.draw_pile.merge_w(wolves)

        """
        self.decks = Decks()

        for player in self.players:
            player.left = self.pile.deal_draw(1, exclude_type="Wolf")
            player.right = self.pile.deal_draw(1, exclude_type="Wolf")
        """

    def getPlayers(self):
        return self.players

    @staticmethod
    def collect_player_names():
        print()
        print('Enter the name of each player. Maximum 10 players. When finished, type "done" \n')
        player_names = []
        while len(player_names) < 10:
            inp = input("Player " + str(len(player_names) + 1) + ": ")
            if inp.lower() == 'done':
                break
            if (inp is not None) and (inp != "") and (inp.lower() not in toLower(player_names)):
                player_names += [inp]
        return player_names

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

    #   def apprentice_seer(self, player):
    #       seen_cards = self.pile.deal_draw(3)"""

    def default(self, player):
        player.discard_to(self.discard_pile)
        player.draw_from(self.draw_pile)

    def drunk(self, player):
        drunk_pile = player.play_space([self.draw_pile.pop()])
        print(drunk_pile)
        drunk_pile.discard(self.discard_pile)
        player.clear()
        player.draw_from(drunk_pile)

    def seer(self, player):  # Technically Apprentice Seer
        seer_pile = player.play_space(self.draw_pile.pop_top(3), False)
        print(seer_pile)
        seer_pile.discard(self.discard_pile)
        seer_pile.shuffle()
        self.discard_pile.push(seer_pile.pop())
        rem_card = seer_pile.pop()
        print()
        print('Remaining Card: ' + rem_card.name)
        print("Your Hand: " + player.left.name + " " + player.right.name)
        choice = choose_name_from_options([rem_card.name, player.left.name, player.right.name],
                                          'Choose a card to discard: ')
        if rem_card.hasName(choice):
            self.discard_pile.push(rem_card)
        elif player.left.hasName(choice):
            self.discard_pile.push(player.left)
            player.left = rem_card
        elif player.right.hasName(choice):
            self.discard_pile.push(player.right)
            player.right = rem_card
        else:
            raise Exception('Uhhhhhhhhh')

    def revealer(self, act_player):
        choo_player = choose_name_from_options([player.name for player in self.players if player != act_player],
                                               'Choose a player to reveal: ')
        for player in self.players:
            if player.name.lower() == choo_player.lower():
                choo_side = choose_name_from_options(['left', 'right'], 'Choose a side: ')
                if choo_side == 'left':
                    player.left.face_up = True
                elif choo_side == 'right':
                    player.right.face_up = True

    def winCheck(self):
        winners = []
        for player in self.getPlayers():
            if player.victory():
                winners.append(player)
        return winners

    # Eventually this will render content to a specific player
#    def render_to_player(self, player):
#        return None

#   def render_to_all(self):
#        return None
