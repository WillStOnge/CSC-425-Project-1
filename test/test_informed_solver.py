import unittest
from game.state import State
from game.informed_search import InformedSearchSolver
import numpy as np


class TestInformedSolver(unittest.TestCase):
    def test_state_walk(self):
        init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
        # init_tile = np.array([[1, 2, 3], [4, 5, 0], [7, 8, 6]])
        init = State(init_tile, 0, 0)

        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        goal = State(goal_tile, 0, 0)

        informed_solver = InformedSearchSolver(init, goal)
        """
        while not informed_solver.current_state == informed_solver.target_state:
            informed_solver.next_state()
        """
        informed_solver.run()
        self.assertTrue(np.all(goal.tile_seq == informed_solver.current_state.tile_seq))