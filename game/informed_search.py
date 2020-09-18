import numpy as np
from .state import State
import sys
import enum
from typing import List, Tuple, Optional
from math import sqrt, floor

"""
This class implement the Best-First-Search (BFS) algorithm along with the Heuristic search strategies

In this algorithm, an OPEN list is used to store the unexplored states and 
a CLOSE list is used to store the visited state. OPEN list is a priority queue. 
The priority is insured through sorting the OPEN list each time after new states are generated 
and added into the list. The heuristics are used as sorting criteria.

In this informed search, reducing the state space search complexity is the main criterion. 
We define heuristic evaluations to reduce the states that need to be checked every iteration. 
Evaluation function is used to express the quality of informedness of a heuristic algorithm. 
"""


class GeneratedStateType(enum.Enum):
    NEITHER = 1
    ON_OPEN = 2
    ON_CLOSED = 3


class InformedSearchSolver:
    """Implements Best First Search
    """

    opened: List[State] = []
    closed: List[State] = []
    depth = 0

    def __init__(self, current: State, target: State):
        self.current_state = current
        self.target_state = target

        if not self.is_solvable():
            raise RuntimeError("Unsolvable")

        self.opened = [current]

    def check_inclusive(self, item: State) -> Tuple[GeneratedStateType, int]:
        """ Check if the generated state is in open and/or closed. """
        is_in_closed = item in self.closed
        is_in_open = item in self.opened

        index = -1
        state_type = GeneratedStateType.NEITHER

        if is_in_closed:
            index = self.closed.index(item)

        if is_in_open:
            index = self.opened.index(item)

        if is_in_open and not is_in_closed:
            state_type = GeneratedStateType.ON_OPEN
        elif not is_in_open and is_in_closed:
            state_type = GeneratedStateType.ON_CLOSED

        return state_type, index

    def check_conditions(self, child: State):
        """ Checks the inclusivity in the open/closed lists and moves the states accordingly.

        Args:
            `state` - State object
        """
        state_type, index = self.check_inclusive(child)

        if state_type is GeneratedStateType.NEITHER:

            child.weight = child.heuristic_score(self.target_state, self.depth)

            self.opened.append(child)

        elif state_type is GeneratedStateType.ON_OPEN:
            if child.depth < self.current_state.depth:
                self.opened[index].depth = child.depth

        else:
            if child.depth < self.current_state.depth:
                self.closed.remove(child)
                self.opened.append(child)

    def next_state(self):
        """Find next state"""
        if self.is_solved():
            raise StopIteration
        observed_state = self.opened.pop(0)
        self.closed.append(observed_state)

        # Get current states graph.
        self.depth = observed_state.depth + 1

        for item in observed_state.neighbors():
            self.check_conditions(item)

        # Sort the open list first by h(n) then g(n).
        self.opened.sort(key=lambda a: a.weight)
        self.current_state = self.opened[0]

    def is_solved(self) -> bool:
        """Checks if the search has found a solution

        Returns:
            bool: is puzzle solved
        """
        return self.current_state == self.target_state

    def is_solvable(self) -> bool:
        """Detects if the current puzzle has a solution

        Returns:
            bool: if the puzzle is solvable
        """

        return self.current_state.tile_reversals(self.target_state) % 2 == 0

    def run(self) -> int:
        """Runs the search"""
        iterations = 0
        while not self.is_solved():
            print(self.current_state)
            self.next_state()
            iterations += 1

        return iterations
