def reverseString(s):
    i = 0
    j = len(s)-1
    while i<j:
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp
        i+=1
        j-=1
    return s



print(reverseString(["h","e","l","l","o"]))
