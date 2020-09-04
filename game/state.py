import numpy as np
from copy import deepcopy
from typing import List


class State:
    def __init__(self, tile_seq=[], depth=0, weight=0):
        self.tile_seq = tile_seq
        self.depth = depth
        self.weight = weight

    def is_solvable(self) -> bool:
        """Detects if the current puzzle has a solution

        Returns:
            bool: if the puzzle is solvable
        """
        inv_count = 0
        arr = self.flatten()
        for i in range(0, 9):
            for j in range(i + 1, 9):
                if arr[j] and arr[i] and arr[i] > arr[j]:
                    inv_count += 1
        return inv_count % 2 == 0

    def flatten(self) -> List[int]:
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

            # ipdb.set_trace()
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

    def __getitem__(self, index: int) -> List[int]:
        return self.tile_seq[index]

    def __eq__(self, obj: "State") -> bool:
        if not isinstance(obj, self.__class__):
            return False

        return np.all(self.tile_seq == obj.tile_seq)

    def __ne__(self, obj: "State") -> bool:
        return not self == obj

    def __hash__(self) -> str:
        return hash((np.array2string(self.tile_seq)))

    def __str__(self):
        return np.array2string(self.tile_seq)

    def __repr__(self):
        return self.tile_seq.__repr__()
