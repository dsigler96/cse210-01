
from xmlrpc.client import FastMarshaller


class Guess:

    def __init__(self):
        self._guess  = "_ _ _ _ _\n"
        self._letter = ""
        self._cut = "F"
    
    def update_guess(self, word):
        if self._letter in word:
            index = word.index(self._letter)
            self._guess = self._guess[:(index * 2)] + self._letter + self._guess[(index * 2) + 1:]
            self._cut = "F"
        else:
            self._cut = "T"


    def check_guess(self, word):
        return ((self._guess.replace(" ", "")) == word)

    def get_guess(self):
        return self._guess

    def set_letter(self, letter):
        self._letter = letter
    
    def get_cut(self):
        return self._cut


    