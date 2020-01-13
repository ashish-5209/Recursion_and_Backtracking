def maxC(n, a, b, c):

    if n < 0:
        return -1
    elif n == 0:
        return 0

    res = max(maxC(n-a, a, b, c),
            maxC(n-b, a, b, c),
            maxC(n-c, a, b, c))

    return -1 if res == -1 else res+1


print(maxC(5, 2, 5, 1))
print(maxC(23, 11, 12, 9))
