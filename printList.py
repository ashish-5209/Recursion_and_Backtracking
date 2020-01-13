def printL1(s):
    for i in range(len(s)-1, -1, -1):
        print(s[i], end=' ')

def printL2(s, l = 0):

    if l == len(s):
        return
    else:
        printL2(s, l+1)
        print(s[l], end=" ")

printL1("ASHISH")
print()
printL2("ASHISH", 0)
