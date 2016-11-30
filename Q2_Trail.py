def fac(x):
    y = 1
    while x > 1:
        y *= x
        x -= 1
    print(y)


def trail(x):
    fac(x)
    n = 1
    y = x
    z = 0
    while y > 0:
        y = x // (5**n)
        n += 1
        z += y
    return z
print(trail(13))
