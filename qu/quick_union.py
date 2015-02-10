class QuickUnion(object):
    ids = []

    def __init__(self, N):
        self.ids = [0]*N
        for (k, v) in enumerate(self.ids):
            self.ids[k] = k;

    def root(self, p):
        while p != self.ids[p]:
            p = self.ids[p]
        return p

    def connected(self, p, q):
        return self.root(self.ids[p]) == self.root(self.ids[q])

    def union(self, p, q):
        if self.connected(p, q):
            return
        i = self.root(p)
        j = self.root(q)

        ''''pid = self.ids[p]

        for (i, k) in enumerate(self.ids):
            if self.ids[i] == pid:
                self.ids[i] = self.ids[q]'''
        self.ids[i] = j


if __name__ == '__main__':
    m = QuickUnion(10)

    m.union(4, 3)
    m.union(3, 8)
    m.union(6, 5)
    m.union(9, 4)
    m.union(2, 1)
    m.union(5, 0)
    m.union(7, 2)
    m.union(6, 1)
    m.union(7, 3)

    print m.ids
