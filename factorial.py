def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

def fact1(n, k = 1):
    if n == 0:
        return k
    else:
        return fact1(n-1, n*k)

print(fact(5))
print(fact1(5))
