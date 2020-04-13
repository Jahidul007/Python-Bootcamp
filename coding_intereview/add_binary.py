class Solution:
    def addBinary(self, a: str, b: str) -> str:
        revA = a[::-1]
        revB = b[::-1]

        lenA, lenB = len(a), len(b)

        if lenA > lenB:
            maxLen = lenA
            revB += '0' * (lenA - lenB)
        else:
            revA += '0' * (lenB - lenA)
            maxLen = lenB

        carry = 0
        ans = [0] * maxLen
        for i in range(maxLen):
            if revA[i] == '0' and revB[i] == '0':
                ans[i] = carry
                carry = 0
            elif revA[i] == '1' and revB[i] == '1':
                ans[i] = carry
                carry = 1
            else:
                if carry == 0:
                    ans[i] = 1
                else:
                    ans[i] = 0
                    carry = 1
        if carry:
            ans.append(carry)
        return "".join(str(x) for x in ans[::-1])


print(Solution().addBinary('11', '1'))
