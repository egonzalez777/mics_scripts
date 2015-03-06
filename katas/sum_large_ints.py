import math

def sum_of_large_ints(n, m):
    def sum1ToN(x):
        return x * (x + 1) / 2;

    return (sum1ToN(m - 1) * (math.floor(n / m)) + sum1ToN(n % m))

print sum_of_large_ints(592929, 29283)


