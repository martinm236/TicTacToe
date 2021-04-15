"""
Třída Hra
"""


class Hra:
    """
    Třída Hra
    """

    def __init__(self, zasebou: int, strategieX, strategieO):
        self.zasebou = zasebou
        self.strategiex = strategieX
        self.strategiey = strategieO
        self.pole = [None] * 20
        for i in range(20):
            self.pole[i] = [None] * 20
        self.delka_pole = len(self.pole)
        self.rounds = 0

    def set_pole(self, osa_x: int, osa_y: int, symbol: str):
        """

        :param osa_x: Osa X
        :param osa_y: Osa Y
        :param symbol: Hráč
        :return: Nastavit hráče na pole
        """
        if self.pole[self.delka_pole - osa_y - 1][osa_x] is None:
            self.pole[self.delka_pole - osa_y - 1][osa_x] = symbol
        else:
            print("Zde už někdo je!")

    def get_pole(self, osa_x: int, osa_y: int):
        """

        :param osa_x: Osa X
        :param osa_y: Osa Y
        :return: Kdo je na tom poli
        """
        if osa_x < len(self.pole) and osa_y < len(self.pole):
            return self.pole[self.delka_pole - osa_y - 1][osa_x]
        return None

    def vypis_pole(self):
        """
        Vypíše pole
        """
        for i in range(len(self.pole)):
            print(self.pole[i])
        print("-----------------------------------------")

    def rcd1d2(self, row_mult, col_mult):
        """

        :param row_mult:
        :param col_mult:
        :return: Vyherce
        """
        for osa_y in range(len(self.pole)):
            for osa_x in range(len(self.pole[0])):
                krizku = 0
                kolecek = 0
                for i in range(self.zasebou):
                    if self.get_pole(osa_x + (i * row_mult), osa_y + (i * col_mult)) == "X":
                        krizku += 1
                        if krizku == self.zasebou:
                            return "X"
                    elif self.get_pole(osa_x + (i * row_mult), osa_y + (i * col_mult)) == "O":
                        kolecek += 1
                        if kolecek == self.zasebou:
                            return "O"
        return None

    def check_rows(self):
        """
        Zkontroluje, zda někdo nevyhrál v řádcích
        """
        return self.rcd1d2(1, 0)

    def check_columns(self):
        """
        Zkontroluje, zda někdo nevyhrál ve sloupcích
        """
        return self.rcd1d2(0, 1)

    def check_diag1(self):
        """
        Zkontroluje, zda někdo nevyhrál v diagonále 1
        """
        return self.rcd1d2(1, 1)

    def check_diag2(self):
        """
        Zkontroluje, zda někdo nevyhrál v diagonále 2
        """
        return self.rcd1d2(-1, 1)

    def get_winner(self):
        """

        :return: Vrátí, kdo vyhrál
        """
        functions = [self.check_rows, self.check_columns, self.check_diag1, self.check_diag2]
        for function in functions:
            funkce = function()
            if funkce is not None:
                return funkce
        return None

    def hraj(self):
        """
        Zde se začíná i končí celá hra
        """
        while self.get_winner() is None:
            self.rounds += 1
            if self.rounds % 2 == 0:
                strategiex = self.strategiex.hraj(self.pole)
                self.set_pole(strategiex[0], strategiex[1], "X")
            else:
                strategiey = self.strategiey.hraj(self.pole)
                self.set_pole(strategiey[0], strategiey[1], "O")

        # print(self.get_winner())
        return self.get_winner()
