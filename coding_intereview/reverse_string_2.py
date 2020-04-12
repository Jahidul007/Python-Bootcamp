def reverseString(s,k):
    i = 0
    j = len(s)-1
    while i<k:
        tmp = s[i]
        s[i] = s[k]
        s[k] = tmp
        i+=1
        k-=1
    return s



print(reverseString('abcdefg',2))