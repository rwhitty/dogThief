from optimizations import *


class Card:

    def __init__(self, name, types=None):
        if types is None:
            types = []
        self.name = name
        self.types = np.array(types)
        self.face_up = False

    def isType(self, typ):
        return len(np.intersect1d(self.types, np.array(typ))) > 0

    def __str__(self):
        return self.name if self.face_up else '[  ?  ]'

    def flip_up(self):
        self.face_up = True

    def flip_down(self):
        self.face_up = False

    def hasName(self, name):
        return self.name.lower() == name.lower()


all_cards = [
    Card("Alpha–Wolf", "Wolf"),
    Card("Apprentice Assassin"),
    Card("Apprentice Seer"),
    Card("Assassin"),
    Card("Bodyguard"),
    Card("Copycat"),
    Card("Cupid"),
    Card("Curator"),
    Card("Diseased"),
    Card("Doppelganger"),
    Card("Dream Wolf", "Wolf"),
    Card("Drunk"),
    Card("Gremlin"),
    Card("Hunter"),
    Card("Insomniac"),
    Card("Instigator"),
    Card("Marksman"),
    Card("Mason"),
    Card("Mason"),
    Card("Minion"),
    Card("Mystic Wolf", "Wolf"),
    Card("Paranormal Investigator"),
    Card("Pickpocket"),
    Card("Priest"),
    Card("Renfield", "Vampire"),
    Card("Revealer"),
    Card("Robber"),
    Card("Seer"),
    Card("Sentinel"),
    Card("Tanner"),
    Card("The Count", "Vampire"),
    Card("The Master", "Vampire"),
    Card("Troublemaker"),
    Card("Vampire", "Vampire"),
    Card("Village Idiot"),
    Card("Villager"),
    Card("Villager"),
    Card("Villager"),
    Card("Werewolf", "Wolf"),
    Card("Werewolf", "Wolf"),
    Card("Witch")
]
