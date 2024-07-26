from Pile import *


class Player:

    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

    def draw_from(self, pile):
        if self.left is None:
            self.left = pile.pop()
        if self.right is None:
            self.right = pile.pop()

    def discard_to(self, choice, pile):
        choice = choice.lower()
        if choice == "left":
            pile.push(self.left)
            self.left = None
        elif choice == "right":
            pile.push(self.right)
            self.right = None
        else:
            raise Exception("Invalid Input: card choice invalid for discard_to")

    def drunk_space(self, name, drunked, include_hand=True):
        drunk_cards = drunked
        if include_hand:
            drunk_cards += [self.left, self.right]
        drunk_pile = Pile(name, drunk_cards)
        drunk_pile.flip_down_all()
        drunk_pile.shuffle()
        return drunk_pile

    def __str__(self):
        return self.name + ": " + str(self.left) + ", " + str(self.right)

    def hand(self):
        return [self.left.name.lower(), self.right.name.lower()]

    def pileIntoHand(self, pile):
        if pile.size() != 2:
            raise Exception("Your pile isn't the right size!")
        self.left = pile.cards[0]
        self.right = pile.cards[1]

    def whereCard(self, card_name):
        if self.left.hasName(card_name) and self.right.hasName(card_name):
            return 'both'
        elif self.left.hasName(card_name):
            return 'left'
        elif self.right.hasName(card_name):
            return 'right'
        else:
            return 'none'

    def victory(self):
        return self.left.isType('Wolf') and self.right.isType('Wolf')
