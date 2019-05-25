import string

def ispangram(str1,alphabet = string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
a = ispangram("The quick brown fox jumps over the lazy dog")
print(a)

def vol(rad):
    return (4.0/3)*(3.14)*(rad**3)
print(vol(5))

