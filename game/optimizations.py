import numpy as np


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