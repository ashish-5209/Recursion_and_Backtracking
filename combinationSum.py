lis = []

def combinationalSum(a,s):
    op=[]
    a = list(set(a))
    a.sort()
    combSum(a,s,0,[],op)
    return op

def combSum(a,s,i,l,op):

        if(s<0):
            return
        if(s==0):
            op.append(list(l))
            return
        while(i<len(a)):
            l.append(a[i])
            combSum(a,s-a[i],i,l,op)
            i+=1
            l.pop()
a = [2,4,6,8]
s = 8
lis = combinationalSum(a, s)
print(lis)
