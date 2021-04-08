"""
Náhodná hra
"""
import random
from strategy import Strategy


class Nahodne(Strategy):
    """
    Náhodná hra
    """
    def __init__(self):
        super().__init__()
        self.jmeno = "Náhodně"

    def hraj(self, pole):
        """
        Hraje náhodnou hru
        """
        while True:
            x_random = random.randint(0, 19)
            y_random = random.randint(0, 19)
            if self.is_free(pole, x_random, y_random):
                return x_random, y_random
