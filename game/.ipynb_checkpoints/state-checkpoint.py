import numpy as np
from typing import List


class State:
    def __init__(self, tile_seq=[], depth=0, weight=0):
        self.tile_seq = tile_seq
        self.depth = depth
        self.weight = weight

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

    def __eq__(self, obj: State) -> bool:
        return self.tile_seq == obj.tile_seq

    def __ne__(self, obj: State) -> bool:
        return not self == obj
