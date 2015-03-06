def fib():
    a, b = 0, 1
    yield a
    yield b
    c = 0
    while True:
        a, b = b, a + b
        c = c + 1
        if c == 12:
            break
        yield b

for f in fib():
    print f
