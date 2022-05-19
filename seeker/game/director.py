from game.hider import Hider
from game.seeker import Seeker
from game.service import Service

class Director:
    def __init__(self):
        self._is_playing = True
        self._hider = Hider()
        self._seeker = Seeker()
        self._service = Service()


    def start_game(self):
        while self._is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        new_location = self._service.read_number("\nEnter a location [1-1000]: ")
        self._seeker.move_location(new_location)

    def do_updates(self):
        self._hider.watch_seeker(self._seeker)

    def do_outputs(self):
        hint = self._hider.get_hint()
        self._service.write_text(hint)
        if self._hider.is_found():
            self._is_playing = False
