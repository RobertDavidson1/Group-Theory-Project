from RandomWalkerZn import RandomWalkerZn


class WalkSim:
    @staticmethod
    def one_walk(size, steps, start=(0, 0), moves=None, seed=None, return_df=False):
        walker = RandomWalkerZn(size=size, start=start, moves=moves, seed=seed)
        path = walker.walk(steps)

        if return_df:
            return walker.to_dataframe()
        else:
            return path

    @staticmethod
    def many_walks(walkers, size, steps, start=(0, 0), moves=None, seeds=None, return_df=False):
        if seeds is None:
            seeds = range(walkers)

        paths = []
        for s in seeds:
            curr_walker = RandomWalkerZn(size=size, start=start, moves=moves, seed=s)
            path = curr_walker.walk(steps)
            if return_df:
                paths.append(curr_walker.to_dataframe())
            else:
                paths.append(path)
        return paths


if __name__ == "__main__":
    SIZE = 10
    STEPS = 5
    SEED = 3

    print(f"Random walk with size = {SIZE}, steps = {STEPS}, seed = {SEED}")
    path = WalkSim.one_walk(size=10, steps=5, seed=3)
    print(path)
