import solvers.solver_minimum_conflicts
import time

start = time.time()
print(solvers.solver_minimum_conflicts.solve(500))
end = time.time()
print(end - start)

