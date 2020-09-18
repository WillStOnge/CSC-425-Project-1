import unittest
from game.state import State
from game.informed_search import InformedSearchSolver
import numpy as np


class TestInformedSearch(unittest.TestCase):
    def test_next_state(self):
        init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        informed_solver = InformedSearchSolver(init, goal)

        self.assertEqual(len(informed_solver.opened), 1)
        self.assertEqual(len(informed_solver.closed), 0)
        informed_solver.next_state()

        self.assertEqual(len(informed_solver.opened), 3)
        self.assertEqual(len(informed_solver.closed), 1)
        informed_solver.next_state()

        self.assertEqual(len(informed_solver.opened), 5)
        self.assertEqual(len(informed_solver.closed), 2)
        informed_solver.next_state()

        with self.assertRaises(StopIteration):
            informed_solver.next_state()

