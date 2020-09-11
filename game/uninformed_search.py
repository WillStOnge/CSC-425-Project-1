from .state import State
from collections import deque
import numpy as np
import ipdb


class UninformedSearchSolver:
    """Implements BFS to find a solution to an 8-puzzle problem
    """

    opened = deque()
    closed = set()
    depth = 0

    def __init__(self, current: State, target: State):
        self.current_state = current
        self.target_state = target
        self.opened.append(current)

    def next_state(self):
        """Finds next state that the puzzle can be and loads it for processing

        previously known as:'state_walk'

        """
        if not self.current_state.is_solvable():
            print("UNSOLVABLE")
            exit(1)

        observed_state: State = self.opened.popleft()

        if np.all(observed_state.tile_seq == self.target_state.tile_seq):
            self.current_state = observed_state

        self.closed.add(observed_state)

        for neighbor in observed_state.neighbors():
            # print(neighbor in self.closed)
            if neighbor not in self.closed and neighbor not in self.opened:
                self.opened.append(neighbor)

    def is_solved(self) -> bool:
        return self.current_state == self.target_state

    def run(self) -> int:
        """Runs the search"""
        print(f"Initial State: \n{self.current_state.tile_seq}")
        print("---------")
        path = 0

        while not self.is_solved():
            self.next_state()
            path += 1

        print(self.current_state.tile_seq)

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current_state.depth)
        # output the goal state
        print(self.target_state.tile_seq)
        print("goal state !!!!!")
        return path
