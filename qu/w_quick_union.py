import quick_union


class WQuickUnion(quick_union.QuickUnion):

    def __init__(self, N):
        super(WQuickUnion, self).__init__(N)
        self.size = [1 for k in [1]*N]

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if i == j:
            return

        if self.size[p] < self.size[q]:
            self.ids[i] = j
            self.size[j] = self.size[i] + self.size[j]
        else:
            self.ids[j] = i
            self.size[i] = self.size[j] + self.size[i]



m = WQuickUnion(10)

m.union(4, 3)
m.union(3, 8)
m.union(6, 5)
m.union(9, 4)
m.union(2, 1)
m.union(5, 0)
m.union(7, 2)
m.union(6, 1)
m.union(7, 3)

# Should log [6, 2, 6, 4, 6, 6, 2, 4, 4]

print m.size, m.ids
