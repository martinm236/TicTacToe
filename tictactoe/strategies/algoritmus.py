"""
Algoritmická hra
"""
import random
from .strategy import Strategy


class Algoritmus(Strategy):
    """
    Algoritmická hra
    """

    def __init__(self):
        super().__init__()
        self.jmeno = "Algoritmus"

    def hraj(self, pole):
        """
        Hraje algoritmickou hru
        """
        while True:
            x_random = random.randint(5, 19)
            y_random = random.randint(5, 19)
            if self.is_free(pole, x_random, y_random):
                return x_random, y_random
