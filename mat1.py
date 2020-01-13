def reverseCol(n1, m1, arr1):
    #Your code here

    for i in range(n1):

        for j in range(m1):
            if j < m1//2:
                arr1[i][j], arr1[i][m1-1-j] = arr1[i][m1-1-j], arr1[i][j]

                print(arr1[i][j], end=" ")
            else:
                print(arr1[i][j], end=" ")

arr1 = [[1 ,2 ,3] ,[5 ,6 ,7] ,[9 ,10 ,11] ,[13 ,14 ,15]]
reverseCol(4, 3, arr1)
