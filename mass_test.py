from game.informed_search import InformedSearchSolver
from game.uninformed_search import UninformedSearchSolver
from game.state import State
import numpy as np
import sys
import os

def mass_test(iterations: int):
    for i in range(iterations):
        arr = np.arange(9).reshape((3, 3))
        np.random.shuffle(arr)
        init_state = State(arr)

        arr1 = np.arange(9).reshape((3, 3))
        np.random.shuffle(arr1)
        goal_state = State(arr1)

        informed_solver = InformedSearchSolver(init_state, goal_state)
        uninformed_solver = UninformedSearchSolver(init_state, goal_state)

        try:
            sys.stdout = open(os.devnull, 'w')
            informed_path = informed_solver.run(100)
            uninformed_path = uninformed_solver.run(100)
            sys.stdout = sys.__stdout__

            if informed_path > uninformed_path:
                print('Iteration', i, '- Informed path was longer than the uninformed')
                print(init_state.tile_seq)
                print('----------')
                print(goal_state.tile_seq)
        except Exception:
            continue

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python mass_test.py testCount')
        exit(1)
    mass_test(int(sys.argv[1]))
    