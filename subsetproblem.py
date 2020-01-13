def subset(s,l, r,ls, curr = ""):
    if l == r:
        if curr != '':
            ls.append(curr)
        return
    subset(s, l+1, r,ls, curr+s[l])
    subset(s, l+1, r,ls, curr)

ls = []
subset("ABC", 0, 3, ls)
ls.sort()
print(ls)
#print(ls)
