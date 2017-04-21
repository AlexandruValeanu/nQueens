from heuristics import *

from random import shuffle

n = 100
queens = list(range(n))
shuffle(queens)

for _ in range(1000):
    shuffle(queens)
    a, b = attacking_pairs(queens), naive_attacking_pairs(queens)
    print(a, b)
    assert a == b