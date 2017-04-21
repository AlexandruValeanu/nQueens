from ortools.constraint_solver import pywrapcp


def solve(N):
    # Create the solver
    solver = pywrapcp.Solver("n-queens")

    # Create the variables
    queens = [solver.IntVar(0, N - 1, "x{0}".format(i)) for i in range(N)]

    # No two queens can be on the same diagonal.
    solver.Add(solver.AllDifferent(queens))
    solver.Add(solver.AllDifferent([queens[i] + i for i in range(N)]))
    solver.Add(solver.AllDifferent([queens[i] - i for i in range(N)]))

    db = solver.Phase(queens, solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)

    solver.NewSearch(db)

    if solver.NextSolution():
        for q in queens:
            print(q.Value(), end=" ")
        print()
    else:
        print("No solution found!")

    solver.EndSearch()
    print("Time: ", solver.WallTime(), "ms")
