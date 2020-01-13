def func1(n):
    if n < 1:
        return
    else:
        print(n, end=" ")
        func1(n-1)
        print(n, end=" ")

func1(3)
