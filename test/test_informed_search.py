import unittest
from game.state import State
from game.informed_search import InformedSearchSolver
import numpy as np


class TestInformedSearch(unittest.TestCase):
    def test_misplaced_tiles(self):
        init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        informed_solver = InformedSearchSolver(init, goal)
        tile = informed_solver.misplaced_tiles(init)

        self.assertEqual(tile, 4)

    def test_reversed_tiles(self):
        # Test row swaps
        init_tile = np.array([[1, 2, 3], [4, 6, 5], [8, 7, 0]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        informed_solver = InformedSearchSolver(init, goal)
        tile = informed_solver.tile_reversals(init)

        self.assertEqual(tile, 2)

        # Test column swaps
        init_tile = np.array([[1, 2, 6], [4, 8, 3], [7, 5, 0]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        informed_solver = InformedSearchSolver(init, goal)
        tile = informed_solver.tile_reversals(init)

        self.assertEqual(tile, 2)

        # Test both
        init_tile = np.array([[1, 2, 6], [4, 5, 3], [8, 7, 0]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        informed_solver = InformedSearchSolver(init, goal)
        tile = informed_solver.tile_reversals(init)

        self.assertEqual(tile, 2)

    def test_euclidean_distance(self):
        init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        informed_solver = InformedSearchSolver(init, goal)
        tile = informed_solver.euclidean_distance(init)

        self.assertEqual(tile, 5)

        init_tile = np.array([[3, 8, 7], [0, 4, 6], [2, 1, 5]])
        goal_tile = np.array([[0, 4, 3], [2, 6, 7], [5, 8, 1]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        informed_solver = InformedSearchSolver(init, goal)
        tile = informed_solver.euclidean_distance(init)

        self.assertEqual(tile, 12)

        init_tile = np.array([[0, 2, 3], [1, 4, 5], [8, 7, 6]])
        goal_tile = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        informed_solver = InformedSearchSolver(init, goal)
        tile = informed_solver.euclidean_distance(init)

        self.assertEqual(tile, 7)

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

