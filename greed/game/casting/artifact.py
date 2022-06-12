from game.casting.actor import Actor


class Artifact(Actor):
    
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        return self._message
    
    def set_message(self, message):
        self._message = message