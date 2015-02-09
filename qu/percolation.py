from
from time import time


class Percolate(object):
    grid = [][]

    def __init__(self, N):
        self.grid = [0]

    def connected(self, i, j):
        return True

    def union(self, i, j):
        pass

    def percolates(self):
        pass



def main(i):
    p = Percolate(i)
    print p.grid
    count = 0
    tries =

    while count <

if __name__ == '__main__':
    import sys

    args = sys.argv;
    if len(args) > 1:
        i = int(args[1])
    main(i)
