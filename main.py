import solvers.solver_csp
import time

start = time.time()
print(solvers.solver_csp.solve(5000))
end = time.time()
print(end - start)

