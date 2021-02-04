class Hra:

    def __init__(self, strategie: int, zasebou: int):
        self.strategie = strategie
        self.zasebou = zasebou
        self.pole = [None] * 20
        for i in range(20):
            self.pole[i] = [None] * 20

        self.delka_pole = len(self.pole)

    def set_pole(self, x: int, y: int, symbol: str):
        if self.pole[self.delka_pole - y - 1][x] is None:
            self.pole[self.delka_pole - y - 1][x] = symbol
        else:
            print("Zde už někdo je!")

    def get_pole(self, x: int, y: int):
        if x < len(self.pole) and y < len(self.pole):
            return self.pole[self.delka_pole - y - 1][x]
        else:
            return None

    def vypis_pole(self):
        for i in range(len(self.pole)):
            print(self.pole[i])

    def rc(self, in_row_multiplier, in_column_multiplier):
        """

        :param in_row_multiplier:
        :param in_column_multiplier:
        :return: Vyherce
        """
        for y in range(len(self.pole)):
            for x in range(len(self.pole[0])):
                krizku = 0
                kolecek = 0
                if self.get_pole(x, y) is not None:
                    for i in range(self.zasebou):
                        if self.get_pole(x + (i * in_row_multiplier), y + (i * in_column_multiplier)) == "X":
                            krizku += 1
                            if krizku == self.zasebou:
                                return "X"
                        elif self.get_pole(x + (i * in_row_multiplier), y + (i * in_column_multiplier)) == "O":
                            kolecek += 1
                            if kolecek == self.zasebou:
                                return "O"
        return None

    def check_rows(self):
        return self.rc(1, 0)

    def check_columns(self):
        return self.rc(0, 1)

    def check_diagonal1(self):
        return self.rc(1, 1)

    def check_diagonal2(self):
        return self.rc(-1, 1)

    def check(self):
        if self.check_rows() == self.check_columns() == self.check_diagonal1() == (self.check_diagonal2() is None):
            return True
        else:
            return False

    def hraj(self):
            while self.check():
                self.set_pole(int(input("corX")), int(input("corZ")), input("symbol"))
                self.vypis_pole()
