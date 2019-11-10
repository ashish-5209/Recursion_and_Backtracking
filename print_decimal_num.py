def decimal(n, curr = "", a = 0):
    for i in range(a):
        print(" ", end=" ")
    if n != 0:
        print("binary("+str(n)+", "+str(curr)+", "+str(a)+"):")
    else:
        print("binary("+str(n)+", "+str(curr)+", "+str(a)+"):", end=" ")

    if n == 0:
        print(curr)
        return
    else:
        for i in range(10):
            decimal(n-1, curr + str(i), a+1)

decimal(3)
