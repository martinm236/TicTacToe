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
        krizku = 0
        kolecek = 0
        for y in range(len(self.pole)):
            for x in range(len(self.pole[0])):
                if self.get_pole(x ,y) is not None:
                    for i in range(self.zasebou):
                        if self.get_pole(x + i, y) == "X":
                            krizku += 1
                            kolecek = 0
                            if krizku == self.zasebou:
                                print("Křížek vyhrál")
                        else:
                            krizku = 0
                            kolecek += 1
                            if kolecek == self.zasebou:
                                print("Kolečko vyhrálo")

    def check_columns(self):
        krizku = 0
        kolecek = 0
        for y in range(len(self.pole)):
            for x in range(len(self.pole[0])):
                if self.get_pole(x ,y) is not None:
                    for i in range(self.zasebou):
                        if self.get_pole(x, y + i) == "X":
                            krizku += 1
                            kolecek = 0
                            if krizku == self.zasebou:
                                print("Křížek vyhrál")
                        else:
                            krizku = 0
                            kolecek += 1
                            if kolecek == self.zasebou:
                                print("Kolečko vyhrálo")

    def check_diagonal1(self):
        krizku = 0
        kolecek = 0
        for y in range(len(self.pole)):
            for x in range(len(self.pole[0])):
                if self.get_pole(x, y) is not None:
                    for i in range(self.zasebou):
                        if self.get_pole(x + i, y + i) == "X":
                            krizku += 1
                            kolecek = 0
                            if krizku == self.zasebou:
                                print("Křížek vyhrál")
                        else:
                            krizku = 0
                            kolecek += 1
                            if kolecek == self.zasebou:
                                print("Kolečko vyhrálo")

    def check_diagonal2(self):
        krizku = 0
        kolecek = 0
        for y in range(len(self.pole)):
            for x in range(len(self.pole[0])):
                if self.get_pole(x, y) is not None:
                    for i in range(self.zasebou):
                        if self.get_pole(x - i, y + i) == "X":
                            krizku += 1
                            kolecek = 0
                            if krizku == self.zasebou:
                                print("Křížek vyhrál")
                        else:
                            krizku = 0
                            kolecek += 1
                            if kolecek == self.zasebou:
                                print("Kolečko vyhrálo")


    def check(self):
        self.check_rows()
        self.check_columns()
        self.check_diagonal1()
        self.check_diagonal2()

    def hraj(self):
            self.set_pole(1, 2, "X")
            self.set_pole(2, 3, "X")
            self.set_pole(3, 4, "X")
            self.set_pole(4, 5, "X")
            self.set_pole(5, 6, "X")
            self.vypis_pole()
            self.check()
