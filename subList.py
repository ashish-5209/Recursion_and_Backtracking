def subList(lis, i,l, curr = ""):

    if i == len(lis):
        print(curr.strip().split(' '))
        l.append(curr.strip().split(' '))

    else:
        subList(lis, i+1, l, curr)
        subList(lis, i+1, l, curr+lis[i]+" ")

lis = ["James", "Bob", "Mat", "Sara"]
l = []
subList(lis, 0, l)
l.sort()
print(l)
