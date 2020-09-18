from .state import State
from collections import deque
import numpy as np
import sys
from typing import Set


class UninformedSearchSolver:
    """Implements BFS to find a solution to an 8-puzzle problem"""

    opened: deque = deque()
    closed: Set[State] = set()
    depth = 0

    def __init__(self, current: State, target: State):
        """Creates State object.

        Args:
            current (State): Initial State
            target (State): Target State
        """

        self.current_state = current
        self.target_state = target

        if not self.is_solvable(self.current_state):
            raise RuntimeError("Unsolvable")

        self.opened.append(current)

    def next_state(self):
        """Finds next state that the puzzle can be and loads it for processing

        previously known as:'state_walk'

        """

        if self.is_solved():
            raise StopIteration

        observed_state: State = self.opened.popleft()
        self.closed.add(observed_state)

        self.current_state = observed_state
        self.depth = observed_state.depth

        for neighbor in observed_state.neighbors():
            if neighbor not in self.closed and neighbor not in self.opened:
                self.opened.append(neighbor)

    def is_solved(self) -> bool:
        """Checks if the search has found a solution

        Returns:
            bool: is puzzle solved
        """
        return self.current_state == self.target_state

    def is_solvable(self, state: State) -> bool:

        return self.tile_reversals(self.current_state) % 2 == 0

    def tile_reversals(self, state: State) -> int:
        """Counts tiles that are reversed to each other

        Returns:
            int: reversed tiles
        """
        reversals = 0

        current_tiles = state.tile_seq
        for row, col in np.ndindex(current_tiles.shape):
            if row != 2:
                if state[row][col] == self.target_state[row + 1][col]:
                    reversals += 1
            if col != 2:
                if state[row][col] == self.target_state[row][col + 1]:
                    reversals += 1

        return reversals

    def run(self) -> int:
        """Runs the search"""
        iterations = 0

        while not self.is_solved():
            self.next_state()
            iterations += 1

        return iterations
