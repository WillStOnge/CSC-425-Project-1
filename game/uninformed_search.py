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

       procedure BFS(G, root) is
2      * let Q be a queue
3      * label root as discovered
4      * Q.enqueue(root)
5      * while Q is not empty do
6      *   v := Q.dequeue()
7      *   if v is the goal then
8      *       return v
9      *   for all edges from v to w in G.adjacentEdges(v) do
10     *       if w is not labeled as discovered then
11                 label w as discovered
12                 w.parent := v
13                 Q.enqueue(w)
        """
        if not self.is_solvable():
            print("UNSOLVABLE")
            exit(1)

        # print(self.closed)
        observed_state: State = self.opened.popleft()

        if np.all(observed_state.tile_seq == self.target_state.tile_seq):
            self.current_state = observed_state

        self.closed.add(observed_state)

        for neighbor in observed_state.neighbors():
            # print(neighbor in self.closed)
            if neighbor not in self.closed and neighbor not in self.opened:
                self.opened.append(neighbor)

    def run(self):
        """Runs the search"""
        print(f"Initial State: \n{self.current_state.tile_seq}")
        print("---------")
        path = 0

        while not self.current_state == self.target_state:
            self.next_state()
            path += 1

        print(self.current_state.tile_seq)

        print("It took ", path, " iterations")
        print("The length of the path is: ", self.current_state.depth)
        # output the goal state
        print(self.target_state.tile_seq)
        print("goal state !!!!!")
