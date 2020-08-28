from .state import State

"""
This class implement the Best-First-Search (BFS) algorithm
along with the Heuristic search strategies

In this algorithm, an OPEN list is used to store the unexplored states and
a CLOSE list is used to store the visited state. OPEN list is a priority queue.
The priority is insured through sorting the OPEN list each time after new
states are generated and added into the list.
The heuristics are used as sorting criteria.

In this informed search, reducing the state space search complexity is
the main criterion.
We define heuristic evaluations to reduce the states that
need to be checked every iteration.
Evaluation function is used to express the quality of informedness
of a heuristic algorithm.



class InformedSearchSolver:
    current = State()
    goal = State()
    openList = []
    closeList = []
    pathLength = 0

    def __init__(self, current, goal):
        self.current = current
        self.goal = goal
        self.openlist.append(current)

    def getWeight(self, e):
        return e.weight

    """
     * Check if the generated state is in open or closed. 
     * The purpose is to avoid looping.
    """
    def check_inclusive(self, state):
        in_open = 0
        in_closed = 0
        ret = [-1, -1]

        for item in self.openlist:
            if item.equals(state):
                in_open = 1
                ret[1] = self.openlist.index(item)
                break

        # finds s in the closed list
        for item in self.closeList:
            if item.equals(state):
                in_closed = 1
                ret[1] = self.closeList.index(item)
                break

        if in_open == 0 and in_closed == 0:
            ret[0] = 1  # the child is not in open or closed
        elif in_open == 1 and in_closed == 0:
            ret[0] = 2  # the child is already in open
        elif in_open == 0 and in_closed == 1:
            ret[0] = 3  # the child is already in closed
        return ret

    """
     * Four directions to walk (up, down, left, right)
     * Uses the Best-first Search algorithm
     *  
     * The blank tile is represent by '0'
    """
    def next_state(self):
        # add closed state
        self.closeList.append(self.current)
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

        self.pathLength += 1

        """ The following program is used to do the state space walk """
        # ↑ move up
        if (row - 1) >= 0:
            tempState = self.current.move('up')

            child = self.openList.pop(0)
            flag = self.check_inclusive(child)

            if flag[0] == 1:
                child.weight = heuristic_test(tempState)
                self.openList.append(child)
            elif flag[0] == 2:
                if child.pathLength < self.current.pathLength:
                    temp = None # Give the state on open the shorter path?
            elif flag[0] == 3:
                if child.pathLength < self.current.pathLength:
                    self.closeList.remove(child)
                    self.openList.append(child)

        # ↓ move down
        if (row + 1) < len(walk_state):
            tempState = self.current.move('down')
            # TODO your code start here
            """
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
            tempState = self.current.move('left')
            # TODO your code start here
            """
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

        # → move right
        if (col + 1) < len(walk_state):
            tempState = self.current.move('right')
            """
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

        # Sort the open list by h(n) then g(n)
        self.openlist.sort(key=self.getWeight)
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
        for r in range(len(curr_seq)):
            for c in range(len(curr_seq[r])):
                if curr_seq[r][c] != goal_seq[r][c]:
                    h1 += 1

        # (2) Sum of distances out of place
        h2 = 0
        for curr_row in range(len(curr_seq)):
            for curr_col in range(len(curr_seq[curr_row])):
                for goal_row in range(len(goal_seq)):
                    for goal_col in range(len(goal_seq[goal_row])):
                        if curr_seq[curr_row][curr_col] == goal_seq[goal_row][goal_col]:
                            h2 += abs(curr_row-goal_row) + abs(curr_col-goal_col)

        # (3) Double the number of direct tile reversals
        h3 = 0
        for row in range(len(goal_seq)):
            for col in range(len(goal_seq[row])-1):
                if goal_seq[row][col] == curr_seq[row+1][col] and goal_seq[row+1][col] == curr_seq[row][col] and \
                        curr_seq[row][col] != 0 and curr_seq[row+1][col] != 0:
                    h3 += 1
                elif goal_seq[row][col] == curr_seq[row][col+1] and goal_seq[row][col+1] == curr_seq[row][col] and \
                        curr_seq[row][col] != 0 and curr_seq[row][col+1] != 0:
                    h3 += 1

        h3 *= 2

        # Set the heuristic value for current state
        current.weight = current.pathLength + h1 + h2 + h3

    """
     * You can choose to print all the states on the search path, or just the start and goal state
    """
    def run(self):
        # Output the start state
        print("Start State:")
        print(self.current.tile_seq)

        path = 0

        while not self.current.equals(self.goal):
            self.next_state()
            print(self.current.tile_seq)
            path += 1

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current.pathLength)
        # Output the goal state
        print("Goal State:")
        print(self.goal.tile_seq)