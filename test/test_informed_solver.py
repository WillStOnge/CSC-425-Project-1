import unittest
from game.state import State
from game.informed_search import InformedSearchSolver
import numpy as np


class TestInformedSolver(unittest.TestCase):
    def test_next_state(self):
        init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        informed_solver = InformedSearchSolver(init, goal)
        path = 0
        while not informed_solver.is_solved():
            informed_solver.next_state()
            path += 1

        self.assertEqual(path, 4)

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
        init_tile = np.array([[1, 2, 3], [4, 5, 6], [8, 7, 0]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        informed_solver = InformedSearchSolver(init, goal)
        tile = informed_solver.tile_reversals(init)

        self.assertEqual(tile, 1)

        # Test column swaps
        init_tile = np.array([[1, 2, 6], [4, 5, 3], [7, 8, 0]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        informed_solver = InformedSearchSolver(init, goal)
        tile = informed_solver.tile_reversals(init)

        self.assertEqual(tile, 1)

        # Test both
        init_tile = np.array([[1, 2, 6], [4, 5, 3], [8, 7, 0]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        informed_solver = InformedSearchSolver(init, goal)
        tile = informed_solver.tile_reversals(init)

        self.assertEqual(tile, 2)
