def permute(s, curr, a = 0):

    for i in range(a):
        print(" ", end=" ")
    if len(s) != 0:
        print("permute("+"".join(s)+", "+"".join(curr)+", "+str(a)+"):", end=" ")
        print("".join(curr))
    else:
        print("permute("+"".join(s)+", "+"".join(curr)+", "+str(a)+"):", end=" ")

    if len(s) == 0:
        print("".join(curr))
    else:
        for i in range(len(s)):
            c = s[i]
            curr.append(c)
            s.pop(i)
            permute(s, curr, a+1)

            s.insert(i, c)
            curr.pop()

s = ['A','B','C']

permute(s, [])
