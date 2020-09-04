import numpy as np
from .state import State

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


class InformedSearchSolver:
    opened = []
    closed = []
    depth = 0

    def __init__(self, current: State, target: State):
        self.current_state = current
        self.target_state = target
        self.opened.append(current)

    def check_inclusive(self, item: State):
        """ Check if the generated state is in open or closed. """
        in_open = 0
        in_closed = 0
        ret = [-1, -1]

        if item in self.opened:
            in_open = 1
            ret[1] = self.opened.index(item)

        if item in self.closed:
            in_closed = 1
            ret[1] = self.closed.index(item)

        if in_open == 0 and in_closed == 0:
            ret[0] = 1  # the child is not in open or closed
        elif in_open == 1 and in_closed == 0:
            ret[0] = 2  # the child is already in open
        elif in_open == 0 and in_closed == 1:
            ret[0] = 3  # the child is already in closed
        return ret

    """ Checks the inclusivity in the open/closed lists and moves the states accordingly. """
    def check_conditions(self, child: State):
        flag = self.check_inclusive(child)

        if flag[0] == 1: # State is in neither list
            self.heuristic_test(child)
            self.openList.append(child)
        elif flag[0] == 2: # State is in the open list
            if child.depth < self.current.depth:
                test = None # Give the state on open the shorter path
        else: # State is in the closed list
            if child.depth < self.current.depth:
                self.closeList.remove(child)
                self.openList.append(child)

    def next_state(self):
        """Four possible directions (up, down, left, and right).
        
        Uses the best first search algorithm. The blank tile is represent by '0'.
        """
        # Add closed state
        self.closed.append(self.current_state)
        self.opened.remove(self.current_state)
        # Move to the next heuristic state
        current_state = self.current_state.tile_seq

        coordinates = np.argwhere(current_state == 0).flatten()
        col, row = coordinates[1], coordinates[0]

        self.depth += 1

        # Move up
        if (row - 1) >= 0:
            temp_state = self.current_state.move("up")
            self.check_conditions(temp_state)

        # Move down
        if (row + 1) < len(current_state):
            temp_state = self.current_state.move("down")
            self.check_conditions(temp_state)

        # Move left
        if (col - 1) >= 0:
            temp_state = self.current_state.move("left")
            self.check_conditions(temp_state)

        # Move right
        if (col + 1) < len(current_state):
            temp_state = self.current_state.move("right")
            self.check_conditions(temp_state)

        # Sort the open list first by h(n) then g(n)
        self.opened.sort(key=lambda a: a.weight)
        self.current_state = self.opened[0]

    def heuristic_test(self):
        """Solve the game using heuristic search strategies
        
        * There are three types of heuristic rules:
        * (1) Tiles out of place
        * (2) Sum of distances out of place
        * (3) 2 x the number of direct tile reversals
        
        * evaluation function
        * f(n) = g(n) + h(n)
        * g(n) = depth of path length to start state
        * h(n) = (1) + (2) + (3)
        """
        h1 = self.misplaced_tiles()
        h2 = self.misplaced_distances()
        h3 = 2 * self.tile_reversals()

        # Set the heuristic value for current state
        self.current_state.weight = self.current_state.depth + h1 + h2 + h3

    def misplaced_tiles(self) -> int:
        """Counts all misplaced tiles

        Returns:
            int: misplaced tile count
        """
        return np.sum(self.current_state.tile_seq != self.target_state.tile_seq)

    def misplaced_distances(self) -> int:
        distance = 0
        current_tiles = self.current_state.tile_seq
        target_tiles = self.target_state.tile_seq
        for current_x, current_y in np.ndindex(current_tiles.shape):
            for goal_x, goal_y in np.ndindex(target_tiles.shape):
                if (
                    self.current_state[current_y][current_x]
                    == self.target_state[goal_y][goal_x]
                ):
                    distance += abs(current_y - goal_y) + abs(current_x - goal_x)
        return distance

    def tile_reversals(self) -> int:
        """Counts tiles that are reversed to each other

        Returns:
            int: reversed tiles
        """
        reversals = 0

        current_tiles = self.current_state.tile_seq
        for row in range(len(current_tiles)):
            for col in range(len(current_tiles[row])):
                if row != 2:
                    if self.current_state[row][col] == self.target_state[row + 1][col]:
                        reversals += 1
                if col != 2:
                    if self.current_state[row][col] == self.target_state[row][col + 1]:
                        reversals += 1

        return reversals

    # You can choose to print all the states on the search path, or just the start and goal state
    def run(self):
        print("Start State:")
        print(self.current_state.tile_seq)

        path = 0

        while not self.current_state == self.target_state:
            self.next_state()
            # print(self.current_state.tile_seq)
            path += 1

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current_state.depth)
        print("Goal State:")
        print(self.target_state.tile_seq)
