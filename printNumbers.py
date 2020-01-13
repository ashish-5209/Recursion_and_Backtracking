def oneToN(n):
    if n < 1:
        return
    else:
        oneToN(n-1)
        print(n, end=" ")

def OneToNT(n, k = 1):
    if n < 1:
        return
    else:
        print(k, end=' ')
        OneToNT(n-1, k+1)

def NtoOne(n):
    if n < 1:
        return
    else:
        print(n, end = " ")
        NtoOne(n-1)

oneToN(10)
print()
OneToNT(10)
print()
NtoOne(10)
