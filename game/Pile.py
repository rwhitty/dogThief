from Card import *


class Pile:

    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def pop(self):
        return self.cards.pop()

    def size(self):
        return len(self.cards)

    def push(self, item):
        self.cards.append(item)

    def peek_top(self, n=1, pop=False):
        out = self.cards[-n:]
        if pop:
            del self.cards[-n:]
        return out

    def peek_bottom(self, n=1, pop=False):
        out = self.cards[:n]
        if pop:
            del self.cards[:n]
        return out

    def shuffle(self):
        card_array = self.cards
        np.random.shuffle(card_array)
        self.cards = card_array

    def pop_type(self, typ):
        out_ind = []
        for i in range(self.size()):
            if self.cards[i].isType(typ):
                out_ind += [i]
        out = self.cards[out_ind]
        del self.cards[out_ind]
        return out

    def __str__(self):
        out = self.name + ":"
        for card in self.cards:
            out += " " + card.name
        return out

    def toList(self):
        out = []
        for card in self.cards:
            out += [card.name.lower()]
        return out

    def copy(self, new_name):
        return Pile(new_name, self.cards)

    def copy_only_type(self, new_name, typ):
        new_cards = []
        for card in self.cards:
            if card.isType(typ):
                new_cards += [card]
        return Pile(new_name, new_cards)

    def copy_without_type(self, new_name, typ):
        new_cards = []
        for card in self.cards:
            if not card.isType(typ):
                new_cards += [card]
        return Pile(new_name, new_cards)

    def flip_up_all(self):
        for card in self.cards:
            card.face_up = True

    def flip_down_all(self):
        for card in self.cards:
            card.face_up = False

    def discard_pick(self, outlet):
        choice = choose_name_from_options(self.toList(), 'Choose a card to discard: ')
        for i in range(self.size()):
            if self.toList()[i] == choice:
                outlet.push(self.cards[i])
                self.cards.remove(self.cards[i])
                break

    @staticmethod
    def merge(p1, p2, new_name):
        return Pile(new_name, p1.cards + p2.cards)


# All the cards
werewolf = Card('Werewolf', 'Wolf', 'Reveal two Werewolves to win the game!')
villager = Card('Villager', None, 'Reveal two Villagers to force everyone else to reveal their cards.')
robber = Card('Robber')
troublemaker = Card('Troublemaker')
seer = Card('Seer')
tanner = Card('Tanner')
minion = Card('Minion')
mason = Card('Mason')
doppelganger = Card('Doppelganger')
drunk = Card('Drunk')
insomniac = Card('Insomniac')
hunter = Card('Hunter')
alpha_wolf = Card('Alpha–Wolf', 'Wolf')

all_cards = Pile('Dogthief Cards', [werewolf, werewolf, villager, villager, villager, robber,
                                    troublemaker, seer, tanner, minion, mason, mason, doppelganger,
                                    drunk, insomniac, hunter, alpha_wolf])
