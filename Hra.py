class Hra:

    def __init__(self, strategie: int, zasebou: int):
        self.strategie = strategie
        self.zasebou = zasebou
        self.pole = [None] * 20
        for i in range(20):
            self.pole[i] = [None] * 20

        self.delka_pole = len(self.pole)

    def set_pole(self, x: int, y: int, symbol: str):
        self.pole[self.delka_pole - y - 1][x] = symbol

    def get_pole(self, x: int, y: int):
        if x < len(self.pole) and y < len(self.pole):
            return self.pole[self.delka_pole - y - 1][x]
        else:
            return None

    def vypis_pole(self):
        for i in range(len(self.pole)):
            print(self.pole[i])

    def check_rows(self):
        for y in range(len(self.pole)):
            for x in range(len(self.pole[0])):
                krizku = 0
                kolecek = 0
                if self.get_pole(x ,y) is not None:
                    for i in range(self.zasebou):
                        if self.get_pole(x + i, y) == "X":
                            krizku += 1
                            kolecek = 0
                            if krizku == self.zasebou:
                                return "X"
                        elif self.get_pole(x + i, y) == "O":
                            krizku = 0
                            kolecek += 1
                            if kolecek == self.zasebou:
                                return "O"

    def check_columns(self):
        for y in range(len(self.pole)):
            for x in range(len(self.pole[0])):
                krizku = 0
                kolecek = 0
                if self.get_pole(x ,y) is not None:
                    for i in range(self.zasebou):
                        if self.get_pole(x, y + i) == "X":
                            krizku += 1
                            kolecek = 0
                            if krizku == self.zasebou:
                                return "X"
                        elif self.get_pole(x, y + i) == "O":
                            krizku = 0
                            kolecek += 1
                            if kolecek == self.zasebou:
                                return "O"

    def check_diagonal1(self):
        for y in range(len(self.pole)):
            for x in range(len(self.pole[0])):
                krizku = 0
                kolecek = 0
                if self.get_pole(x, y) is not None:
                    for i in range(self.zasebou):
                        if self.get_pole(x + i, y + i) == "X":
                            krizku += 1
                            kolecek = 0
                            if krizku == self.zasebou:
                                return "X"
                        elif self.get_pole(x + i, y + i) == "O":
                            krizku = 0
                            kolecek += 1
                            if kolecek == self.zasebou:
                                return "O"

    def check_diagonal2(self):
        for y in range(len(self.pole)):
            for x in range(len(self.pole[0])):
                krizku = 0
                kolecek = 0
                if self.get_pole(x, y) is not None:
                    for i in range(self.zasebou):
                        if self.get_pole(x - i, y + i) == "X":
                            krizku += 1
                            kolecek = 0
                            if krizku == self.zasebou:
                                return "X"
                        elif self.get_pole(x - i, y + i) == "O":
                            krizku = 0
                            kolecek += 1
                            if kolecek == self.zasebou:
                                return "O"


    def check(self):
        self.check_rows()
        self.check_columns()
        self.check_diagonal1()
        self.check_diagonal2()

    def hraj(self):
            self.set_pole(1, 2, "O")
            self.set_pole(2, 3, "O")
            self.set_pole(3, 4, "O")
            self.set_pole(4, 5, "O")
            self.set_pole(5, 6, "O")
            self.vypis_pole()
            self.check()
