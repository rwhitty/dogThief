from Pile import *


class Decks:

    def __init__(self):
        self.draw = Pile(all_cards)  # The front of the list (index 0) is the top
        self.discard = Pile([])  # Ditto above
        self.draw.shuffle()

    def deal_to_player(self, player):  # exclude_type is easier to implement outside
        if self.draw.size() < 1:
            self.shuffle_all()
        player.draw_from(self.draw)

    def disc_to_player(self, player):  # exclude_type is easier to implement outside
        if self.discard.size() < 1:
            raise Exception("Not enough cards in discard pile!")
        player.draw_from(self.discard)

    def shuffle_all(self):
        self.draw.cards = self.discard.cards
        self.discard.cards = []
        self.draw.shuffle()

    def draw_empty(self, n=1):
        return self.draw.size() < n
