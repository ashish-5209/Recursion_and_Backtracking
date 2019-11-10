def binary(n, curr = "", a = 0):
    for i in range(a):
        print(" ", end=" ")
    if n != 0:
        print("binary("+str(n)+", "+str(curr)+", "+str(a)+"):")
    else:
        print("binary("+str(n)+", "+str(curr)+", "+str(a)+"):", end=" ")
    if n == 0:
        print(curr)
    else:
        binary(n-1, curr+"0", a+1)
        binary(n-1, curr+"1", a+1)

binary(5)
