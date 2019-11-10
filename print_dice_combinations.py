def diceTrack(n):
    lis = []
    dicePrint(n, lis)

def dicePrint(n, lis, a = 0):

    for i in range(a):
        print(" ", end=" ")
    if n != 0:
        print("binary("+str(n)+", "+str(lis)+", "+str(a)+"):")
    else:
        print("binary("+str(n)+", "+str(lis)+", "+str(a)+"):", end=" ")

    if n == 0:
        print(lis)

    else:
        for i in range(1, 7):
            lis.append(i)
            dicePrint(n-1, lis, a + 1)
            lis.pop()

diceTrack(3)
