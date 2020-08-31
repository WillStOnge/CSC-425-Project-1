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
    current = State()
    goal = State()
    openList = []
    closeList = []
    depth = 0

    def __init__(self, current, goal):
        self.current = current
        self.goal = goal
        self.openList.append(current)

    def sortFun(self, e):
        return e.weight


    def check_inclusive(self, s):
        """ Check if the generated state is in open or closed. """
        in_open = 0
        in_closed = 0
        ret = [-1, -1]

        if item is in self.openList:
            in_open = 1
            ret[1] = self.openList.index(item)

        if item is in self.closeList
            in_closed = 1
            ret[1] = self.closeList.index(item)

        if in_open == 0 and in_closed == 0:
            ret[0] = 1  # the child is not in open or closed
        elif in_open == 1 and in_closed == 0:
            ret[0] = 2  # the child is already in open
        elif in_open == 0 and in_closed == 1:
            ret[0] = 3  # the child is already in closed
        return ret

    def check_conditions(self, state: State):
        """ Checks the inclusivity in the open/closed lists and moves the states accordingly.
        Args:
            `state` - State object
        """
        flag = self.check_inclusive(state)

        if flag[0] == 1:  # State is in neither list
            self.heuristic_test(state)
            openList.append(state)
        elif flag[0] == 2:  # State is in the open list
            if state.depth < self.current.depth:
                test = None  # Give the state on open the shorter path
        else:  # State is in the closed list
            if state.depth < self.current.depth:
                closeList.remove(state)
                openList.append(state)

    def next_state(self):
        """Four possible directions (up, down, left, and right).
        
        
        Uses the best first search algorithm. The blank tile is represent by '0'.
        """
        # Add closed state
        self.closeList.append(self.current)
        self.openList.remove(self.current)
        # Move to the next heuristic state
        walk_state = self.current.tile_seq

        coordinates = np.argwhere(new_state.tile_seq == 0).flatten()
        col, row = coordinates[1], coordinates[0]

        self.depth += 1

        # Move up
        if (row - 1) >= 0:
            tempState = self.current.move("up")
            self.check_conditions(tempState)

        # Move down
        if (row + 1) < len(walk_state):
            tempState = self.current.move("down")
            self.check_conditions(tempState)

        # Move left
        if (col - 1) >= 0:
            tempState = self.current.move("left")
            self.check_conditions(tempState)

        # Move right
        if (col + 1) < len(walk_state):
            tempState = self.current.move("right")
            self.check_conditions(tempState)

        # Sort the open list first by h(n) then g(n)
        self.openList.sort(key=lambda a: a.weight)
        self.current = self.openList[0]

    def heuristic_test(self, current):
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
        curr_seq = current.tile_seq
        goal_seq = self.goal.tile_seq

        # (1) Tiles out of place
        
        h1 = np.sum(curr_seq != goal_seq)
        
        # (2) Sum of distances out of place
        h2 = 0
        for curr_row in range(len(curr_seq)):
            for curr_col in range(len(curr_seq[curr_row])):
                for goal_row in range(len(goal_seq)):
                    for goal_col in range(len(goal_seq[goal_row])):
                        if curr_seq[curr_row][curr_col] == goal_seq[goal_row][goal_col]:
                            h2 += abs(curr_row - goal_row) + abs(curr_col - goal_col)

        # (3) Twice the number of direct tile reversals
        h3 = 0
        for row in range(len(goal_seq) - 1):
            for col in range(len(goal_seq[row]) - 1):
                if (
                    goal_seq[row][col] == curr_seq[row + 1][col]
                    and goal_seq[row + 1][col] == curr_seq[row][col]
                    and curr_seq[row][col] != 0
                    and curr_seq[row + 1][col] != 0
                ):
                    h3 += 1
                elif (
                    goal_seq[row][col] == curr_seq[row][col + 1]
                    and goal_seq[row][col + 1] == curr_seq[row][col]
                    and curr_seq[row][col] != 0
                    and curr_seq[row][col + 1] != 0
                ):
                    h3 += 1
        h3 *= 2

        # Set the heuristic value for current state
        current.weight = current.depth + h1 + h2 + h3

    # You can choose to print all the states on the search path, or just the start and goal state
    def run(self):
        print("Start State:")
        print(self.current.tile_seq)

        path = 0

        while not self.current.equals(self.goal):
            self.next_state()
            print(self.current.tile_seq)
            path += 1

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current.depth)
        print("Goal State:")
        print(self.goal.tile_seq)
