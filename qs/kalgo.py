n = 50
l = []

while n > 0:
    l.append(n % 2)
    n = n / 2
    print n


print ''.join(l)
