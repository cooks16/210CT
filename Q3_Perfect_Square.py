def square(x):
    i = x * x
    y = x
    # continue to half the number until i find a perfect square below the number given
    while i > x:
        y //= 2
        i = y * y
    # increase in intervals of 1 until the perfect square becomes larger than the number given
    while i < x:
        y += 1
        i = y * y
    # subtract 1 and square the result to find the closest perfect square which is less than the number given
    y -= 1
    i = y * y
    return i


print(square(1423))
