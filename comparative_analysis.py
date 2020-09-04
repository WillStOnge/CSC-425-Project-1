from game.state import State
from game.informed_search import InformedSearchSolver
from game.uninformed_search import UninformedSearchSolver
import numpy as np
import time

def compare_time():
    init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
    goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    init = State(init_tile)
    goal = State(goal_tile)

    print('Informed search took {:.4f} milliseconds'.format(time_informed(init, goal) * 1000))
    print('Uninformed search took {:.4f} milliseconds'.format(time_uninformed(init, goal) * 1000))

def time_informed(init: State, goal: State) -> float:
    start = time.time()
    solver = InformedSearchSolver(init, goal)

    while not solver.current_state == solver.target_state:
            solver.next_state()

    #solver.run()

    end = time.time()
    return end - start

def time_uninformed(init: State, goal: State) -> float:
    start = time.time()
    solver = UninformedSearchSolver(init, goal)

    while not solver.current_state == solver.target_state:
            solver.next_state()

    #solver.run()
            
    end = time.time()
    return end - start

if __name__ == "__main__":
    compare_time()