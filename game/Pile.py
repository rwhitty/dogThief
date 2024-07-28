from Card import *


class Pile:

    def __init__(self, cards):
        self.cards = cards

    def pop(self):
        return self.cards.pop()

    def pop_top(self, n=1):
        out = self.cards[-n:]
        del self.cards[-n:]
        return out

    def push(self, card):
        self.cards.append(card)

    def size(self):
        return len(self.cards)

    def shuffle(self):
        card_list = self.cards
        np.random.shuffle(card_list)
        self.cards = card_list

    def pop_type(self, typ):
        out, out_ind = [], []
        for num, card in enumerate(self.cards):
            if card.isType(typ):
                out_ind.append(num)
                out.append(card)
        for ind in sorted(out_ind, reverse=True):
            del self.cards[ind]
        return Pile(out)

    def __str__(self):
        out = ""
        for card in self.cards:
            out += " " + card.name
        return out

    def toList(self):
        out = []
        for card in self.cards:
            out.append(card.name.lower())
        return out

    def merge_w(self, p2):
        self.cards.extend(p2.cards)
        self.shuffle()

    def flip_up_all(self):
        for card in self.cards:
            card.flip_up()

    def flip_down_all(self):
        for card in self.cards:
            card.flip_down()

    def discard(self, out_pile):
        choice = choose_name_from_options(self.toList(), 'Choose a card to discard: ')
        for card in self.cards:
            if card.name.lower() == choice:
                card.flip_down()
                out_pile.push(card)
                self.cards.remove(card)
                break
