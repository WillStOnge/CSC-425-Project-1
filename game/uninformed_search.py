from .state import State
from typing import Set
from collections import deque
import numpy as np


"""
This class implement one of the Uninformed Search algorithm
You may choose to implement the Breadth-first or Depth-first or
Iterative-Deepening search algorithm

"""


class UninformedSearchSolver:
    opened = deque()    # Fronteer
    closed = set()  # Explored
    depth = 0

    def __init__(self, current: State, target: State):
        self.current_state = current
        self.target_state = target
        self.opened.append(current)

    # def check_inclusive(self, s):
    #     # your code start here
    #     pass

    def is_solvable(self):
        inv_count = 0

        for i in range(0, 9):
            for j in range(i+1, 9):
                #  // Value 0 is used for empty space
                if (self.current_state.flatten()[j] and self.current_state.flatten()[i] and self.current_state.flatten()[i] > self.current_state.flatten()[j]):
                    inv_count += 1
        return inv_count % 2 == 0

    def state_walk(self):
        """
        * four types of walks
        * best first search
        *  ↑ ↓ ← → (move up, move down, move left, move right)
        * the blank tile is represent by '0'
        """

        observed_state: State = self.opened.popleft()
        if not self.is_solvable():
            print("UNSOLVABLE")
            return

        if observed_state not in self.closed:
            self.current_state = observed_state

            self.closed.add(observed_state)
            neighbors = observed_state.neighbors()

            for neighbor in neighbors:
                self.opened.append(neighbor)

        return self.opened
        # if np.all(observed_state == self.target_state):
        #     return observed_state
        # self.current_state = observed_state

        # self.closed.append(observed_state)

        # for neighbor in observed_state.neighbors():
        #     if neighbor not in self.closed or neighbor not in self.opened:
        #         print("appending")
        #         self.opened.append(neighbor)

        # possible_states = [
        #     x
        #     for x in observed_state.neighbors()
        #     if x not in self.closed and x not in self.opened
        # ]
        # [self.opened.append(x) for x in possible_states]

    # Check the following to make it work properly

    def run(self):
        # output the start state
        print(f"Initial State: \n{self.current_state.tile_seq}")
        print("---------")
        path = 0

        while not self.current_state == self.target_state:
            self.state_walk()
            # print(succ)
            print(f"State: {path+1}")
            print(self.current_state.tile_seq)
            print("--------")
            path += 1

        # print(self.current_state.tile_seq)
        # path += 1

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current_state.depth)
        # output the goal state
        target = self.target_state.tile_seq
        print(target)
        print("goal state !!!!!")
