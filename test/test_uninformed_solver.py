import unittest
from game.state import State
from game.uninformed_search import UninformedSearchSolver
import numpy as np
import ipdb


class TestUninformedSolver(unittest.TestCase):
    def test_state_walk(self):
        init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        uninformed_solver = UninformedSearchSolver(init, goal)

        self.assertEqual(len(uninformed_solver.opened), 1)
        self.assertEqual(len(uninformed_solver.closed), 0)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 3)
        self.assertEqual(len(uninformed_solver.closed), 1)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 5)
        self.assertEqual(len(uninformed_solver.closed), 2)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 5)
        self.assertEqual(len(uninformed_solver.closed), 3)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 5)
        self.assertEqual(len(uninformed_solver.closed), 4)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 6)
        self.assertEqual(len(uninformed_solver.closed), 5)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 7)
        self.assertEqual(len(uninformed_solver.closed), 6)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 8)
        self.assertEqual(len(uninformed_solver.closed), 7)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 9)
        self.assertEqual(len(uninformed_solver.closed), 8)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 10)
        self.assertEqual(len(uninformed_solver.closed), 9)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 10)
        self.assertEqual(len(uninformed_solver.closed), 10)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 10)
        self.assertEqual(len(uninformed_solver.closed), 11)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 10)
        self.assertEqual(len(uninformed_solver.closed), 12)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 10)
        self.assertEqual(len(uninformed_solver.closed), 13)
        uninformed_solver.next_state()

        self.assertEqual(len(uninformed_solver.opened), 10)
        self.assertEqual(len(uninformed_solver.closed), 14)
        uninformed_solver.next_state()
