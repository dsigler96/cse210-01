
class Guess:

    def __init__(self):
        self._guess  = "_ _ _ _ _"
        self._letter = ""

    def get_letter(self, letter):
        self._letter = letter
    
    def update_guess(self, parachute):
        word = parachute.get_word()
        if self._letter in word:
            index = word.index(self._letter)
            self._guess = self._guess[:(index * 2)] + self._letter + self._guess[(index * 2) + 1:]
        else:
            parachute.cut_line()

    def check_guess(self, parachute):
        return ((self._guess.replace(" ", "")) == parachute.get_word())

    def get_guess(self):
        return self._guess

    