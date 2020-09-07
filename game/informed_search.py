import numpy as np
from .state import State
import sys
import enum

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
    """[summary]

    Raises:
        Exception: [description]

    Returns:
        [type]: [description]
    """

    opened = []
    closed = []
    depth = 0

    def __init__(self, current: State, target: State):
        self.current_state = current
        self.target_state = target
        self.opened.append(current)

    def check_inclusive(self, item: State) -> (GeneratedStateType, int):
        """ Check if the generated state is in open and/or closed. """
        is_in_closed = item in self.closed
        is_in_open = item in self.opened

        index = None
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
            child.weight = self.heuristic_score(child)
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

        if not self.current_state.is_solvable():
            raise RuntimeError("Unsolvable")

        self.closed.append(self.current_state)
        self.opened.remove(self.current_state)

        # Get current states graph.
        current_state = self.current_state.tile_seq
        (row, col) = np.argwhere(current_state == 0).flatten()
        self.depth += 1

        if (row - 1) >= 0:
            temp_state = self.current_state.move("up")
            self.check_conditions(temp_state)

        if (row + 1) < len(current_state):
            temp_state = self.current_state.move("down")
            self.check_conditions(temp_state)

        if (col - 1) >= 0:
            temp_state = self.current_state.move("left")
            self.check_conditions(temp_state)

        if (col + 1) < len(current_state):
            temp_state = self.current_state.move("right")
            self.check_conditions(temp_state)

        # Sort the open list first by h(n) then g(n).
        self.opened.sort(key=lambda a: a.weight)
        self.current_state = self.opened[0]

    def heuristic_score(self, state: State):
        """Sets the weight to the heuristic value
        
        Solve the game using heuristic search strategies
        
        * There are three types of heuristic rules:
        * (1) Tiles out of place
        * (2) Sum of distances out of place
        * (3) 2 x the number of direct tile reversals
        
        * evaluation function
        * f(n) = g(n) + h(n)
        * g(n) = depth of path length to start state
        * h(n) = (1) + (2) + (3)
        """
        h1 = self.misplaced_tiles(state)
        h2 = self.misplaced_distances(state)
        h3 = 2 * self.tile_reversals(state)

        # Set the heuristic value for current state
        return state.depth + h1 + h2 + h3

    def misplaced_tiles(self, state: State) -> int:
        """Counts all misplaced tiles

        Returns:
            int: misplaced tile count
        """
        return np.sum(state.tile_seq != self.target_state.tile_seq)

    def misplaced_distances(self, state: State) -> int:
        distance = 0
        current_tiles = state.tile_seq
        target_tiles = self.target_state.tile_seq
        for current_x, current_y in np.ndindex(current_tiles.shape):
            for goal_x, goal_y in np.ndindex(target_tiles.shape):
                if state[current_y][current_x] == self.target_state[goal_y][goal_x]:
                    distance += abs(current_y - goal_y) + abs(current_x - goal_x)

        return distance

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

    def is_solved(self) -> bool:
        """Checks if the search has found a solution

        Returns:
            bool: is puzzle solved
        """
        return self.current_state == self.target_state

    # You can choose to print all the states on the search path, or just the start and goal state
    def run(self) -> int:
        path = 0
        while not self.is_solved():
            self.next_state()
            path += 1

        return path, self.depth
