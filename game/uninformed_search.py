from .state import State
from collections import deque
import numpy as np


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

    def is_solvable(self) -> bool:
        """Detects if the current puzzle has a solution

        Returns:
            bool: if the puzzle is solvable
        """
        inv_count = 0
        arr = self.current_state.flatten()
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if arr[j] and arr[i] and arr[i] > arr[j]:
                    inv_count += 1
        return inv_count % 2 == 0

    def next_state(self):
        """Finds next state that the puzzle can be and loads it for processing

        previously known as:'state_walk'
        """
        observed_state: State = self.opened.popleft()
        if not self.is_solvable():
            print("UNSOLVABLE")
            return

        if np.all(observed_state == self.target_state):
            self.current_state = observed_state
            return

        self.closed.add(observed_state)

        for neighbor in observed_state.neighbors():
            if neighbor not in self.closed or neighbor not in self.opened:
                self.opened.append(neighbor)

    def run(self):
        """Runs the search
        """
        # output the start state
        print(f"Initial State: \n{self.current_state.tile_seq}")
        print("---------")
        path = 0

        while not self.current_state == self.target_state:
            self.next_state()
            print(f"State: {path+1}")
            # print(self.current_state.tile_seq)
            print("--------")
            path += 1

        # print(self.current_state.tile_seq)
        # path += 1

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current_state.depth)
        # output the goal state
        print(self.target_state.tile_seq)
        print("goal state !!!!!")
