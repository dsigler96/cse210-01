import random

class Die:
    """
    This is the class that simulates rolling a single die
    """
    def __init__(self):
        """Creates a die"""
        self.value = 0
        self.score = 0


    def roll(self):
        """Generates a roll and allocates points"""
        self.value = random.randint(1,6)
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0
