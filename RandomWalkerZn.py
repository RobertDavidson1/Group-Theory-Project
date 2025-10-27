import numpy as np
import pandas as pd


class RandomWalkerZn:
    def __init__(self, size, start=(0, 0), moves=None, seed=None):
        self.size = int(size)
        self.pos = np.array(start, dtype=int) % self.size
        self.moves = np.array(moves if moves is not None else [(1, 0), (-1, 0), (0, 1), (0, -1)], dtype=int)
        self.rng = np.random.default_rng(seed)

        self.history = None

    def step(self):
        pos_change = self.moves[self.rng.integers(len(self.moves))]
        self.pos = (self.pos + pos_change) % self.size
        return tuple(self.pos)

    def walk(self, steps, cache=True):
        t = int(steps)
        positions = np.empty((t + 1, 2), dtype=int)
        positions[0] = self.pos

        for i in range(1, t + 1):
            self.step()
            positions[i] = self.pos
        if cache:
            self.history = positions.copy()
        return positions

    def to_dataframe(self):
        if self.history is None:
            raise ValueError("No history yet. Call walk(...) first.")
        return pd.DataFrame(self.history, columns=["x", "y"])

    def __str__(self):
        return f"RandomWalkerZn(n={self.size}, pos=({self.pos[0]},{self.pos[1]}))"


if __name__ == "__main__":
    pass
