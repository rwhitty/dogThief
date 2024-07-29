from Pile import *


class Player:

    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

    def clear(self):
        self.left = None
        self.right = None

    def play_space(self, cards_inq, include_hand=True):
        if include_hand:
            cards_inq += [self.left, self.right]
        play_pile = Pile(cards_inq)
        play_pile.flip_down_all()
        play_pile.shuffle()
        return play_pile

    def __str__(self):
        return self.name + ":\t" + str(self.left) + "\t" + str(self.right)

    def draw_from(self, pile):
        if not self.left:
            self.left = pile.pop()
        if not self.right:
            self.right = pile.pop()

    def whereCard(self, card_name):
        if self.left.hasName(card_name) and self.right.hasName(card_name):
            return 'both'
        elif self.left.hasName(card_name):
            return 'left'
        elif self.right.hasName(card_name):
            return 'right'
        else:
            return 'neither'

    def discard_to(self, pile, choice=None):
        if not choice:
            choice = choose_name_from_options(['left', 'right', self.left.name, self.right.name],
                                              'Choose a card to discard: ')
        if choice == "left":
            self.left.flip_down()
            pile.push(self.left)
            self.left = None
        elif choice == "right":
            self.right.flip_down()
            pile.push(self.right)
            self.right = None
        elif self.left.hasName(choice) or self.right.hasName(choice):
            where = self.whereCard(choice)
            if where == 'left' or where == 'right':
                self.discard_to(pile, choice=where)
            elif where == 'both':
                choice2 = choose_name_from_options(['left', 'right', self.left.name, self.right.name],
                                                   'Choose which ' + choice + ' to discard: ')
                self.discard_to(pile, choice=choice2)
            else:
                raise Exception("This shouldn't be happening!")
        else:
            raise Exception("This shouldn't be happening!")

    def victory(self):  # If there's other _static_ means of victory, we can add them here.
        return self.left.isType('Wolf') and self.right.isType('Wolf')
