def rotateString(A: str, B: str):
    if len(A) == len(B) and len(A) > 0:
        s = A + A
        if (s).find(B) > 0:
            return True
    return False

'''
return B in S
'''


print(rotateString('', ''))
