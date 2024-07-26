import numpy as np


class Card:

    def __init__(self, name, types=None, desc=None, face_up=False):
        if types is None:
            types = []
        self.name = name
        self.types = np.array(types)
        self.desc = desc
        self.face_up = face_up

    def pushDesc(self, func):
        self.desc = func

    def isType(self, typ):
        return len(np.intersect1d(self.types, np.array(typ))) > 0

    def __str__(self):
        return self.name

    def describe(self):
        return "The " + self.name + "." + self.desc

    def flip_up(self):
        self.face_up = True

    def flip_down(self):
        self.face_up = False

    def hasName(self, name):
        return self.name.lower() == name.lower()


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
        np.random.shuffle(self.cards)

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

    def pile2Pile(self, outlet):
        picking = True
        while picking:
            inp = input('Choose a card to discard: ').lower()
            if inp in self.toList():
                ind = 0
                found = False
                while ind < self.size() and not found:
                    if self.toList()[ind] == inp:
                        outlet.push(self.cards[ind])
                        self.cards.remove(self.cards[ind])
                        found = True
                    else:
                        ind += 1
                picking = False
            else:
                print('Valid input please!')

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
