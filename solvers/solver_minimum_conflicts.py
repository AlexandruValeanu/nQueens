from random import *
from collections import Counter

n = 0
conflicts = []
columns = Counter()
lrDiagonals = Counter()
rlDiagonals = Counter()
queens = []


def init_all_conflicts():
    global n
    global conflicts
    global columns
    global lrDiagonals
    global rlDiagonals
    global queens

    n = len(queens)

    conflicts = [0 for _ in range(n)]
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


def conflicts_if_changed_queen(row, new_col):
    old_col = queens[row]

    columns[old_col] -= 1
    lrDiagonals[row + old_col] -= 1
    rlDiagonals[row - old_col] -= 1

    columns[new_col] += 1
    lrDiagonals[row + new_col] += 1
    rlDiagonals[row - new_col] += 1

    value = columns[new_col] + lrDiagonals[row + new_col] + rlDiagonals[row - new_col] - 3

    columns[old_col] += 1
    lrDiagonals[row + old_col] += 1
    rlDiagonals[row - old_col] += 1

    columns[new_col] -= 1
    lrDiagonals[row + new_col] -= 1
    rlDiagonals[row - new_col] -= 1

    return value


def min_conflicts(max_iterations=50000):
    global queens
    queens = list(range(n))
    shuffle(queens)

    for iteration in range(max_iterations):
        init_all_conflicts()

        filtered = []
        for (i, c) in enumerate(conflicts):
            if c > 0:
                filtered.append(i)

        if len(filtered) == 0:
            return queens

        row = choice(filtered)
        newConflicts = []
        Min = 2 ** 30
        minimums = []

        for new_col in range(n):
            newConflicts.append(conflicts_if_changed_queen(row, new_col))

            if Min > newConflicts[new_col]:
                Min = newConflicts[new_col]
                minimums = [new_col]
            elif Min == newConflicts[new_col]:
                minimums.append(new_col)

        queens[row] = choice(minimums)

    raise Exception("Incomplete solution: try more iterations.")


def solve(number_queens):
    global n
    n = number_queens
    return min_conflicts()


def slow_minimum_conflicts(number_queens, max_iterations=50000):
    import heuristics

    global n
    global conflicts
    global queens

    n = number_queens
    queens = list(range(n))
    shuffle(queens)

    def random_position(confl, predicate):
        return choice([i for i in range(n) if predicate(confl[i])])

    for iteration in range(max_iterations):
        conflicts = heuristics.get_all_conflicts(queens)

        if max(conflicts) == 0:
            return queens

        row = random_position(conflicts, lambda x: x > 0)
        new_conflicts = [heuristics.conflicts(queens, row, col) for col in range(n)]
        Min = min(new_conflicts)
        queens[row] = random_position(new_conflicts, lambda x: x == Min)

    raise Exception("Incomplete solution: try more iterations.")
