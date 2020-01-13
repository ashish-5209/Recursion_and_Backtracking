def palindrom(s, l, r):

    if l >= r:
        return True
    else:
        if s[l] != s[r]:
            return False
        else:
            return palindrom(s, l+1, r-1)

print(palindrom("Ashish", 0, 5))
