from game.card import Card


class Director:
    """A person who directs the game. 
    The responsibility of a Director is to control the sequence of play.
    """

    def __init__(self):
        """
        Constructs a new Director.
        """
        self.is_playing = True
        self.total_score = 300
        self.card1 = 0
        self.card2 = 0
        self.hi_lo = ""


    def start_game(self):
        """
        Starts the game by running the main game loop.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_outputs()
            self.cont_check()

    def get_inputs(self):
        """
        Gets the input of the user for higher or lower.
        """
        if not self.is_playing:
            return 

        self.card1 = Card.flip1()
        print(f"The first card is {self.card1}")

        self.hi_lo = input("Higher or lower? [h/l] ")

        if self.hi_lo == "h" or self.hi_lo == "l":
            return
        else:
            print("Please enter a lowercase h or l to proceed")
            self.get_inputs()
            return
       
    def do_outputs(self):
        """
        Flips a second card and updates the player's score accordingly.
        """
        if not self.is_playing:
            return 

        score = Card.flip2(self.card1, self.hi_lo)
        self.total_score = self.total_score + score
        print(f"Your score is: {self.total_score}\n")
        return

    def cont_check(self):
        """
        Asks the player if they want to continue. 
        """
        if not self.is_playing:
            return
        if self.total_score <= 0:
            print("Your score is below 0, and you have lost. Try again!")
            self.is_playing = False
            return

        cont = input("Play again? [y/n] ")

        if cont == "y":
            return
        elif cont == "n":
            self.is_playing = False
            return
        else:
            print("Please enter a y or n")
            self.cont_check()
            return
        


        
        
        