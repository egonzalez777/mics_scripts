import random
import pprint


class Percolate(object):
    N = None
    grid = None
    i = set()

    def __init__(self, N):
        self.N = N
        self.grid = [[0 for k in [0]*N] for i in [0]*N]

        self.c = 0
        rand = random.randint(0, 10)
        n = N*N/rand
        print '-----', n, '--------'
        while True:
            i = random.randint(0, N-1)
            j = random.randint(0, N-1)
            self.union(i, j)
            self.i.add((i, j))
            self.c = self.c + 1
            if self.c == n:
                break

    def connected(self, i, j):
        return True

    def union(self, i, j):
        self.grid[i][j] = 1

    def percolates(self):
        return self.N**2 - float(self.c) < self.c



def main(i):
    p = Percolate(i)
    pp = pprint.PrettyPrinter()

    pp.pprint(p.grid)
    print(p.i)
    print(p.percolates())


if __name__ == '__main__':
    import sys

    args = sys.argv;
    if len(args) > 1:
        i = int(args[1])
    main(i)
