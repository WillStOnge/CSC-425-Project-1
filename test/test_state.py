import unittest
from game.state import State
import numpy as np


class TestState(unittest.TestCase):
    def test_move_up(self):
        initial_state = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
        expected_state = np.array([[0, 2, 3], [1, 4, 6], [7, 5, 8]])

        old_state = State(initial_state, 0, 0)
        new_state = old_state.move("up")

        self.assertTrue(np.all(new_state.tile_seq == expected_state))
        self.assertTrue(np.all(old_state.tile_seq == initial_state))

        initial_state = np.array([[0, 2, 3], [1, 4, 6], [7, 5, 8]])
        state = State(initial_state, 0, 0)

        with self.assertRaises(IndexError):
            state.move("up")

    def test_move_right(self):
        initial_state = np.array([[1, 2, 3], [4, 0, 6], [7, 5, 8]])
        expected_state = np.array([[1, 2, 3], [4, 6, 0], [7, 5, 8]])
        old_state = State(initial_state, 0, 0)
        new_state = old_state.move("right")

        self.assertTrue(np.all(new_state.tile_seq == expected_state))

        initial_state = np.array([[1, 2, 3], [4, 5, 0], [6, 7, 8]])
        state = State(initial_state, 0, 0)

        with self.assertRaises(IndexError):
            state.move("right")

    def test_move_down(self):
        initial_state = np.array([[0, 2, 3], [1, 4, 6], [7, 5, 8]])
        expected_state = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])

        old_state = State(initial_state, 0, 0)
        new_state = old_state.move("down")

        self.assertTrue(np.all(new_state.tile_seq == expected_state))
        self.assertTrue(np.all(old_state.tile_seq == initial_state))

        initial_state = np.array([[1, 2, 3], [4, 5, 4], [0, 7, 8]])
        state = State(initial_state, 0, 0)

        with self.assertRaises(IndexError):
            state.move("down")

    def test_move_left(self):
        initial_state = np.array([[1, 2, 3], [4, 0, 6], [7, 5, 8]])
        expected_state = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])

        old_state = State(initial_state, 0, 0)
        new_state = old_state.move("left")

        self.assertTrue(np.all(new_state.tile_seq == expected_state))
        self.assertTrue(np.all(old_state.tile_seq == initial_state))

        initial_state = np.array([[1, 2, 3], [0, 4, 5], [6, 7, 8]])
        state = State(initial_state, 0, 0)

        with self.assertRaises(IndexError):
            state.move("left")

    def test_neighbors(self):
        initial_state = State(np.array([[1, 2, 3], [4, 0, 6], [7, 5, 8]]))
        up_state = State(np.array([[1, 0, 3], [4, 2, 6], [7, 5, 8]]))
        right_state = State(np.array([[1, 2, 3], [4, 6, 0], [7, 5, 8]]))
        down_state = State(np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]]))
        left_state = State(np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]]))
        neighbors = initial_state.neighbors()
        self.assertTrue(
            np.all(
                np.array([x.tile_seq for x in neighbors])
                == np.array(
                    [
                        right_state.tile_seq,
                        left_state.tile_seq,
                        up_state.tile_seq,
                        down_state.tile_seq,
                    ]
                )
            )
        )

    def test_misplaced_tiles(self):
        init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        self.assertEqual(init.misplaced_tiles(goal), 4)

    def test_reversed_tiles(self):
        # Test row swaps
        init_tile = np.array([[1, 2, 3], [4, 6, 5], [8, 7, 0]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        self.assertEqual(init.tile_reversals(goal), 2)

        # Test column swaps
        init_tile = np.array([[1, 2, 6], [4, 8, 3], [7, 5, 0]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        self.assertEqual(init.tile_reversals(goal), 2)

        # Test both
        init_tile = np.array([[1, 2, 6], [4, 5, 3], [8, 7, 0]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        self.assertEqual(init.tile_reversals(goal), 2)

    def test_euclidean_distance(self):
        init_tile = np.array([[1, 2, 3], [0, 4, 6], [7, 5, 8]])
        goal_tile = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        self.assertEqual(init.euclidean_distance(goal), 5)

        init_tile = np.array([[3, 8, 7], [0, 4, 6], [2, 1, 5]])
        goal_tile = np.array([[0, 4, 3], [2, 6, 7], [5, 8, 1]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        self.assertEqual(init.euclidean_distance(goal), 12)

        init_tile = np.array([[0, 2, 3], [1, 4, 5], [8, 7, 6]])
        goal_tile = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

        init = State(init_tile, 0, 0)
        goal = State(goal_tile, 0, 0)

        self.assertEqual(init.euclidean_distance(goal), 7)
