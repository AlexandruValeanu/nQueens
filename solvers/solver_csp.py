from ortools.constraint_solver import pywrapcp


def solve(number_queens):
    n = number_queens

    # Create the solver
    solver = pywrapcp.Solver("n-queens")

    # Create the variables
    queens = [solver.IntVar(0, n - 1, "x{0}".format(i)) for i in range(n)]

    # No two queens can be on the same diagonal.
    solver.Add(solver.AllDifferent(queens))
    solver.Add(solver.AllDifferent([queens[i] + i for i in range(n)]))
    solver.Add(solver.AllDifferent([queens[i] - i for i in range(n)]))

    db = solver.Phase(queens, solver.CHOOSE_MIN_SIZE_LOWEST_MAX, solver.ASSIGN_CENTER_VALUE)
    solver.NewSearch(db)

    list_queens = []

    if solver.NextSolution():
        for q in queens:
            list_queens.append(q.Value())

    solver.EndSearch()
    return list_queens
