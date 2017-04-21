from typing import *
from collections import Counter


def get_all_conflicts(queens):
    n = len(queens)
    conflicts = [0 for i in range(n)]

    columns = Counter()
    lrDiagonals = Counter()
    rlDiagonals = Counter()

    for (row, col) in enumerate(queens):
        columns[col] += 1
        lrDiagonals[row + col] += 1
        rlDiagonals[row - col] += 1

    for (row, col) in enumerate(queens):
        conflicts[row] += columns[col]
        conflicts[row] += lrDiagonals[row + col]
        conflicts[row] += rlDiagonals[row - col]
        conflicts[row] -= 3

    return conflicts


def attacking_pairs(queens):
    columns = Counter()
    lrDiagonals = Counter()
    rlDiagonals = Counter()

    total = 0

    for (row, col) in enumerate(queens):
        total += columns[col]
        total += lrDiagonals[row + col]
        total += rlDiagonals[row - col]

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


def conflicts(queens, row, col):
    total = 0

    for (r, c) in enumerate(queens):
        if r != row and (c == col or abs(row - r) == abs(col - c)):
            total += 1

    return total
