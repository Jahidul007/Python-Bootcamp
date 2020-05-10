class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = list(str(n))
        i = len(s) - 1

        while i - 1 >= 0 and s[i - 1] >= s[i]:
            i -= 1

        if i == 0: return -1

        j = len(s) - 1
        while s[j] <= s[i - 1]:
            j -= 1
            # swap the values
        s[i - 1], s[j] = s[j], s[i - 1]
        # reverse the list after i-1
        s[i:] = s[i:][::-1]
        res = int(''.join(s))

        if res <= 2 ** 31 - 1:
            return res
        return -1
