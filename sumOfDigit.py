def countD(n):

    if n < 10:
        return n
    else:
        return countD(n//10) + n%10

print(countD(298716))
