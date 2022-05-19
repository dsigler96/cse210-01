import random

class Hider:

    def __init__(self):
        self._location = random.randint(1,1000)
        self._distance = [0, 0]

    def get_hint(self):
        if self._distance[-1] == 0:
            hint = "(;.;) You found me!"
        elif self._distance[-1] > self._distance[-2]:
            hint = "(^.^) Getting colder!"
        elif self._distance[-1] < self._distance[-2]:
            hint = "(>.<) Getting warmer!"
        return hint

    def is_found(self):
        return (self._distance[-1] == 0)
    
    def watch_seeker(self, seeker):
        distance = abs(self._location - seeker.get_location())
        self._distance.append(distance)

