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

    def check(self):
        kolecek = 0
        krizku = 0
        for y in range(len(self.pole)):
            for x in range(len(self.pole[0])):
                if self.get_pole(x ,y) is not None:
                    if self.get_pole(x ,y) == "X":
                        for i in range(self.zasebou):
                            # Ve sloupci X
                            if self.get_pole(x, y + i) == "X":
                                krizku += 1
                                if krizku == self.zasebou:
                                    print("Křížek vyhrál")
                            else:
                                krizku = 0
                        for i in range(self.zasebou):
                            # Za sebou X
                            if self.get_pole(x + i, y) == "X":
                                krizku += 1
                                if krizku == self.zasebou:
                                    print("Křížek vyhrál")
                            else:
                                krizku = 0
                        for i in range(self.zasebou):
                            # V diagonale1 X
                            if self.get_pole(x + i, y + i) == "X":
                                krizku += 1
                                if krizku == self.zasebou:
                                    print("Křížek vyhrál")
                            else:
                                krizku = 0
                        for i in range(self.zasebou):
                            # V diagonale2 X
                            if self.get_pole(x - i, y + i) == "X":
                                krizku += 1
                                if krizku == self.zasebou:
                                    print("Křížek vyhrál")
                            else:
                                krizku = 0
                    else:
                        for i in range(self.zasebou):
                            # Ve sloupci O
                            if self.get_pole(x, y + i) == "O":
                                kolecek += 1
                                if kolecek == self.zasebou:
                                    print("Kolečko vyhrálo")
                            else:
                                kolecek = 0
                        for i in range(self.zasebou):
                            # Za sebou O
                            if self.get_pole(x + i, y) == "O":
                                kolecek += 1
                                if kolecek == self.zasebou:
                                    print("Kolečko vyhrálo")
                            else:
                                kolecek = 0
                        for i in range(self.zasebou):
                            # V diagonale1 O
                            if self.get_pole(x + i, y + i) == "O":
                                kolecek += 1
                                if kolecek == self.zasebou:
                                    print("Kolečko vyhrálo")
                            else:
                                kolecek = 0
                        for i in range(self.zasebou):
                            # V diagonale2 O
                            if self.get_pole(x - i, y + i) == "O":
                                kolecek += 1
                                if kolecek == self.zasebou:
                                    print("Kolečko vyhrálo")
                            else:
                                kolecek = 0

                else:
                    krizku = 0
                    kolecek = 0
    def hraj(self):
            self.set_pole(6, 2, "O")
            self.set_pole(7, 2, "O")
            self.set_pole(8, 2, "O")
            self.set_pole(9, 2, "O")
            self.set_pole(10, 2, "O")
            self.vypis_pole()
            self.check()
