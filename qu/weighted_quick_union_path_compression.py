import weighted_quick_union

class WeightedQuickUnionPathCompression(weighted_quick_union.WeightedQuickUnion):

    def __init__(self, N):
        super(WeightedQuickUnionPathCompression, self).__init__(N)

    def root(self, i):

        while (i != self.ids[i]):
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]

        return i


m = WeightedQuickUnionPathCompression(10)

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
