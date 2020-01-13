def func(a,i = 0, curr = ""):
    global lis
    if i == len(a):
        lis.add(curr)
        return
    else:
        func(a,i+1, curr)
        func(a,i+1, curr+str(a[i]))
a = [1,2,2]
lis = set()
func(a)
lis = sorted(lis)

print(lis)
