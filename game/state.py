import numpy as np
from copy import deepcopy
from typing import List
from math import sqrt, floor


class State:
    def __init__(self, tile_seq=[], depth=0, weight=0):
        self.tile_seq = tile_seq
        self.depth = depth
        self.weight = weight

    def flatten(self) -> "np.ndarray[np.float64]":
        """Flattens the nested array structure into a one dimensional array

        Returns:
            Flattened array
        """

        tiles = np.zeros(len(self.tile_seq) * len(self.tile_seq[0]))
        index = 0
        for row in self.tile_seq:
            for item in row:
                tiles[index] = item
                index += 1
        return tiles

    def move(self, direction: str) -> "State":
        """ Moves the empty tile in the given direction

        Args:
            direction: `str` - "up", "right", "down" or "left"

        Returns:
            All possible states after the move is done.
        Raises:
            IndexError: If the move is unsupported
        """

        new_state = State(deepcopy(self.tile_seq), self.depth + 1, self.weight)

        coordinates = np.argwhere(new_state.tile_seq == 0).flatten()
        current_x, current_y = coordinates[1], coordinates[0]

        if direction == "up":
            if current_y == 0:
                raise IndexError

            target_x = current_x
            target_y = current_y - 1

            new_state.tile_seq[current_y][current_x] = new_state.tile_seq[target_y][
                target_x
            ]
            new_state.tile_seq[target_y][target_x] = 0

        elif direction == "right":
            if current_x == 3:
                raise IndexError

            target_x = current_x + 1
            target_y = current_y

            new_state.tile_seq[current_y][current_x] = new_state.tile_seq[target_y][
                target_x
            ]
            new_state.tile_seq[target_y][target_x] = 0

        elif direction == "down":
            if current_y == 3:
                raise IndexError

            target_x = current_x
            target_y = current_y + 1

            new_state.tile_seq[current_y][current_x] = new_state.tile_seq[target_y][
                target_x
            ]
            new_state.tile_seq[target_y][target_x] = 0

        elif direction == "left":
            if current_x == 0:
                raise IndexError

            target_x = current_x - 1
            target_y = current_y

            new_state.tile_seq[current_y][current_x] = new_state.tile_seq[target_y][
                target_x
            ]
            new_state.tile_seq[target_y][target_x] = 0

        return new_state

    def neighbors(self) -> List["State"]:
        """Computes all future states possible from current situation

        Returns:
            List[State]: All possible states
        """
        neighbors = list()

        try:
            neighbors.append(self.move("right"))
        except IndexError:
            pass

        try:
            neighbors.append(self.move("left"))
        except IndexError:
            pass

        try:
            neighbors.append(self.move("up"))
        except IndexError:
            pass

        try:
            neighbors.append(self.move("down"))
        except IndexError:
            pass

        return neighbors

    def heuristic_score(self, target_state: "State", current_depth: int) -> int:
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
        h1 = self.misplaced_tiles(target_state)
        h2 = self.misplaced_distances(target_state)
        h3 = 2 * self.tile_reversals(target_state)
        h4 = self.euclidean_distance(target_state)

        # Set the heuristic value for current state
        return current_depth + h1 + h2 + h3 + h4

    def misplaced_tiles(self, target_state: "State") -> int:
        """Counts all misplaced tiles

        Returns:
            int: misplaced tile count
        """
        return np.sum(self.tile_seq != target_state.tile_seq)

    def misplaced_distances(self, target_state: "State") -> int:
        """ Calculates Manhattan distance 
        
        Returns:
            int: misplaced distances
        """
        distance = 0

        current_tiles = self.tile_seq
        target_tiles = target_state.tile_seq

        for current_x, current_y in np.ndindex(current_tiles.shape):
            for goal_x, goal_y in np.ndindex(target_tiles.shape):
                if self[current_y][current_x] == target_state[goal_y][goal_x]:
                    distance += abs(current_y - goal_y) + abs(current_x - goal_x)

        return distance

    def euclidean_distance(self, target_state: "State") -> int:
        """ Calculates Euclidean distance 
        
        Returns:
            int: misplaced distances
        """
        distance = 0

        current_tiles = self.tile_seq
        target_tiles = target_state.tile_seq

        for current_x, current_y in np.ndindex(current_tiles.shape):
            for goal_x, goal_y in np.ndindex(target_tiles.shape):
                if self[current_y][current_x] == target_state[goal_y][goal_x]:
                    distance += sqrt(
                        pow(current_y - goal_y, 2) + pow(current_x - goal_x, 2)
                    )
        return floor(distance)

    def tile_reversals(self, target_state: "State") -> int:
        """Counts tiles that are reversed to each other

        Returns:
            int: reversed tiles
        """
        reversals = 0

        current_tiles = self.tile_seq
        for row, col in np.ndindex(current_tiles.shape):
            if row != 2:
                if self[row][col] == target_state[row + 1][col]:
                    reversals += 1
            if col != 2:
                if self[row][col] == target_state[row][col + 1]:
                    reversals += 1

        return reversals

    def __getitem__(self, index: int) -> List[int]:
        return self.tile_seq[index]

    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, self.__class__):
            return False

        return bool(np.all(self.tile_seq == obj.tile_seq))

    def __ne__(self, obj: object) -> bool:
        return not self == obj

    def __hash__(self) -> int:
        return hash((np.array2string(self.tile_seq)))

    def __str__(self):
        return np.array2string(self.tile_seq)

    def __repr__(self):
        return self.tile_seq.__repr__()
