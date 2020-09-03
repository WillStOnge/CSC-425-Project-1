import unittest
from game.state import State
from game.uninformed_search import UninformedSearchSolver
import numpy as np


class TestUninformedSolver(unittest.TestCase):
    def test_state_walk(self):
        init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
        # init_tile = np.array([[1, 2, 3], [4, 5, 0], [7, 8, 6]])
        init = State(init_tile, 0, 0)

        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        goal = State(goal_tile, 0, 0)

        uninformed_solver = UninformedSearchSolver(init, goal)
        while not uninformed_solver.current_state == uninformed_solver.target_state:
            uninformed_solver.next_state()
            # print(succ)
        self.assertTrue(
            np.all(goal.tile_seq == uninformed_solver.current_state.tile_seq)
        )
