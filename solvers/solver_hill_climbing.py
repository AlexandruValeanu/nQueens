from heuristics import *
from random import shuffle


def hill_climbing(n, max_iterations=10000):
    queens = list(range(n))
    shuffle(queens)

    number_iterations = 0
    heuristicValue = attacking_pairs(queens)

    while number_iterations < max_iterations:
        number_iterations += 1

        if heuristicValue == 0:
            break

        chosenQueen = -1
        chosenColumn = -1
        bestHeuristicValue = heuristicValue

        for i in range(n):
            tmpCol = queens[i]

            for j in range(n):
                if queens[i] == tmpCol:
                    continue

                queens[i] = j
                newHeuristicValue = attacking_pairs(queens)

                if newHeuristicValue < bestHeuristicValue:
                    bestHeuristicValue = newHeuristicValue
                    chosenQueen = i
                    chosenColumn = j

                queens[i] = tmpCol

        if heuristicValue == bestHeuristicValue:
            queens = list(range(n))
            shuffle(queens)
        elif bestHeuristicValue < heuristicValue:
            heuristicValue = bestHeuristicValue
            queens[chosenQueen] = chosenColumn

    return (queens, heuristicValue, number_iterations)
