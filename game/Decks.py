from Pile import *


class Decks:

    def __init__(self):
        self.draw_pile = Pile(all_cards)  # The front of the list (index 0) is the top
        self.discard_pile = Pile([])  # Ditto above
        np.random.shuffle(self.draw_pile)

    def deal_draw(self, n, exclude_type=None):

        dealt_cards = []
        index = 0

        while len(dealt_cards) < n:
            if self.draw_pile[-1] != exclude_type:
                dealt_cards.append(self.draw_pile.pop(index))
            else:
                index += 1

            if len(self.draw_pile) == 0:
                self.draw_pile = self.discard_pile
                self.discard_pile = []
                np.random.shuffle(self.draw_pile)

        np.random.shuffle(self.discard_pile)
        return dealt_cards

    def deal_discard(self, n, exclude_type=None):

        if n > len(self.discard_pile):
            raise Exception("Not enough cards in discard pile!")

        dealt_cards = []
        index = 0

        while len(dealt_cards) < n:
            if self.discard_pile[-1] != exclude_type:
                dealt_cards.append(self.discard_pile.pop(index))
            else:
                index += 1

        np.random.shuffle(self.discard_pile)
        return dealt_cards
