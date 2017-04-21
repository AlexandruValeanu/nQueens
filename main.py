import nqueens_csp
from heuristics import *

if __name__ == '__main__':
    queens = nqueens_csp.solve(1000)
    print(queens)