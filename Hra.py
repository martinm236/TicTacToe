class Hra:

    def __init__(self, strategie, zasebou):
        self.strategie = strategie
        self.zasebou = zasebou
        self.pole = [None] * 20
        for i in range(20):
            self.pole[i] = [None] * 20

        self.delka_pole = len(self.pole)

    def set_pole(self, x, y, symbol):
        self.pole[self.delka_pole - y - 1][x - 1] = symbol

    def get_pole(self, x, y):
        return self.pole[self.delka_pole - y - 1][x - 1]

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
                        pass
                    else:
                        pass

    def hraj(self):
            self.set_pole(6, 2, "X")
            print(self.get_pole(6, 2))
            self.vypis_pole()
