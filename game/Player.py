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
        if choice == "left":
            pile.push(self.left)
            self.left = None
        elif choice == "right":
            pile.push(self.right)
            self.right = None
        else:
            raise Exception("Invalid Input: card choice invalid for discard_to")

    def drunk_space(self, drunked, include_hand=True):
        drunk_cards = drunked
        if include_hand:
            drunk_cards += [self.left.cards, self.right]
        drunk_pile = Pile(self.name + "'s " + "Drunk Pile", drunk_cards)
        drunk_pile.flip_down_all()
        drunk_pile.shuffle()
        return drunk_pile

    def __str__(self):
        return self.name + ": " + str(self.left if self.left else "None") + ", " \
                                + str(self.right if self.right else "None")
