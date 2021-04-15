"""
Ruční hra
"""

from .strategy import Strategy


class Rucne(Strategy):
    """
    Ruční hra
    """

    def __init__(self):
        super().__init__()
        self.jmeno = "Ručně"


    @classmethod
    def hraj(cls):
        """
        Hraje ruční hru
        """
        return int(input("osa X ")), int(input("osa Y "))
