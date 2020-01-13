def BoundaryTraversal(a,n,m):
    #code here

    for i in range(m):
        print(a[0][i], end=" ")

    for i in range(1,n):
        print(a[i][m-1], end=" ")

    for i in range(m-2, -1, -1):
        print(a[n-1][i], end=" ")

    for i in range(n-2, 0, -1):
        print(a[i][0], end= " ")

a = [[5, 11, 30], [5, 19, 19]]
BoundaryTraversal(a, 2, 3)
