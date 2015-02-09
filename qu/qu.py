class UF(object):
    ids = []

    def __init__(self, N):
        self.ids = [0]*N
        for (k, v) in enumerate(self.ids):
            self.ids[k] = k;

    def connected(self, p, q):
        return self.ids[p] == self.ids[q]

    def union(self, p, q):
        if self.connected(p, q):
            return

        pid = self.ids[p]

        for (i, k) in enumerate(self.ids):
            if self.ids[i] == pid:
                self.ids[i] = self.ids[q]


if __name__ == '__main__':
    m = UF(10)

    m.union(6, 5)
    m.union(2, 0)
    m.union(0, 6)
    m.union(1, 5)
    m.union(3, 9)
    m.union(9, 6)

    print m.ids

