def prime(n, x):
    if n % 2 == 0:  # Check if even
        return False
    elif x == n:    # base case which is achieved when prime
        return True
    else:
        if n % x == 0:   # check if divisible
            return False
        else:   # call function moving towards base case
            return prime(n, x + 2)

print(prime(499, 3))
