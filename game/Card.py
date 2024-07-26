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
        return self.name if self.face_up else '[  ?  ]'

    def describe(self):
        return "The " + self.name + "." + self.desc

    def flip_up(self):
        self.face_up = True

    def flip_down(self):
        self.face_up = False

    def hasName(self, name):
        return self.name.lower() == name.lower()


def choose_name_from_options(options, prompt, catch='Valid input please!'):
    picking = True
    while picking:
        choice = input(prompt).lower()
        if choice in [option.lower() for option in options]:
            return choice
        else:
            print(catch)


def toLower(str_set):
    return [elem.lower() for elem in str_set]
