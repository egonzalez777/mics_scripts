# v['a'] = 1.0
# b = b - (b*v)*v  >>> setitem(v, 'a', 1.0)
# print(b)         >>> b = add(b, neg(scalar_mul(v, dot(b,v))))


class Vec:
    # Operator overloading

    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    def add(u, v):
        '''Returns the sum of the two vectors'''
        assert u.D == v.D
        pass
