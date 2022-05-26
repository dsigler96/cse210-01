from game.guess import Guess
from game.parachute import Parachute
from game.service import Service

class Director:
    def __init__(self):
        self._is_playing = True
        self._guess = Guess()
        self._parachute = Parachute()
        self._service = Service()
        self._prompt = "Guess a letter [a-z]: "
        self._game_over = "Game Over"


    def start_game(self):
        while self._is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        self._service.show_guess(self._guess)
        self._service.show_parachute(self._parachute)
        letter = input(self._prompt)
        self._guess.get_letter(letter)

    def do_updates(self):
        self._guess.update_guess(self._parachute)

    def do_outputs(self):
        if self._parachute.get_lives == 0:
            self._service.read_letter(self._game_over)
            self._service.show_parachute(self._parachute)
            self._is_playing = False
        elif self._guess.check_guess:
            self._is_playing = False
        else:
            return