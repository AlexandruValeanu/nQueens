from typing import *
from collections import Counter


def attacking_pairs(queens):
    rows = Counter()
    columns = Counter()
    lrDiagonals = Counter()
    rlDiagonals = Counter()

    total = 0

    for (row, col) in enumerate(queens):
        total += rows[row]
        total += columns[col]
        total += lrDiagonals[row + col]
        total += rlDiagonals[row - col]

        rows[row] += 1
        columns[col] += 1
        lrDiagonals[row + col] += 1
        rlDiagonals[row - col] += 1

    return total


def naive_attacking_pairs(queens):
    n = len(queens)
    total = 0

    for i in range(n):
        row1, col1 = i, queens[i]

        for j in range(i + 1, n):
            row2, col2 = j, queens[j]

            if row1 == row2 or col1 == col2:  # row or column clash
                total += 1
            elif abs(row1 - row2) == abs(col1 - col2):  # diagonal clash
                total += 1

    return total
