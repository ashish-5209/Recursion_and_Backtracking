c = 0
def diceTrack(n):

    lis = []
    dicePrint(n, lis, 0)

def dicePrint(n, lis, s, a = 0):
    for i in range(a):
        print(" ", end=" ")
    if n != 0:
        print("dicePrint("+str(n)+", "+str(lis)+", "+str(a)+"):")
    else:
        print("dicePrint("+str(n)+", "+str(lis)+", "+str(a)+"):", end=" ")
    global c
    c += 1
    if n == 0:
        if sum(lis) == 7:
            print(lis)
        return
    else:
        for i in range(1, 7):
            if ((s+i+1*(n-1))<=7) and ((s+i+6*(n-1))>=7):
                lis.append(i)
                dicePrint(n-1, lis,s+i, a+1)
                lis.pop()

diceTrack(3)

print(c)
