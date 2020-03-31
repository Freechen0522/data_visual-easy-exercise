from random import randint

class Die():
    """show a die class"""
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

    