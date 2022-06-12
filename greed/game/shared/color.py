class Color:
        
    def __init__(self, red, green, blue, alpha = 255):
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    def to_tuple(self):
        return (self._red, self._green, self._blue, self._alpha)   