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
    openlist = []
    closed = []
    depth = 0

    def __init__(self, current, goal):
        self.current = current
        self.goal = goal
        self.openlist.append(current)

    def sortFun(self, e):
        return e.weight

    """
     * check if the generated state is in open or closed
     * the purpose is to avoid a circle
     * @param s
     * @return
    """

    def check_inclusive(self, s):
        in_open = 0
        in_closed = 0
        ret = [-1, -1]

        for item in self.openlist:
            if item.equals(s):
                in_open = 1
                ret[1] = self.openlist.index(item)
                break

        for item in self.closed:
            if item.equals(s):
                in_closed = 1
                ret[1] = self.closed.index(item)
                break

        if in_open == 0 and in_closed == 0:
            ret[0] = 1  # the child is not in open or closed
        elif in_open == 1 and in_closed == 0:
            ret[0] = 2  # the child is already in open
        elif in_open == 0 and in_closed == 1:
            ret[0] = 3  # the child is already in closed
        return ret

    """
     * four types of walks
     * best first search
     *  ↑ ↓ ← → (move up, move down, move left, move right)
     * the blank tile is represent by '0'
    """

    def state_walk(self):
        # add closed state
        self.closed.append(self.current)
        self.openlist.remove(self.current)
        # move to the next heuristic state
        walk_state = self.current.tile_seq
        row = 0
        col = 0

        for i in range(len(walk_state)):
            for j in range(len(walk_state[i])):
                if walk_state[i, j] == 0:
                    row = i
                    col = j
                    break

        self.depth += 1

        """ The following program is used to do the state space walk """
        # ↑ move up
        if (row - 1) >= 0:
            # TODO your code start here
            """
             *get the 2d array of current 
             *define a temp 2d array and loop over current.tile_seq
             *pass the value from current.tile_seq to temp array
             *↑ is correspond to (row, col) and (row-1, col)
             *exchange these two tiles of temp
             *define a new temp state via temp array
             *call check_inclusive(temp state)
             *do the next steps according to flag
             *if flag = 1 //not in open and closed
             *begin
             *assign the child a heuristic value via heuristic_test(temp state);
             *add the child to open
             *end;
             *if flag = 2 //in the open list
             *if the child was reached by a shorter path
             *then give the state on open the shorter path
             *if flag = 3 //in the closed list
             *if the child was reached by a shorter path then
             *begin
             *remove the state from closed;
             *add the child to open
             *end;
            """
            # TODO your code end here

        # ↓ move down
        if (row + 1) < len(walk_state):
            # TODO your code start here
            """
             *get the 2d array of current 
             *define a temp 2d array and loop over current.tile_seq
             *pass the value from current.tile_seq to temp array
             *↓ is correspond to (row, col) and (row+1, col)
             *exchange these two tiles of temp
             *define a new temp state via temp array
             *call check_inclusive(temp state)
             *do the next steps according to flag
             *if flag = 1 //not in open and closed
             *begin
             *assign the child a heuristic value via heuristic_test(temp state);
             *add the child to open
             *end;
             *if flag = 2 //in the open list
             *if the child was reached by a shorter path
             *then give the state on open the shorter path
             *if flag = 3 //in the closed list
             *if the child was reached by a shorter path then
             *begin
             *remove the state from closed;
             *add the child to open
             *end;
            """
            # TODO your code end here

        # ← move left
        if (col - 1) >= 0:
            # TODO your code start here
            """
             *get the 2d array of current 
             *define a temp 2d array and loop over current.tile_seq
             *pass the value from current.tile_seq to temp array
             *← is correspond to (row, col) and (row, col-1)
             *exchange these two tiles of temp
             *define a new temp state via temp array
             *call check_inclusive(temp state)
             *do the next steps according to flag
             *if flag = 1 //not in open and closed
             *begin
             *assign the child a heuristic value via heuristic_test(temp state);
             *add the child to open
             *end;
             *if flag = 2 //in the open list
             *if the child was reached by a shorter path
             *then give the state on open the shorter path
             *if flag = 3 //in the closed list
             *if the child was reached by a shorter path then
             *begin
             *remove the state from closed;
             *add the child to open
             *end;
            """
            # TODO your code end here

        # → move right
        if (col + 1) < len(walk_state):
            # TODO your code start here
            """
             *get the 2d array of current 
             *define a temp 2d array and loop over current.tile_seq
             *pass the value from current.tile_seq to temp array
             *→ is correspond to (row, col) and (row, col+1)
             *exchange these two tiles of temp
             *define a new temp state via temp array
             *call check_inclusive(temp state)
             *do the next steps according to flag
             *if flag = 1 //not in open and closed
             *begin
             *assign the child a heuristic value via heuristic_test(temp state);
             *add the child to open
             *end;
             *if flag = 2 //in the open list
             *if the child was reached by a shorter path
             *then give the state on open the shorter path
             *if flag = 3 //in the closed list
             *if the child was reached by a shorter path then
             *begin
             *remove the state from closed;
             *add the child to open
             *end;
            """
            # TODO your code end here

        # sort the open list first by h(n) then g(n)
        self.openlist.sort(key=self.sortFun)
        self.current = self.openlist[0]

    """
     * Solve the game using heuristic search strategies
     
     * There are three types of heuristic rules:
     * (1) Tiles out of place
     * (2) Sum of distances out of place
     * (3) 2 x the number of direct tile reversals
     
     * evaluation function
     * f(n) = g(n) + h(n)
     * g(n) = depth of path length to start state
     * h(n) = (1) + (2) + (3)
    """

    def heuristic_test(self, current):
        curr_seq = current.tile_seq
        goal_seq = self.goal.tile_seq

        # (1) Tiles out of place
        h1 = 0
        # TODO your code start here
        for r in range(len(curr_seq)):
            for c in range(len(curr_seq[r])):
                if curr_seq[r][c] != goal_seq[r][c]:
                    h1 += 1


        # TODO your code end here

        # (2) Sum of distances out of place
        h2 = 0
        # TODO your code start here
        for curr_row in range(len(curr_seq)):
            for curr_col in range(len(curr_seq[curr_row])):
                for goal_row in range(len(goal_seq)):
                    for goal_col in range(len(goal_seq[goal_row])):
                        if curr_seq[curr_row][curr_col] == goal_seq[goal_row][goal_col]:
                            h2 += abs(curr_row-goal_row) + abs(curr_col-goal_col)
        # TODO your code end here

        # (3) 2 x the number of direct tile reversals
        h3 = 0
        # TODO your code start here
        for row in range(len(goal_seq)):
            for col in range(len(goal_seq[row])-1):
                if goal_seq[row][col] == curr_seq[row+1][col] and goal_seq[row+1][col] == curr_seq[row][col] and \
                        curr_seq[row][col] != 0 and curr_seq[row+1][col] != 0:
                    h3 += 1
                elif goal_seq[row][col] == curr_seq[row][col+1] and goal_seq[row][col+1] == curr_seq[row][col] and \
                        curr_seq[row][col] != 0 and curr_seq[row][col+1] != 0:
                    h3 += 1
        # TODO your code end here

        h3 *= 2

        # set the heuristic value for current state
        current.weight = current.depth + h1 + h2 + h3

    # You can choose to print all the states on the search path, or just the start and goal state
    def run(self):
        # output the start state
        print("start state !!!!!")
        print(self.current.tile_seq)

        path = 0

        while not self.current.equals(self.goal):
            self.state_walk()
            print(self.current.tile_seq)
            path += 1

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current.depth)
        # output the goal state
        target = self.goal.tile_seq
        print(target)
        print("goal state !!!!!")
