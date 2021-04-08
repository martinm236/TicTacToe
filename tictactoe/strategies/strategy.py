"""
Základ pro strategie
"""


class Strategy:
    """
    Třída pro strategie, všechny z ní dědí
    """

    def __init__(self):
        self.success = False

    def is_free(self, pole, osa_x, osa_y):
        """
        Zjistí, zda je pozice na poli volná
        """
        self.success = True
        if pole[19 - osa_y][osa_x] is None:
            return True
        return None

    def check_around(self, pole, osa_x, osa_y, xyadd):
        """
        Zjistí zda je okolo volno
        """
        self.success = True
        if pole[19 - osa_y + xyadd[0]][osa_x + xyadd[1]] is None:
            return osa_x + xyadd[1], osa_y + xyadd[0]
        return False
