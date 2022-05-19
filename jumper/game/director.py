from game.guess import Guess
from game.parachute import Parachute
from game.service import Service

class Director:
    def __init__(self):
        self._is_playing = True
        self._guess = Guess()
        self._parachute = Parachute()
        self._service = Service()


    def start_game(self):
        while self._is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        #Shows guess status
        #Shows parachute status
        #prompts guess
        return

    def do_updates(self):
        #Checks if letter was in word
        return

    def do_outputs(self):
        #Updates lives accordingly
        #Updates parachute image
        #Checks if game is over
        return