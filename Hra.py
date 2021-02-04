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

    def check(self):
        for y in range(len(self.pole)):
            for x in range(len(self.pole[0])):
                krizku = [0, 0, 0, 0]
                kolecek = [0, 0, 0, 0]
                if self.get_pole(x, y) is not None:
                    for i in range(self.zasebou):
                        if self.get_pole(x, y + i) == "X":
                            krizku[0] += 1
                            if krizku[0] == self.zasebou:
                                return "X"
                        elif self.get_pole(x + i, y) == "X":
                            krizku[1] += 1
                            if krizku[1] == self.zasebou:
                                return "X"
                        elif self.get_pole(x + i, y + i) == "X":
                            krizku[2] += 1
                            if krizku[2] == self.zasebou:
                                return "X"
                        elif self.get_pole(x - i, y + i) == "X":
                            krizku[3] += 1
                            if krizku[3] == self.zasebou:
                                return "X"
                        elif self.get_pole(x, y + i) == "O":
                            kolecek[0] += 1
                            if kolecek[0] == self.zasebou:
                                return "O"
                        elif self.get_pole(x + i, y) == "O":
                            kolecek[1] += 1
                            if kolecek[1] == self.zasebou:
                                return "O"
                        elif self.get_pole(x + i, y + i) == "O":
                            kolecek[2] += 1
                            if kolecek[2] == self.zasebou:
                                return "O"
                        elif self.get_pole(x - i, y + i) == "O":
                            kolecek[3] += 1
                            if kolecek[3] == self.zasebou:
                                return "O"

    def hraj(self):
        while self.check() is None:
            self.set_pole(int(input("corX")), int(input("corZ")), input("symbol"))
            self.vypis_pole()
