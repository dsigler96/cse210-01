import random

class Card:
    """
    Created a class for flipping cards
    """

    def __init__(self):
        """
        Allocated card variables
        """
        self.score = 0
        self.card1 = 0
        self.card2 = 0


    def flip1():
        """
        The first flip
        """
        Card.card1 = random.randint(1,13)
        return Card.card1

    def flip2(card, hi_lo):
        """
        The second flip that compares the two values of the cards and assigns points
        """
        Card.card2 = random.randint(1,13)
        print(f"The next card is {Card.card2}")

        if card < Card.card2 and hi_lo == "h":
            Card.score = 100
        elif card > Card.card2 and hi_lo == "l":
            Card.score = 100
        elif card == Card.card2:
            print("Both cards had equal value, so no points will be distributed")
            Card.score = 0
        else:
            Card.score = -75
        
        return Card.score
        
    
