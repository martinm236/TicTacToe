"""
Tady se vytváří spouští hra
"""
import matplotlib.pyplot as plt
from tictactoe.hra.hra import Hra
from tictactoe.strategies.rucne import Rucne
from tictactoe.strategies.nahodne import Nahodne
from tictactoe.strategies.algoritmus import Algoritmus

r = Rucne()
n = Nahodne()
a = Algoritmus()
X = 0
O = 0
objs = list()
for i in range(5):
    objs.append(Hra(5, n, a))
for obj in objs:
    if obj.hraj() == "X":
        X += 1
    else:
        O += 1

labels = ['Kolečko - ' + a.jmeno, 'Křížek - ' + n.jmeno]
values = [O, X]


WIDTH = 0.1

fig, ax = plt.subplots()

a = ax.bar(labels, values, WIDTH, label='Výhry')
ax.bar_label(a, values)
ax.set_ylabel('Výhry')
ax.set_title('Piškvorky')
ax.legend()
fig.set_size_inches(18.5, 10.5)
plt.savefig("foo.png")
plt.show()
