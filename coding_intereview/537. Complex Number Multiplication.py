class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        # i^2=-1,(a+bi)*(a+bi)=a^2+2abi-b^2

        a = a.split("+")
        a1 = a[0]
        b1 = a[1][:-1]

        b = b.split("+")
        a2 = b[0]
        b2 = b[1][:-1]

        real = int(a1) * int(a2) - int(b1) * int(b2)
        imag = int(a1) * int(b2) + int(a2) * int(b1)

        return "{}+{}i".format(str(real), str(imag))