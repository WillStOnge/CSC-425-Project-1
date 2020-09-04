"""
Solving Eight Puzzle Game using Search Strategies
The eight-puzzle game is a 3 × 3 version of the 15-puzzle in which eight tiles can be moved around in nine spaces.
CSC 425 525 Artificial Intelligence
Instructor: Dr. Junxiu Zhou
Semester: Fall 2020

Your names: Arseny Poga, Will St. Onge, and Trey Regruth
"""

import numpy as np
from game.state import State
from game.uninformed_search import UninformedSearchSolver
from game.informed_search import InformedSearchSolver


def main():
    # initialize the init state and goal state as 2d array
    init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
    goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

    # 123046758

    init = State(init_tile, 0, 0)
    goal = State(goal_tile, 0, 0)

    # uninformed_solver = UninformedSearchSolver(init, goal)
    # uninformed_solver.run()

    informed_solver = InformedSearchSolver(init, goal)
    informed_solver.run()


if __name__ == "__main__":
    main()
